import ttkbootstrap as ttk
from ttkbootstrap.constants import *



class AboutFrame(ttk.Frame):

    """
    关于信息页面
    """

    def __init__(self, master=None, **kwargs):

        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        ttk.Label(
            master=self,
            text="Author: @御河DE天街, Bilibili: @御河DE天街FS",
        ).pack(pady=3)

        ttk.Label(
            master=self,
            text="Github: https://github.com/FantasySilence/mc-item"
        ).pack(pady=3)

        ttk.Label(
            master=self,
            text="   Credits:\n\
        感谢刘老师(Bilibili: @WIFI连接超时)给我画出的大饼，不然我也不会改进(doge)\n\
        感谢Alan在样式选择以及UI布局等方面提出的宝贵建议"
        ).pack(pady=3)

        ttk.Label(
            master=self,
            text="Description:\n\
        这是一个MC物品小帮手, 可以帮助你整理投影材料列表，便于准备物资\n\
        如果在全物品迷路，你也可以使用它查询你想要的物品所在的位置\n\
        当仓库中物品发生变动时，你也可以相应地进行更新，以匹配仓库发生的变动"
        ).pack(pady=10)

        ttk.Label(self, text="Copyrights@LSP_Hub, All Rights Reserved.").pack()
        