import pandas as pd
#这里是程序所用到的excl数据表格
excl_path=""

#这里是excl_cloum字段表的路径
excl_cloum_path=""

#这里是mdb文件表的路径
mdb_path = ""

# #对应下面需要填入字段的
# table_list = []

#自增字段(一般是标记为自增但是数据库没有设置自增的
populate_fields=[]

#特殊需要处理的字段（一个字段就需要单独写方法
special_fields=[]

#存放重复字段 % 百分号的
repeating_fields=[]

test_diy={}
#当前表格名称
now_sheelm=""
#当前的dataform
now_data_form=None

#表格需要添加进入的字段
XH_LINE = {
    "MSLINK":"_id",
    "GD_ID":"管线段号",
    "CZ":"管线材质",
    "MSFS":"埋设方式",
    "QDMS":"起点埋深",
    "ZDMS":"终点埋深",
    "GNJ":"管径",
    "GWJ":"管径",
    "GWG":"管径",
    "DY":"电压",
    "DLGS":"线缆条数",
    "ZKS":"总孔数",
    "ZYKS":"已用孔数",
    "QD_ID":"起点点号",
    "ZD_ID":"终点点号"
}

#初始化字典
def getInit(sheet_name,path):
    test_diy.clear()
    populate_fields.clear()
    special_fields.clear()
    repeating_fields.clear()

    excl = pd.read_excel(path,sheet_name=sheet_name)
    excl_list = list(excl)
    print("我是字段")
    print(excl_list)
    column_list=excl.values.tolist()[0]
    print("我是数据")
    print(column_list)
    for i in list(excl):
        #自增字段
        if len(i.split("*"))==2:
            populate_fields.append(i.split("*")[0])
            test_diy[column_list[excl_list.index(i)]] = i.split("*")[0]

            continue
        #特殊字段
        if len(i.split("&"))==2  :
            #避免重复添加
            if (i.split("&")[0] not in special_fields):
                special_fields.append(i.split("&")[0])
            test_diy[column_list[excl_list.index(i)]] = i.split("&")[0]
            continue
        if len(i.split("%"))==2 :
            if i.split("%")[0] not in repeating_fields:
                repeating_fields.append(i.split("%")[0])
            test_diy[column_list[excl_list.index(i)]] = i.split("%")[0]
            continue

        test_diy[column_list[excl_list.index(i)]] =i


if __name__ == "__main__":
    getInit("LD_POINT",r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\字段表演示(13类).xlsx")
    print(populate_fields)
    print(special_fields)
