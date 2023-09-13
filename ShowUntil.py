import pandas as pd
#获取表的
def getExclSheet(path):
    excel_file = pd.ExcelFile(path)
    name=excel_file.sheet_names
    print(name)
    return name














if __name__=="__main__":
    getExclSheet(r"F:\咸鱼项目\8-8咸鱼unet项目\测试\testAccess\newTest\字段表演示.xlsx")