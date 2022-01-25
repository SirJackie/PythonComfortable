from PythonComfortable.Digits import Digits
from PythonComfortable.Files import Files
from PythonComfortable.Dialogs import MessageBox, ChoiceBox
from PythonComfortable.JackieBrowser import *

print(Digits.ToNDigitsString(532, 5))
print(Files.ListDir([".", "PythonComfortable"]))
MessageBox("标题", "内容")
print(ChoiceBox("标题", "请选择：", ["a", "b", "c"]))

pythonVariable = "A String From Python"


def PythonFunction():
    print("Python received a call from JS")


browser = JackieBrowser("./HTMLSourceCodes/index.html")
browser.Set(None, "pythonVariable", pythonVariable)
browser.Add("./HTMLSourceCodes/index.html", PythonFunction)
browser.Execute("https://www.baidu.com/", "alert(\"JS received a call from Python when accessing Baidu.\");")
browser.Run()

