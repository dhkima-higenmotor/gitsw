@echo off
setlocal

REM # Input Argument
set project-name=%1

cd /D "D:\github\"%project-name%
set /p branch-name=<.current_user

REM # Commit
git add --all
git commit -m "Update before New Branch"
git push -u origin main

REM # branch main
git checkout main
git pull

REM # branch branch-name
git branch %branch-name%
git checkout %branch-name%

findstr /X %branch-name% .branch_list && echo Exists already. || echo %branch-name%>> .branch_list

