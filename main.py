from Classes.Digits import Digits
from Classes.IO import IO
from Classes.MessageBox import MessageBox

print(Digits.ToNDigitsString(532, 5))
print(IO.ListDir([".", "Classes"]))
MessageBox.SynchronousPopUpOKBox("Title", "Content")
