# 1.自动化船体建模（粗模）

- Step1.将 [型值表.xlsx](型值表.xlsx)按照如下步骤改造成 [改造后型值表.xlsx](改造后型值表.xlsx) 

<img src="型值表处理步骤.png" width="600" />

- Step2.使用脚本 [GetPointsFromOffsetTable.py](GetPointsFromOffsetTable.py) 生成点数据表格 [点数据.xls](点数据.xls) 
- Step3.打开Rhino，运行脚本 [DrawHullLinesInRhino.py](DrawHullLinesInRhino.py) 生成曲线并自动放样生成曲面

<img src="runPythonInRhino.png" width="600" />

