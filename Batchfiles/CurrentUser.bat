@echo off
setlocal

REM # Input Argument
set project-name=%1

cd /D "D:\github\"%project-name%
gh api user -q ".login" > .current_user
