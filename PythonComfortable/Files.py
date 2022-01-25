import re
import os
import shutil


class Files:
    @staticmethod
    # File Path List 2 File Path String
    def fpl2fp(filePathList):
        return os.path.join(*filePathList)

    @staticmethod
    # File Name List 2 File Name String
    def fnl2fn(fileNameList):
        return os.path.join(*fileNameList)

    @staticmethod
    # File Name List 2 File Path String
    def fnl2fp(fileNameList):
        return os.path.join(*(fileNameList[:-1]))

    @staticmethod
    # File Name List 2 File Path List
    def fnl2fpl(fileNameList):
        return fileNameList[:-1]

    @staticmethod
    def TryCreateFolder(filePathList):
        try:
            filePath = Files.fpl2fp(filePathList)
            os.mkdir(filePath)
        except FileNotFoundError:
            # Create the father folder first
            Files.TryCreateFolder(filePathList[:-1])
            Files.TryCreateFolder(filePathList)
        except FileExistsError:
            pass
        else:
            pass

    @staticmethod
    def Write(fileNameList, content):
        # Try to Create a Folder
        filePathList = Files.fnl2fpl(fileNameList)
        Files.TryCreateFolder(filePathList)

        # Write File
        fileName = Files.fnl2fn(fileNameList)
        with open(fileName, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def WriteBinary(fileNameList, content):
        # Try to Create a Folder
        filePathList = Files.fnl2fpl(fileNameList)
        Files.TryCreateFolder(filePathList)

        # Write File
        fileName = Files.fnl2fn(fileNameList)
        with open(fileName, "wb") as f:
            f.write(content)

    @staticmethod
    def Read(fileNameList):
        fileName = Files.fnl2fn(fileNameList)
        content = ""
        with open(fileName, "r", encoding="utf-8") as f:
            content = f.read()
        return content

    @staticmethod
    def ReadBinary(fileNameList):
        fileName = Files.fnl2fn(fileNameList)
        content = ""
        with open(fileName, "rb") as f:
            content = f.read()
        return content

    @staticmethod
    def ReadLatin1(fileNameList):
        fileName = Files.fnl2fn(fileNameList)
        content = ""
        with open(fileName, "r", encoding="latin-1") as f:
            content = f.read()
        return content

    @staticmethod
    def Escape(title):
        # Replace all the illegal characters into underscore
        rStr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        new_title = re.sub(rStr, "_", title)
        return new_title

    @staticmethod
    def Exist(fileNameList):
        fileName = Files.fnl2fn(fileNameList)
        return os.path.exists(fileName)

    @staticmethod
    def Rename(fileNameList, newFileNameList):
        os.rename(
            Files.fnl2fn(fileNameList),
            Files.fnl2fn(newFileNameList)
        )

    @staticmethod
    def ListDir(filePathList):
        return os.listdir(Files.fpl2fp(filePathList))

    @staticmethod
    def GetCWD():
        return os.getcwd()

    @staticmethod
    def Delete(fileNameList):
        os.remove(Files.fnl2fn(fileNameList))

    @staticmethod
    def DeleteFolder(filePathList):
        shutil.rmtree(Files.fpl2fp(filePathList))

    @staticmethod
    def CheckMP3Playable(fileNameList):
        fileName = Files.fnl2fn(fileNameList)

        # 读取文件内字符串
        head_3_str = None
        with open(fileName, "r", encoding="latin-1") as f:
            file_str = f.read()
            head_3_str = file_str[:3]

        # 判断开头是不是ID3
        if head_3_str == "ID3":
            return True

        # 判断结尾有没有TAG
        last_32_str = file_str[-32:]
        if last_32_str[:3] == "TAG":
            return True

        # 判断第一帧是不是FFF开头, 转成数字
        # 应该循环遍历每个帧头，这样才能100%判断是不是mp3
        first_char = ord(file_str[:1])
        if first_char == 255:
            return True
        return False

    @staticmethod
    def CheckImageType(fileNameList):
        fileContent = Files.ReadLatin1(fileNameList)

        # Read Headed Chars
        head3Chars = fileContent[:3]
        head4Chars = fileContent[:4]

        # Define Known Headed Chars
        jpgHead = chr(int("0xff", 16)) + chr(int("0xd8", 16)) + chr(int("0xff", 16))
        pngHead = chr(int("0x89", 16)) + chr(int("0x50", 16)) + chr(int("0x4e", 16)) + chr(int("0x47", 16))

        if head3Chars == jpgHead:
            return "JPG"
        elif head4Chars == pngHead:
            return "PNG"
        else:
            return "Unknown"

    @staticmethod
    def Copy(src, dst):
        # Try Create Folder is already included in Files.WriteBinary().
        Files.WriteBinary(dst, Files.ReadBinary(src))

    @staticmethod
    def CopyWithShutil(src, dst):
        Files.TryCreateFolder(Files.fnl2fpl(dst))              # Try Create Folder
        shutil.copyfile(Files.fnl2fn(src), Files.fnl2fn(dst))  # Write File
