import math

from numpy import nan

import UntilConfig as uConfig




def process_fields(name,list):
    #属于管道
    if name=="管径" or name=="井盖尺寸" :
        return gj_list(list)

    if name=="特征" or name == "附属物":
        return tz_list(list)

    if name=="_id":
        return _id_list(list)





#处理 管经 以及 井盖尺寸
def gj_list(gj_list):
    for i in gj_list:
        data_list =(str(i[0]).split("X"))
        #分离开带X
        if len(data_list)>1:
            i[1]=data_list[0]
            i[2]=data_list[1]
            i[0]=None
        else:
            #不带X置为0
            i[1]=None
            i[2]=None
    # print(gj_list)
    return gj_list

def tz_list(tz_list):
    file = pd.read_excel("./中文管点附属物对应字母.xlsx",sheet_name="字段")
    data_dict = file.set_index('地面箱式变压器').to_dict()['XB']
    print("我是当前表222")
    print(uConfig.now_sheelm)
    list_data = []
    for i in tz_list:

        if type(i)!=str and math.isnan(i):
            list_data.extend([None])
        else:

            list_data.append([""+uConfig.now_sheelm.split("_")[0]+data_dict[i]])
    print("我是list_data")
    print(list_data)
    return list_data


#只是正对Point来做的
def _id_list(id_list):
    data_from =  uConfig.now_data_form.copy()
    number_list = [[int(item[2:])] for item in data_from["物探点号"].values.tolist()]
    return number_list


import pandas as pd
if __name__ == "__main__":
    # file = pd.read_excel(r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\中文管点附属物对应字母.xlsx",sheet_name="字段")
    # data_dict = file.set_index('地面箱式变压器').to_dict()['XB']
    # print(data_dict)
    # print(math.nan)
    # print(type(math.nan))
    # print(  math.isnan(math.nan))
    # list_=tz_list([nan,nan,nan,nan])
    # print(list_)
    # print(list_[0])
    uConfig.now_data_form = pd.read_excel(r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\采集成果20230915(1).xls",sheet_name="LD_POINT")
    list=_id_list([])
    print(list)

