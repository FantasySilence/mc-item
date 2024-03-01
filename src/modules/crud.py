import pandas as pd
import ttkbootstrap as ttk

from src.common.files_io import FilesIO


class ItemAddDeleteCheckModify:

    """
    实现信息修改查询功能
    """

    def __init__(self, item_name: str, storage_type: str, run_log: ttk.StringVar):

        """
        item_name：待操作的物品名称
        storage_type：仓库类型
        run_log：运行日志
        """

        self.item_name = item_name
        self.storage_type = storage_type
        self.run_log = run_log


    def quiry(self):

        """
        查询功能
        """

        # ------ 加载单分类全物品的数据库 ------ #
        if self.storage_type == "single":
            data = pd.read_excel(FilesIO.getSingleDB())
            data = data.values
            data_dict = {
                data[i, 0]:[attr for attr in data[i, 1:]] for i in range(data.shape[0])
            }

        # ------ 加载多分类全物品的数据库 ------ #
        elif self.storage_type == "multi":
            data = pd.read_excel(FilesIO.getMultiDB())
            data = data.values
            data_dict = {
                data[i, 0]:[attr for attr in data[i, 1:]] for i in range(data.shape[0])
            }
        if self.item_name in data_dict.keys():
            return data_dict[self.item_name]
        else:
            self.run_log.set(f"查询失败，物品{self.item_name}不存在！")
            return None
    

    def modify(self, item_class, item_loc, box_loc):

        """
        修改功能
        """

        pass

