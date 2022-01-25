from easygui import choicebox


def ChoiceBox(title, content, choiceList):

    selected = choicebox(
        content,
        title,
        choiceList
    )

    return selected
