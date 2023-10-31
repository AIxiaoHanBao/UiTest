# ReadMe
p3.7 win64打包
```cmd
pyinstaller --clean --add-data ./QCandyUi/;./QCandyUi/ -c -i Ai.png Show.py DealShow.py DealUi.py Handling.py MdbController.py EclController.py Populate.py ShowUntil.py UntilConfig.py
```
p32 win32打包
```cmd
pyinstaller --clean -c -i Ai.png Show.py DealShow.py DealUi.py Handling.py  MdbController.py EclController.py Populate.py ShowUntil.py UntilConfig.py
```

## 环境
python == 3.7

其他的懒得打

# 2023-10-31
修复了只显示LINE和POINT表格名称，支持更多，开放性更多