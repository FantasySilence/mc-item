import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class CrudFrame(ttk.Frame):

    """
    信息修改页面
    """

    def __init__(self, master=None, **kwargs):

        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        ttk.Label(self, text="修改信息", font=("Arial", 20)).pack()
        ttk.Label(self, text="开发中...", font=("Arial", 20)).pack()
        