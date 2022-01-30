from PythonComfortable.Files import Files

Files.Write(["Temp", "nhzg utf-8.txt"], "你好，中国！", "utf-8")
print(Files.Read(["Temp", "nhzg utf-8.txt"], "utf-8"))

Files.Write(["Temp", "nhzg gb2312.txt"], "你好，中国！", "gb2312")
print(Files.Read(["Temp", "nhzg gb2312.txt"], "gb2312"))

Files.Write(["Temp", "nhzg gbk.txt"], "你好，中国！", "gbk")
print(Files.Read(["Temp", "nhzg gbk.txt"], "gbk"))
