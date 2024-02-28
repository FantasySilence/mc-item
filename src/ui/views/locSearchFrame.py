import time
import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path

PATH = Path(__file__).parent / "images"

from src.modules.loc_check import ItemLocationCheck



class LocSearchFrame(ttk.Frame):

    """
    物品位置信息
    """

    def __init__(self, master, **kwargs):

        # ------ 设置窗口的根容器 ------ #
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        self.storage_type = ttk.StringVar(value="single")
        self.item_name = ttk.StringVar(value="填物品名字, 兄嘚...")
        self.run_log = ttk.StringVar(value="勾八你倒是查呀，不查我显示个der...")


        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        option_text = "找不见物品?快来试试物品寻找吧！"
        self.option_frame = ttk.Labelframe(self, text=option_text, padding=(40,10))
        self.option_frame.pack(fill=BOTH, expand=YES, pady=0)

        # 仓库类型选择UI的建立
        self.create_storage_type_page()

        # 物品名称填写UI的建立
        self.create_name_entry_page()

        # 运行信息显示
        self.create_run_log_page()

    
    def create_storage_type_page(self):

        """
        创建仓库类型选择交互UI
        """

        # ------ 创建仓库类型选择页面容器 ------ #
        type_row = ttk.Frame(self.option_frame)
        type_row.pack(fill=X, expand=YES, pady=20)
        type_lbl = ttk.Label(type_row, text="仓库类型", width=8)
        type_lbl.pack(side=LEFT, padx=(15, 0))

        # 单选按钮，选择后仓库类型将变为单分类"single"
        single_opt = ttk.Radiobutton(
            master=type_row,
            text="单分类全物品",
            value="single",
            variable=self.storage_type
        )
        single_opt.pack(side=LEFT)
        single_opt.invoke()  # 默认选中单分类全物品按钮

        # 单选按钮，选择后仓库类型将变为多分类"multi"
        multi_opt = ttk.Radiobutton(
            master=type_row,
            text="多分类全物品",
            value="multi",
            variable=self.storage_type,
        )
        multi_opt.pack(side=LEFT, padx=15)


    def create_name_entry_page(self):

        """
        创建物品名称填写UI
        """

        # ------ 创建物品名称填写页面容器 ------ #
        name_entry_frame = ttk.Frame(self.option_frame)
        name_entry_frame.pack(fill=X, expand=YES)

        name_entry_label = ttk.Label(
            master=name_entry_frame,
            text="待查找的物品:",
            width=12
        )
        name_entry_label.pack(side=LEFT, padx=(15, 0))

        # 物品名输入框
        name_entry = ttk.Entry(
            master=name_entry_frame,
            textvariable=self.item_name
        )
        name_entry.pack(side=LEFT, fill=X, expand=YES, padx=5)

        # 确认按钮
        confirm_button = ttk.Button(
            master=name_entry_frame,
            command=self.functionForConfirm,
            text="确认",
            bootstyle = (PRIMARY, OUTLINE),
            width=6
        )
        confirm_button.pack(side=RIGHT, padx=5)


    def create_run_log_page(self):

        """
        创建显示运行日志(结果)的文本框
        """

        # ------ 创建运行日志页面容器 ------ #
        log_row = ttk.Frame(self.option_frame)
        log_row.pack(fill=X, expand=YES, pady=20)

        # 显示运行信息的文本框
        log_text = ttk.Label(
            master=log_row,
            textvariable=self.run_log,
        )
        log_text.pack(fill=X, expand=YES)


    def functionForConfirm(self):

        """
        创建物品填写交互UI时为按钮配置功能
        """

        t = threading.Thread(target=self._updateLog)
        t.start()
        

    def _updateLog(self):

        """
        实现运行信息的更新
        """

        storage_type_dict = {
            "single": "单分类全物品",
            "multi": "多分类全物品",
        }
        self.run_log.set("运行中...\n你的仓库类型为：{}\n你查询的物品为：{}"\
                        .format(storage_type_dict[self.storage_type.get()], 
                                self.item_name.get()))
        ItemLocationCheck(
            self.item_name.get(),
            self.storage_type.get(),
            self.run_log
        ).Check()
        self.item_name.set("")
