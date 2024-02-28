import threading
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from pathlib import Path
from tkinter.filedialog import askopenfilename

from src.modules.material_organize import MaterialsOrg

PATH = Path(__file__).parent / "images"


class OrganizeFrame(ttk.Frame):

    """
    材料列表整理界面
    """

    def __init__(self, master, **kwargs):

        # ------ 设置窗口的根容器 ------ #
        super().__init__(master, **kwargs)
        # 桌面路径
        _desktop = Path.home() / "Desktop"
        self.pack(fill=BOTH, expand=YES)
        self.storage_type = ttk.StringVar(value="single")
        self.path_var = ttk.StringVar(value=_desktop)
        self.run_log = ttk.StringVar(value="你不填材料列表我显示个der...")

        
        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        option_text = "填写下面的项目开始让你的材料列表变得好用吧！"
        self.option_frame = ttk.Labelframe(self, text=option_text, padding=(40,10))
        self.option_frame.pack(fill=BOTH, expand=YES, pady=0)

        # 文件选择UI的建立
        self.create_file_select_page()

        # 仓库类型选择UI的建立
        self.create_storage_type_page()

        # 运行信息显示
        self.create_run_log_page()
    

    def create_file_select_page(self):

        """
        创建文件选择交互UI
        """

        # ------- 创建文件选择页面容器 ------ #
        path_row = ttk.Frame(self.option_frame)
        path_row.pack(fill=X, expand=YES) 

        path_lbl = ttk.Label(path_row, text="选择文件：", width=8)
        path_lbl.pack(side=LEFT, padx=(15, 0))

        # 路径输入框
        path_ent = ttk.Entry(path_row, textvariable=self.path_var)
        path_ent.pack(side=LEFT, fill=X, expand=YES, padx=5)

        # 文件搜索按钮
        browse_button = ttk.Button(
            master=path_row,
            text="打开",
            command=self.functionForBrowse,
            bootstyle = (PRIMARY, OUTLINE),
            width=6
        )
        browse_button.pack(side=RIGHT, padx=5)
    

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

        # 确认按钮，点击后运行整理材料列表功能，并显示运行日志(结果)
        confirm_button = ttk.Button(
            master=type_row,
            text="确认",
            command=self.functionForConfirm,  
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


    def functionForBrowse(self):

        """
        创建文件选择交互UI时为按钮配置功能
        """

        path = askopenfilename(title="请选择你的材料列表")
        if path:
            self.path_var.set(path)
    

    def functionForConfirm(self):

        """
        创建仓库类型选择交互UI时为按钮配置功能
        """

        t = threading.Thread(target=self._updateLog)
        t.start()
        

    def _updateLog(self):

        """
        实现运行信息的更新
        """

        file_path = self.path_var.get()
        file_name = Path(file_path).name
        storage_type_dict = {
            "single": "单分类全物品",
            "multi": "多分类全物品",
        }
        self.run_log.set("运行中...\n你的仓库类型为：{}\n你的材料列表文件为：{}"\
                    .format(storage_type_dict[self.storage_type.get()], file_name))
        MaterialsOrg(file_path, self.storage_type.get(), self.run_log).Organize()
