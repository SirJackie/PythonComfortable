import tkinter as tk
import tkinter.messagebox as messagebox


class MessageBox:
    root = None

    @staticmethod
    def SynchronousOKBox(title, content):

        # Make sure tkinter root window won't come out when using messagebox
        if MessageBox.root is None:
            MessageBox.root = tk.Tk()
            MessageBox.root.withdraw()

        # Create a messagebox, function will end after it closes
        isClicked = False
        while not isClicked:
            isClicked = messagebox.showinfo(
                title,
                content
            )

    @staticmethod
    def SynchronousPopUpOKBox(title, content):

        # Initialize
        if MessageBox.root is None:
            MessageBox.root = tk.Tk()

        # Make sure tkinter root window WILL come out when using messagebox
        if MessageBox.root is not None:
            MessageBox.root.wm_deiconify()

        # Create a messagebox, function will end after it closes
        isClicked = False
        while not isClicked:
            isClicked = messagebox.showinfo(
                title,
                content
            )

        MessageBox.root.withdraw()


if __name__ == "__main__":
    MessageBox.SynchronousOKBox("Title", "Content")
