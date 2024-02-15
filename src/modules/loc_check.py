import time
import pandas as pd
from tkinter import *

from src.common.files_io import FilesIO
from src.common.const import idx_menu_single, idx_menu_multi



class ItemLocationCheck:

    """
    查询某物品在全物品的对应位置，便于搜索
    """

    def __init__(self, item_name:str, storage_type:str, run_log:StringVar):
        
        """
        参数初始化
        item_name：待查询的物品名称
        storage_type：仓库类型，单分类全物品(single)&多分类全物品(multi)
        item_location：物品所在位置
        item_type：物品所属类别
        run_log：运行日志，用于显示运行状态，例如：运行中，运行完成，运行错误等。
        """

        self.item_name = item_name
        self.storage_type = storage_type
        self.run_log = run_log
        self.item_box_location = None
        self.item_chest_location = None
        self.item_type = None
    

    def Check(self):

        """
        查询位置
        """

        start_time = time.time()
        self.run_log.set("正在检索...")

        # ------读取数据库以及索引目录------ #
        if self.storage_type.lower() == "single":
            data_base = pd.read_excel(FilesIO.getSingleDB())
            idx_menu = idx_menu_single
            flag = True
        elif self.storage_type.lower() == "multi":
            data_base = pd.read_excel(FilesIO.getMultiDB())
            idx_menu = idx_menu_multi
            flag = True
        else:
            flag = False
            self.run_log.set("仓库类型错误！\n仅支持单分类全物品(single),\n多分类全物品(multi)")
        
        if flag:

            # ------从数据库中提取数据，存入字典------ #
            data_base_dict = {
                item:[item_type, chest_loc, box_loc]
                for item, item_type, chest_loc, box_loc in zip(data_base['物品ID'], data_base['分类'], 
                                                               data_base['物品位置'], data_base['盒子位置'])
            }
            
            # ------查询物品所在位置------ #
            if self.item_name in data_base_dict.keys():
                
                # 该物品所属的分类
                self.item_type = idx_menu[data_base_dict[self.item_name][0]]
                # 装有该物品的箱子的位置信息
                self.item_chest_location = data_base_dict[self.item_name][1]
                # 装有该物品的盒子的箱子的位置信息
                self.item_box_location = data_base_dict[self.item_name][2]

                end_time = time.time()
                self.run_log.set("检索完成！耗时%.3fms,\n物品%s属于%s类,\n物品位于%s,盒子位于%s"%\
                            ((end_time-start_time)*1000, self.item_name, 
                            self.item_type, self.item_chest_location, self.item_box_location))
                
            else:
                self.run_log.set("未找到！请输入物品名称的标准译名")
    

        




        