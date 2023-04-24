@echo off
setlocal

REM # Input Argument
set organ-name=%1
set project-name=%2

REM # Clone Repository from Github
cd /D "D:\github"
REM git clone --depth=1 https://github.com/%organ-name%/%project-name%.git
git clone https://github.com/%organ-name%/%project-name%.git
