@echo off

REM set root=C:\ProgramData\Anaconda3
set /p root=<condapath
call %root%\Scripts\activate.bat %root%

REM call conda env list
call conda activate base
call cd D:\github\gitsw
call python gitsw.py

REM pause
exit

