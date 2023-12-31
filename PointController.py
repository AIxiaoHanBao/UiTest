import math
import pandas as pd
import UntilConfig as uConfig
import  MdbController as mdbConfig
import  Populate as popConfig
import Handling as handConfig

#加工数据
def integrateData(excl_cloum,data,result_list):
    #获取特殊字段
    splic_list = uConfig.special_fields.copy()
    repeating_list = uConfig.repeating_fields.copy()
    populate_list_data = uConfig.populate_fields.copy()

    for i in excl_cloum:
        print(i)
        if  i in splic_list:
            # 优先处理特殊字段
            splic_list_data = handConfig.process_fields(i, data[i].values.tolist())
            # 处理完成就删除这个字段避免重复处理出现问题
            splic_list.pop(splic_list.index(i))
            # 加入到里面

            for j in range(len(result_list)):
                if splic_list_data[j] is None:
                    result_list[j].extend([None])
                    continue
                result_list[j].extend(splic_list_data[j])

            continue
        #自增字段的处理
        elif i in populate_list_data:
            #如果自增字段中存在重复的获取其中一列即可
            if False in data[i].duplicated():
                populate_list = popConfig.populateCloum(data.iloc[:, 0].tolist())
            else:
                populate_list = popConfig.populateCloum(data[i].tolist())

            for j in range(len(result_list)):
                value = populate_list[j]
                result_list[j].extend([value])
            populate_list_data.pop(populate_list_data.index(i))
            continue

        # 特殊字段(一般来说特殊字段都是处理了后批量添加(如果后续有处理完单独加入后续防范方法写一下
        elif i in repeating_list:
            repeating_list_data = data[i].values.tolist()

            for j in range(len(result_list)):

                result_list[j].extend(repeating_list_data[j])
            repeating_list.pop(repeating_list.index(i))
            continue
        # 默认处理的字段就是这样,不存于 特殊 和 自增字段
        # (i not in uConfig.special_fields) and (i not in uConfig.populate_fields)
        elif ((i not in uConfig.special_fields) and (i not in uConfig.populate_fields) and (i not in uConfig.repeating_fields)):
            for j in range(len(result_list)):
                value = data[i].values.tolist()[j]
                result_list[j].extend([value])
    return  result_list



def initData(sheet_name,path):
    mdbConfig.del_table(sheet_name)
    uConfig.now_sheelm = sheet_name

    # 获取文件
    excl_file1 = pd.read_excel(uConfig.excl_path, sheet_name=sheet_name)
    excl_file2 = pd.read_excel(uConfig.excl_path, sheet_name="收点")
    #设置大写
    excl_file2['物探点号'] = excl_file2['物探点号'].str.upper()
    merged_table = excl_file1.merge(excl_file2[['物探点号', '北坐标', '东坐标', '高程']], on='物探点号', how='left')
    # merged_table.to_excel('merged_table.xlsx', index=False)

    # print(merged_table.keys())

    uConfig.now_data_form = merged_table.copy()

    # 获取到这个表格的字典(直接设置好特殊字段和自增字段
    uConfig.getInit(sheet_name,path)
    # 获取mdb对应的字段
    table_cloum = list(uConfig.test_diy.keys())
    # 获取excl对应字段
    excl_cloum = list(uConfig.test_diy.values())
    # print(excl_cloum)
    # 获取到特定列表的数据
    data = merged_table[excl_cloum]
    #初始化result_list
    result_list = [[] for _ in range(len(data[excl_cloum[0]].values.tolist()))]

    #得到处理后的数据
    result_list = integrateData(excl_cloum,data,result_list)

    new_list=[]
    for list_data in result_list:
        new_list.append([None if isinstance(val, float) and math.isnan(val) else val for val in list_data])



    return new_list,table_cloum


def insertData(sheet_name, table_cloum, list):
    msg = mdbConfig.insert_data(sheet_name, table_cloum, list)

def getMsg(sheet_name,table_cloum,new_list):

    msg = mdbConfig.insert_data(sheet_name,table_cloum,new_list)
    return msg



if __name__ == "__main__":
    uConfig.mdb_path=r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\园区模板null.mdb"
    uConfig.excl_path=r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\采集成果.xls"
    uConfig.excl_cloum_path=r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\字段表演示.xlsx"

    new_list, table_cloum = initData("XH_POINT")

    #到时候使用for循环读取到msg来显示
    msg =  getMsg("XH_POINT",table_cloum,new_list[0])