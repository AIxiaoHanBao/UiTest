import pandas as pd
#测试Point的专属字段是否存在，存在则执行



if __name__ == '__main__':
    df = pd.read_excel("采集成果.xls")
    print("X坐标" in df)