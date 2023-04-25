# gitsw

_Github Client for Sloidworks_

## Requirements

### 1. Git for Windows Portable
* Make folder `D:\UTIL`
* Download `64-bit Git for Windows Portable` in https://git-scm.com/download/win 
* Move & Extract into `D:\UTIL\Git`

### 2. Github CLI
* Download  & Install `msi` file from https://cli.github.com/
* Auth Environment Variable : `GH_TOKEN`

### 3. Windows Terminal
* Execution : `wt.exe`
* New Profiles : git-cmd
  - Name : `git-cmd`
  - Command : `D:\UTIL\Git\git-cmd.exe`
  - Start : `D:\`
  - Icon : `D:\UTIL\Git\mingw64\share\git\git-for-windows.ico`

* New Profiles : git-bash
  - Name : `git-bash`
  - Command : `D:\UTIL\Git\git-bash.exe -i -l`
  - Start : `D:\`
  - Icon : `D:\UTIL\Git\mingw64\share\git\git-for-windows.ico`

* New Profiles : Anaconda3
  - Name : `Anaconda3`
  - Command : `%windir%\System32\cmd.exe "/K" D:\UTIL\anaconda3\Scripts\activate.bat D:\UTIL\anaconda3`
  - Start : `D:\`
  - Icon : `D:\UTIL\anaconda3\Menu\anaconda-navigator.ico`


## Config

* Environment Variable

```
GH_TOKEN = <github_token>
```

* git global

```
git config --global user.email "...@..."
git config --global user.name "..."
git config --global color.ui auto
git config --global core.editor 'code'
git config --global credential.helper cache
git config --global push.default matching
git config --global init.defaultBranch main
```

* github CLI

```
gh config set editor "code -w"
gh config set git_protocol https
# gh auth login
```

## Requirements to Development

### 1. Anaconda
* https://www.anaconda.com/download/
* Download and Install into `D:\UTIL\anaconda3`

### 2. Python Libraries

```
pip install PySimpleGUI
pip install GitPython
pip install github-cli
```
