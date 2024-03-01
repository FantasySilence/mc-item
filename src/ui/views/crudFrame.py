import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.modules.crud import ItemAddDeleteCheckModify


class CrudFrame(ttk.Frame):

    """
    信息修改页面
    """

    def __init__(self, master=None, **kwargs):
        
        # ------ 设置窗口的根容器 ------ #
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        self.storage_type = ttk.StringVar(value="single")
        self.run_log = ttk.StringVar(value="6,全是null我拿命改是吧...")
        self.item_name = ttk.StringVar(value="开发ing...")
        self.item_class = ttk.StringVar(value="开发ing...")
        self.item_loc = ttk.StringVar(value="开发ing...")
        self.box_loc = ttk.StringVar(value="开发ing...")

        # ------ 设置标签页面容器，存放交互逻辑 ------ #
        option_text = "信息有误！！！快改！！！"
        self.option_frame = ttk.Labelframe(self, text=option_text, padding=(40,10))
        self.option_frame.pack(fill=BOTH, expand=YES, pady=0)

        # 仓库类型选择UI的建立
        self.create_storage_type_page()

        # 物品信息输入UI的建立
        self.create_input_page()

        # 运行信息显示
        self.create_run_log_page()

    
    def create_input_page(self):

        """
        创建物品信息输入交互UI
        """

        # ------- 创建物品信息输入页面容器 ------ #
        input_row = ttk.Frame(self.option_frame)
        input_row.pack(fill=X, pady=(10, 0))

        # 物品名称输入框
        name_lbl = ttk.Label(input_row, text="物品名称:", width=8)
        name_lbl.grid(row=0, column=0)
        self.name_entry = ttk.Entry(
             master=input_row,
             textvariable=self.item_name,
             width=8
        )
        self.name_entry.grid(row=0, column=1, padx=(0, 10))

        # 物品分类输入框
        num_lbl = ttk.Label(input_row, text="物品分类:", width=8)
        num_lbl.grid(row=0, column=2, padx=(10, 0))
        self.num_entry = ttk.Entry(
             master=input_row,
             textvariable=self.item_class,
             width=8
        )
        self.num_entry.grid(row=0, column=3, padx=(0, 10))

        # 物品位置输入框
        location_lbl = ttk.Label(input_row, text="物品位置:", width=8)
        location_lbl.grid(row=1, column=0, pady=(10, 0))
        self.location_entry = ttk.Entry(
             master=input_row,
             textvariable=self.item_loc,
             width=8
        )
        self.location_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 0))

        # 盒子位置输入框
        box_lbl = ttk.Label(input_row, text="盒子位置:", width=8)
        box_lbl.grid(row=1, column=2, padx=(10, 0), pady=(10, 0))
        self.box_entry = ttk.Entry(
             master=input_row,
             textvariable=self.box_loc,
             width=8,
        )
        self.box_entry.grid(row=1, column=3, padx=(0, 10), pady=(10, 0))

        # 修改按钮
        modify_button = ttk.Button(
            master=input_row,
            text="修改",
            bootstyle = (PRIMARY, OUTLINE),
            width=6
        )
        modify_button.grid(row=1, column=4, pady=(10, 0))

        # 查询按钮
        query_button = ttk.Button(
            master=input_row,
            text="查询",
            command=self.functionForQuiry,
            bootstyle = (PRIMARY, OUTLINE),
            width=6
        )
        query_button.grid(row=0, column=4)
    

    def create_storage_type_page(self):

        """
        创建仓库类型选择交互UI
        """

        # ------ 创建仓库类型选择页面容器 ------ #
        type_row = ttk.Frame(self.option_frame)
        type_row.pack(fill=X, expand=YES, pady=8)
        type_lbl = ttk.Label(type_row, text="仓库类型", width=8)
        type_lbl.pack(side=LEFT)

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


    def create_run_log_page(self):

            """
            创建显示运行日志(结果)的文本框
            """

            # ------ 创建运行日志页面容器 ------ #
            log_row = ttk.Frame(self.option_frame)
            log_row.pack(fill=X, expand=YES, pady=8)

            # 显示运行信息的文本框
            log_text = ttk.Label(
                master=log_row,
                textvariable=self.run_log,
            )
            log_text.pack(fill=X, expand=YES)
    

    def functionForQuiry(self):
         
        """
        查询按钮的功能配置
        """

        item_attr = ["self.item_class", "self.item_loc", "self.box_loc"]
        for i in range(len(item_attr)):
            exec(f"{item_attr[i]}.set('')")
        if self.item_name.get() == "":
            self.run_log.set("物品名称不能为空！！！")
            return
        attr_list = ItemAddDeleteCheckModify(
             item_name=self.item_name.get(),
             storage_type=self.storage_type.get(),
             run_log=self.run_log
        ).quiry()
        for i in range(len(attr_list)):
             exec(f"{item_attr[i]}.set(attr_list[i])")
        self.run_log.set("查询成功")
        