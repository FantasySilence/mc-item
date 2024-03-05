import os
import sys

# 全局路径别名
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.append(src_path)


from src.ui.mainWindow import MainWindow

# 主程序入口
MainWindow.show()
