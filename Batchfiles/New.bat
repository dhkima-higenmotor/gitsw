@echo off
setlocal

REM # Input Argument
set organ-name=%1
set project-name=%2

REM # Make New Repository on Github
cd /D "D:\github"
gh repo create --internal --clone %organ-name%/%project-name%

REM # README.md
cd %project-name%
echo # %project-name% > README.md

REM # Dotfiles
copy "D:\github\gitsw\Dotfiles\_gitignore" .gitignore
copy "D:\github\gitsw\Dotfiles\_gitattribute" .gitattribute
copy "D:\github\gitsw\Dotfiles\_member_list" .member_list

REM # MakeDirectory
mkdir 3D
echo # Solidworks 3D Modeling > ".\3D\README.md"

REM # 1st Commit & Push
git add --all
git commit -m "1st"
git push --set-upstream origin HEAD
