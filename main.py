from PythonComfortable.Digits import Digits
from PythonComfortable.IO import IO
from PythonComfortable.Dialog import MessageBox, ChoiceBox

print(Digits.ToNDigitsString(532, 5))
print(IO.ListDir([".", "PythonComfortable"]))
MessageBox("标题", "内容")
print(ChoiceBox("标题", "请选择：", ["a", "b", "c"]))
