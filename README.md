# gitsw

_Github Client for Sloidworks_

## Requirements

### 1. Git for Windows Portable
* Make folder `D:\UTIL`
* Download `64-bit Git for Windows Portable` in https://git-scm.com/download/win 
* Move & Extract as D:\UTIL\Git`

### 2. Github CLI
* Download  & Install `msi` file from https://cli.github.com/
* Auth Environment Variable : `GH_TOKEN`

### 3. Anaconda
* https://www.anaconda.com/download/
* Download and Install

### 4. Windows Terminal
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
