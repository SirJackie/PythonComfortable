from PythonComfortable.Digits import Digits
from PythonComfortable.Files import Files
from PythonComfortable.Dialogs import MessageBox, ChoiceBox

print(Digits.ToNDigitsString(532, 5))
print(Files.ListDir([".", "PythonComfortable"]))
MessageBox("标题", "内容")
print(ChoiceBox("标题", "请选择：", ["a", "b", "c"]))
