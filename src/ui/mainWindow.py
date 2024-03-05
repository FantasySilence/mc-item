import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.ui.views.organizeFrame import OrganizeFrame
from src.ui.views.locSearchFrame import LocSearchFrame
from src.ui.views.crudFrame import CrudFrame
from src.ui.views.aboutFrame import AboutFrame

uiPATH = os.path.dirname(os.path.abspath(__file__))
rootPATH = os.path.dirname(os.path.dirname(uiPATH))
PATH = os.path.join(rootPATH, 'resources\\images')


class MainWindow(ttk.Frame):

    """
    加载主窗口
    """

    def __init__(self, master):
        
        # ------ 创建主页面窗口的根容器 ------ #
        super().__init__(master)
        self.pack(fill=BOTH, expand=YES)
        self.create_page()

    
    def create_page(self):

        """
        创建画面
        """

        # ------ 加载图片 ------ #
        self.images = [
            ttk.PhotoImage(name="logo", 
                           file=PATH  + "/logo.png"),
        ]

        # ------ 创建窗口标题的容器 ------ #
        hdr_frame = ttk.Frame(self, padding=20, bootstyle=SECONDARY)
        hdr_frame.pack(fill=BOTH, expand=YES)

        # 向标题子容器中放入一幅logo图片
        hdr_label = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE, SECONDARY)
        )
        hdr_label.pack(side=LEFT)

        # 向标题子容器中添加标题文字
        logo_text = ttk.Label(
            master=hdr_frame,
            text='LSP物品管理系统',
            font=('TkDefaultFixed', 30),
            bootstyle=(INVERSE, SECONDARY)
        )
        logo_text.pack(side=LEFT, padx=8)


        # ------- 创建多选页面按钮容器 ------- #
        notebook = ttk.Notebook(self, padding=(20, 0), bootstyle=INFO)
        notebook.pack(fill=BOTH, expand=YES)

        # 添加材料列表整理页面
        organizeFrame = OrganizeFrame(notebook, padding=20)
        notebook.add(organizeFrame, text='文件处理')

        # 添加信息查询页面
        locsearchFrame = LocSearchFrame(notebook, padding=20)
        notebook.add(locsearchFrame, text='信息查询')

        # 添加信息修改页面
        crudFrame = CrudFrame(notebook, padding=20)
        notebook.add(crudFrame, text='信息修改')

        # 添加关于界面
        aboutFrame = AboutFrame(notebook)
        notebook.add(aboutFrame, text='关于')
    

    @staticmethod
    def _show():

        root = ttk.Window(title="v0.1.7")
        MainWindow(root)
        root.mainloop()
    

    @classmethod
    def show(cls):
        MainWindow._show()