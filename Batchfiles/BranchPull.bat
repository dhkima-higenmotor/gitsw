@echo off
setlocal

REM # Input Argument
set project-name=%1
set branch-name=%2

REM # branch
cd /D "D:\github\"%project-name%
git branch %branch-name%
git checkout %branch-name%
git pull
