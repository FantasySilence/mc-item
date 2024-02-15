import os
import tkinter as tk
from tkinter import filedialog


class FilesIO:

    """
    这是一个文件IO流类
    """

    @staticmethod
    def getRootDir():

        """
        获取根路径
        """

        module_path = os.path.dirname(__file__)
        common_path = os.path.abspath(module_path)
        src_path = os.path.dirname(common_path)
        return os.path.dirname(src_path)


    @staticmethod
    def getSelectFile():

        """
        获取选择的文件
        """

        root = tk.Tk()
        root.withdraw()  # 隐藏主窗口

        file_path = filedialog.askopenfilename(title="选择文件")

        if file_path:
            return os.path.abspath(file_path)  # 返回路径
        else:
            return False       # 返回False表示没有选择文件


    @staticmethod
    def saveFile(temp_file_path):

        """
        保存文件
        """

        root = tk.Tk() 
        root.withdraw() # 隐藏主窗口 

        file_path = filedialog.asksaveasfilename(
            initialfile="Materials.xlsx",
            defaultextension=".xlsx", 
            filetypes=[("Excel File", "*.xlsx")], 
            title="保存文件") 
        
        if file_path:
            os.rename(temp_file_path, file_path)
        else:
            os.remove(temp_file_path)
    

    @staticmethod
    def getSingleDB():

        """
        获取单分类全物品数据库地址
        """

        return os.path.join(FilesIO.getRootDir(), 
                            "resources\\data\\DataBase_single.xlsx")


    @staticmethod
    def getMultiDB():

        """
        获取多分类全物品数据库地址
        """

        return os.path.join(FilesIO.getRootDir(), 
                            "resources\\data\\DataBase_multi.xlsx")