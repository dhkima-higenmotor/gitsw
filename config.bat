@echo off

set root=C:\ProgramData\Anaconda3
call %root%\Scripts\activate.bat %root%

REM call conda env list
call conda activate base
call cd D:\codeberg\gitsw
call python config.py

REM pause
exit

