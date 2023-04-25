set root=D:\UTIL\anaconda3
call %root%\Scripts\activate.bat %root%

REM call conda env list
call conda activate base
call cd D:\codeberg\gitsw
call python gitsw.py

REM pause
exit

