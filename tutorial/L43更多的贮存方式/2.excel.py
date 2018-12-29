# excel读写
# excel是一种广泛流传的办公文件格式，表格形式，比csv复杂一些，带一些功能样式，适合普通用户观看。由于带功能样式，所以需要专门的包负责解析。excel的后缀 老格式.xls 新格式.xlsx，新格式兼容老格式。
# 操作excel包选择  XlsxWriter Xlrd pyexcel  , start数、维护时间都较好，大同小异，下面以pyexcel讲解。
# pip install  pyexcel_xls  pyexcel_xlsx  pyexcel
from pyexcel_io import save_data
from pyexcel_io import get_data

data=get_data('2readfile.xlsx')
print(type(data))
sheet1=data['Sheet1']
print(sheet1)
for index,row in enumerate(sheet1):
    if index<= 0:
        continue
    print(f'这是第{index}个学生，名字是{row[1]}')
# 报错
# 1. 不支持格式，请安装插件pyexcel-xlsx
# 2. 没有权限，管理员powershell中运行脚本

