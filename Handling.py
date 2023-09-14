import UntilConfig as uConfig


def process_fields(name,list):
    #属于管道
    if name=="管径":
        data_list=gj_list(list)
        return data_list
    if name=="井盖尺寸":
        data_list=gj_list(list)
        return data_list




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

# def tz_list(tz_list):
#     for i in tz_list:




