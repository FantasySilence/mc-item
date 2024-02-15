from tkinter import *



class CrudFrame(Frame):

    def __init__(self, root):

        super().__init__(root)
        self.page = Frame()
        self.var = StringVar()
        self.item_name = StringVar()
        self.run_log = StringVar()
        self.run_log.set(" ")
        self.page.pack()
        self.create_page()
    

    def create_page(self):

        # ------标题栏------ #
        Label(self, text="增删改查物品信息").grid(row=0, column=0)
        Label(self, text="选择你的仓库类型：", font=("微软雅黑", 15)).grid(row=1, column=0, pady=10, sticky=W)

        # ------两个单选按钮，self.var获取选项------ #
        Radiobutton(self, text="单分类全物品(single)", variable=self.var, font=("微软雅黑", 15),
                    value="single").grid(row=2, column=0, pady=10)
        Radiobutton(self, text="多分类全物品(multi)", variable=self.var, font=("微软雅黑", 15),
                    value="multi").grid(row=2, column=1, pady=10)
    
        
        # ------制作UI------ #
        Label(self, text="物品名称: ", font=("微软雅黑", 15)).grid(row=3, column=0, pady=5)
        Entry(self, textvariable=self.item_name, font=("微软雅黑", 15), background="white").grid(row=3, column=1, pady=5)

        Label(self, text="物品分类: ", font=("微软雅黑", 15)).grid(row=4, column=0, pady=5)
        Entry(self, textvariable=self.item_name, font=("微软雅黑", 15), background="white").grid(row=4, column=1, pady=5)

        Label(self, text="物品位置: ", font=("微软雅黑", 15)).grid(row=5, column=0, pady=5)
        Entry(self, textvariable=self.item_name, font=("微软雅黑", 15), background="white").grid(row=5, column=1, pady=5)

        Label(self, text="盒子位置: ", font=("微软雅黑", 15)).grid(row=6, column=0, pady=5)
        Entry(self, textvariable=self.item_name, font=("微软雅黑", 15), background="white").grid(row=6, column=1, pady=5)
 
        # ------显示运行日志------ #
        Label(self).grid(row=6, column=0, pady=5)
        Label(self, textvariable=self.run_log, font=("微软雅黑", 15)).grid(row=7, column=0, pady=5)

        # ------退出按钮------ #
        Button(self, text="退出", font=("微软雅黑", 15), command=self.quit).grid(row=7, column=1, pady=5)