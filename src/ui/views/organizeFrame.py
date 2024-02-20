from tkinter import *
from tkinter import messagebox

from src.modules.material_organize import MaterialsOrg
from src.common.files_io import FilesIO

class OrganizeFrame(Frame):

    def __init__(self, root):

        super().__init__(root)
        self.page = Frame()
        self.var = StringVar()
        self.run_log = StringVar()
        self.run_log.set(" ")
        self.page.pack()
        self.create_page()
    

    def create_page(self):

        # ------标题栏------ #
        Label(self, text="投影材料列表整理").grid(row=0, column=0, sticky=W)
        Label(self, text="选择你的仓库类型：", font=("微软雅黑", 15)).grid(row=1, column=0, pady=10)

        # ------两个单选按钮，self.var获取选项------ #
        Radiobutton(self, text="单分类全物品(single)", variable=self.var,  font=("微软雅黑", 15),
                    value="single").grid(row=2, column=0, pady=10)
        Radiobutton(self, text="多分类全物品(multi)", variable=self.var,  font=("微软雅黑", 15),
                    value="multi").grid(row=2, column=1, pady=10)
        
        # ------标题栏------ #
        Label(self).grid(row=3, column=0)
        Label(self, text="选择投影生成的材料列表文件：", font=("微软雅黑", 15)).grid(row=4, column=0, pady=10)

        # ------获取文件路径------ #
        Button(self, text="选择文件", font=("微软雅黑", 15), 
               command=self.button_function1).grid(row=5, column=0, pady=10)

        # ------显示运行日志------ #
        Label(self).grid(row=6, column=0)
        Label(self, textvariable=self.run_log, font=("微软雅黑", 15)).grid(row=7, column=0)

        # ------退出按钮------ #
        Button(self, text="退出", font=("微软雅黑", 15), command=self.quit).grid(row=7, column=1)
        

    def button_function1(self):

        """
        绑定"确定"按钮
        """   

        material_path: str = FilesIO.getSelectFile()
        storage_type = self.var.get()

        if storage_type == "":
            messagebox.showerror("错误", "请选择仓库类型")
            return
        
        else:
            MaterialsOrg(material_path, storage_type, self.run_log).Organize()