from cefpython3 import cefpython as cef
import sys
import os
import win32gui
import win32api
import ctypes
import inspect
import re


def GetTaskBarHeight():
    monitorInfo = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
    monitorArea = monitorInfo.get("Monitor")
    workArea = monitorInfo.get("Work")
    taskbarHeight = monitorArea[3]-workArea[3]
    return taskbarHeight


def GetScreenSize():
    user32 = ctypes.windll.user32
    screenWidth = user32.GetSystemMetrics(0)
    screenHeight = user32.GetSystemMetrics(1)
    return screenWidth, screenHeight


def SetWindowSizeAndPos(width, height, left, top):
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, left, top, width, height, True)


def GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight):
    screenWidth, screenHeight = GetScreenSize()
    taskbarHeight = GetTaskBarHeight()

    windowLeft = int((screenWidth - windowWidth) / 2)
    windowTop = int(((screenHeight - taskbarHeight) - windowHeight) / 2)

    return windowLeft, windowTop


def EnableHighDPISupport():
    cef.DpiAware.EnableHighDpiSupport()


def GetVariableName(vari):
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bGetVariableName\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


def GetFunctionName(func):
    return func.__name__


def LocalizeURL(URL):
    # Try to find protocol sign
    if URL.find("://") != -1:
        # This URL has its own protocol, ust return, don't process
        return URL

    # Have No Protocol, it must be a local file system path
    # Transform it into a URL with 'file://' protocol

    # Linuxlize the URL
    linuxlizedURL = URL.replace("\\", "/")

    # Clean the 'this folder' definition
    if linuxlizedURL[0:2] == "./":
        linuxlizedURL = linuxlizedURL[2:]

    # Get Linuxlized CWD Path
    linuxlizedCWD = os.getcwd().replace("\\", "/")

    # Merge and Generate the Target URL
    targetURL = "file:///" + linuxlizedCWD + "/" + linuxlizedURL
    return targetURL


def VariableHookee(url, name, value):
    return {
        "type": "VariableHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "name": name,
        "value": value
    }


def FunctionHookee(url, name, function):
    return {
        "type": "FunctionHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "name": name,
        "function": function
    }


def CodeHookee(url, jsCode):
    return {
        "type": "CodeHookee",
        "url": LocalizeURL(url) if url is not None else None,
        "jsCode": jsCode
    }


class Communicator:
    # Public Hookees
    hookees = []

    # Hooker
    @classmethod
    def OnLoadingStateChange(cls, browser, is_loading, **_):
        # When the page is loading
        if not is_loading:
            # When the page finished loading

            # Create JS Binding Object
            js = cef.JavascriptBindings()

            for hookee in cls.hookees:
                if hookee["type"] == "VariableHookee":
                    # Pass Variable to JS
                    if hookee["url"] is None or browser.GetUrl() == LocalizeURL(hookee["url"]):
                        js.SetProperty(hookee["name"], hookee["value"])
                elif hookee["type"] == "FunctionHookee":
                    # Bind Python Function to JS
                    if hookee["url"] is None or browser.GetUrl() == LocalizeURL(hookee["url"]):
                        js.SetFunction(hookee["name"], hookee["function"])
                elif hookee["type"] == "CodeHookee":
                    # Python execute JS Code (immediately)
                    if hookee["url"] is None or browser.GetUrl() == LocalizeURL(hookee["url"]):
                        browser.ExecuteJavascript(hookee["jsCode"])

            # Finish JS Binding Task
            browser.SetJavascriptBindings(js)


#
# The Browser Class
#

# You have to notice that you can't create multiple browser instances
# Due to the share of Communicator class's static property 'hookees'.
# If I want to solve this problem, I may use metaclass to produce multiple Communicator classes.
# But I don't think it is necessary as long as the Browser class is depended on single thread

class JackieBrowser:
    url = None
    browser = None

    def __init__(self, url_):
        self.Initialize(url_)
        self.AutoResizeWindow()

    def Initialize(self, url_):
        sys.excepthook = cef.ExceptHook
        EnableHighDPISupport()
        cef.Initialize(settings={}, switches={'disable-gpu': ""})
        self.url = url_
        self.browser = cef.CreateBrowserSync(url=LocalizeURL(self.url))

    @staticmethod
    def AutoResizeWindow():
        screenWidth, screenHeight = GetScreenSize()
        taskbarHeight = GetTaskBarHeight()

        windowWidth = int(screenWidth * 0.97)
        windowHeight = int((screenHeight - taskbarHeight) * 0.97)
        windowLeft, windowTop = GetLeftAndTopUsingWidthAndHeight(windowWidth, windowHeight)

        SetWindowSizeAndPos(windowWidth, windowHeight, windowLeft, windowTop)

    @staticmethod
    def AddHookee(hookee):
        Communicator.hookees.append(hookee)

    def Set(self, url, varName, varValue):
        self.AddHookee(VariableHookee(url, varName, varValue))

    def Add(self, url, func):
        self.AddHookee(FunctionHookee(url, GetFunctionName(func), func))

    def Execute(self, url, code):
        self.AddHookee(CodeHookee(url, code))

    def Run(self):
        self.browser.SetClientHandler(Communicator())
        cef.MessageLoop()
        cef.Shutdown()
