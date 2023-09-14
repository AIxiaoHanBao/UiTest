import math

from numpy import nan

import UntilConfig as uConfig

tz_list_dic = {'电力井': 'YJ', '跌水井': 'DSJ', '发射塔': 'TT', '阀门': 'FM', '阀门井': 'FMJ', '分线箱': 'JXX',
               '化粪池': 'HFC', '监视器': 'JSQ', '检查井': 'YJ', '检修井': 'JXJ', '交通信号杆': 'XHD', '排气阀': 'PQF',
               '排气井': 'PQFJ', '配电房': 'PDF', '人孔井': 'RK', '手孔井': 'SK', '水表': 'SB', '水表井': 'SBJ',
               '水塔': 'ST', '消防井': 'FMJ', '消防栓': 'XFS', '信号灯': 'XHD', '雨篦': 'YSB', '变材': 'BC',
               '变径': 'BJ', '出水口': 'CSK', '多通': 'DT', '非探测区': 'FP', '进水口': 'JSK', '井边点': 'JBD',
               '蒙板': 'GM', '入户点': 'JRD', '三分支': '3FZ', '三通': '3T', '上杆（引上点）': 'SG', '四分支': '4FZ',
               '四通': '4T', '弯头': 'WT', '一般管线点': 'GD', '预留口': 'YLK', '转折点': 'ZZD',"灯杆":'DG'}


def process_fields(name,list):
    #属于管道
    if name=="管径" or name=="井盖尺寸" :
        return gj_list(list)

    if name=="特征" or name == "附属物":
        return tz_list(list)





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
    list_data = []
    for i in tz_list:
        print(i)
        print(type(i))
        if type(i)!=str and math.isnan(i):
            list_data.extend([None])
        else:
            print(i)
            print(type(i))
            list_data.append([tz_list_dic[i]])
    print("我是list_data")
    print(list_data)
    return list_data






import pandas as pd
if __name__ == "__main__":
    # file = pd.read_excel(r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\中文管点附属物对应字母.xlsx",sheet_name="字段")
    # data_dict = file.set_index('地面箱式变压器').to_dict()['XB']
    # print(data_dict)
    # print(math.nan)
    # print(type(math.nan))
    # print(  math.isnan(math.nan))
    list_=tz_list([nan,nan,nan,nan])
    print(list_)
    print(list_[0])

