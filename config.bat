@echo off

REM path
call %userprofile%\scoop\apps\miniconda3\current\Scripts\activate.bat

REM execute
cd D:\github\gitsw
call python config.py

REM pause
exit
