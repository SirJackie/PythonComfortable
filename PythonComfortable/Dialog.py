from easygui import choicebox
import ctypes


def MessageBox(title, content):
    ctypes.windll.user32.MessageBoxW(0, content, title, 0)


def ChoiceBox(title, content, choiceList):
    return choicebox(content, title, choiceList)
