@echo off
setlocal

REM # Input Argument
set project-name=%1
set member-name=%2

REM # Add member list
cd /D "D:\github\"%project-name%

findstr /X %member-name% .member_list && echo Exists already. || echo %member-name%>> .member_list
