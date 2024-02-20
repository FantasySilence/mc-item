from tkinter import *

from src.ui.views.organizeFrame import OrganizeFrame
from src.ui.views.locSearchFrame import LocSearchFrame
from src.ui.views.crudFrame import CrudFrame
from src.ui.views.aboutFrame import AboutFrame




class Window:

    """
    实现主要功能的页面
    """

    def __init__(self):
        
        # ------创建主窗口------ #
        self.root = Tk()
        self.root.title("MC物品小帮手")
        self.root.geometry("800x500")
        self.create_page()
    

    def create_page(self):

        # ------投影材料列表整理页面------ #
        self.organizeFrame = OrganizeFrame(self.root)

        # ------查询物品在全物品的位置页面------ #
        self.locsearchFrame = LocSearchFrame(self.root)

        # ------增删改查物品信息页面------ #
        self.crudFrame = CrudFrame(self.root)
        
        # ------关于页面------ #
        self.aboutFrame = AboutFrame(self.root)

        # ------默认显示投影材料列表整理页面，不需要显示其他页面------ #
        self.updateViews(self.organizeFrame)

        
        # ------设置菜单选项------ #
        menubar = Menu(self.root)
        menubar.add_command(label="投影材料列表整理", 
                            command=lambda: self.updateViews(self.organizeFrame))
        menubar.add_command(label="查询物品在全物品的位置", 
                            command=lambda: self.updateViews(self.locsearchFrame))
        menubar.add_command(label="增删改查物品信息", 
                            command=lambda: self.updateViews(self.crudFrame))
        menubar.add_command(label="关于", 
                            command=lambda: self.updateViews(self.aboutFrame))
        self.root["menu"] = menubar
    
    
    def updateViews(self, view: Frame):

        self.organizeFrame.pack_forget()
        self.locsearchFrame.pack_forget()
        self.crudFrame.pack_forget()
        self.aboutFrame.pack_forget()
        view.pack()


    # ------ 显示主窗口 ------ #
    def show(self):
        self.root.mainloop()
        
