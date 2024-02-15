import time
import pandas as pd
from tkinter import *

from src.common.files_io import FilesIO
from src.common.excelFormater import Formater
from src.common.const import idx_menu_single, idx_menu_multi



class MaterialsOrg:

    """
    使用投影获取材料列表之后对其进行整理，在全物品中拣货更便捷
    """

    def __init__(self, material_data:str, storage_type:str, run_log:StringVar):

        """
        参数初始化
        material_data：投影材料列表路径
        storage_type：仓库类型，单分类全物品(single)&多分类全物品(multi)
        run_log：运行日志，用于显示运行状态，例如：运行中，运行完成，运行错误等。
        """

        self.material_data = material_data
        self.storage_type = storage_type
        self.tempres = FilesIO.getRootDir() + "temp.xlsx"
        self.run_log = run_log
    

    def Organize(self):

        """
        整理材料
        """

        start_time = time.time()

        # ------读取数据库,材料列表以及索引目录------ #
        material_data = pd.read_csv(self.material_data, encoding="gbk").iloc[:,:2]

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
            data_base_dict = {label:[] for label in idx_menu.keys()}
            for i in idx_menu.keys():
                data_base_dict[i].extend(data_base[data_base['分类'] == i]["物品ID"].tolist())


            # ------对材料列表进行整理------ #
            with pd.ExcelWriter(self.tempres) as writer:
                for i in idx_menu.keys():
                    label_i = {
                        name:[amount, "%d × 64 + %d"%(amount//64,amount-(amount//64)*64), "%.2f"%(amount/1728)] 
                        for name,amount in zip(material_data['Item'],material_data['Total'])
                        if name in data_base_dict[i]
                        }
                    df_i = pd.DataFrame(label_i, index=['数量','组数','盒数'])
                    df_i.T.to_excel(writer, sheet_name=idx_menu[i])

            
            # ------调整格式------ #
            Formater.doFormat(self.tempres)
            end_time = time.time()
            self.run_log.set("材料整理完成！用时%.3fms"%((end_time-start_time)*1000))

            FilesIO.saveFile(self.tempres)
