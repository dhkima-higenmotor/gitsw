@echo off
setlocal

REM # Input Argument
set project-name=%1

REM # Branch List
git checkout main
cd /D "D:\github\"%project-name%
git branch > .branch_list

REM # Delete "* "
FOR /F "tokens=* delims=" %%i IN (.branch_list) DO SET text=%%i
set text=%text:* =% 
echo %text% > .branch_list
