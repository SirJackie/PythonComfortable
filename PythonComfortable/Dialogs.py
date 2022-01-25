import easygui


def MessageBox(title, content):
    easygui.msgbox(content, title)


def ChoiceBox(title, content, choiceList):
    return easygui.choicebox(content, title, choiceList)
