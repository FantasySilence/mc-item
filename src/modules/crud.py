import time
import pandas as pd
from tkinter import *

from src.common.const import idx_menu_single, idx_menu_multi



class ItemAddDeleteCheckModify:

    """
    实现物品数据库的增删查改
    """

    def __init__(self, item_dict:dict, storage_type:str, execution:str, run_log:StringVar):

        """
        item_dict：待操作的物品，传入字典({xxx:[xx, xx, xx], yyy:[yy, yy, yy]......})
        storage_type：仓库类型，单分类全物品(single)&多分类全物品(multi)
        execution：执行的操作(add/delete/check/modify)
        run_log：运行日志，用于显示运行状态，例如：运行中，运行完成，运行错误等
        """

        self.item_dict = item_dict
        self.storage_type = storage_type
        self.execution = execution
        self.run_log = run_log
        self.item_attribute = None
    

    def execute(self):

        """
        执行操作
        """

    

    def __add__(self):

        """
        增加物品
        """
    

    def __delete__(self):

        """
        删除物品
        """
    

    def __check__(self):

        """
        查询物品
        """
    

    def __modify__(self):

        """
        修改物品
        """