# How to settup

## 1. Install Git_for_Windows

* Download [Git-2.40.1-64-bit.exe](https://github.com/git-for-windows/git/releases/download/v2.40.1.windows.1/Git-2.40.1-64-bit.exe) and install.
* Start `cmd` or `wt`, and type like that :

```cmd
git config --global user.email "<Email_address>"
git config --global user.name "<Username>"
git config --global color.ui auto
git config --global core.editor 'code'
git config --global push.default matching
git config --global init.defaultBranch main
```

## 2. Install Github-CLI

* Download [gh_2.28.0_windows_amd64.msi](https://github.com/cli/cli/releases/download/v2.28.0/gh_2.28.0_windows_amd64.msi) and install.
* Start `cmd` or `wt`, and type like that :

```cmd
setx GH_TOKEN <Github_Token>
gh config set editor "code -w"
gh config set git_protocol https
``` 

* `<Github_Token>` : [Use what created in Github personal access token](https://docs.github.com/ko/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)


## 3. Install Anaconda3

* Download [Anaconda3-2023.03-1-Windows-x86_64.exe](https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Windows-x86_64.exe) and install.
* Start `Anaconda Prompt (Anaconda3)`, and type like that :

```cmd
pip install PySimpleGUI
```

## 4. Install VScode (Optional)

* Download [System_Installer](https://code.visualstudio.com/download#) and install.

## 5. Install gitsw

* Start `Git CMD`, and type like that :

```cmd
mkdir D:\github
git clone --depth=1 https://github.com/dhkima-higenmotor/gitsw.git D:\github\gitsw
cd /D D:\github\gitsw
```

* Start `cmd` or `wt`, and type like that :

```cmd
# Modify Commit Messages
code D:\github\gitsw\Config\commits

# Check and Modify path of gitsw
code D:\github\gitsw\Config\exepath

# Modify Font and size
code D:\github\gitsw\Config\font

# Check and Modify path of `git.exe`
code D:\github\gitsw\Config\gitpath

# Modify Organizations
code D:\github\gitsw\Config\organs

# Modify Repositoies
code D:\github\gitsw\Config\repos

# Check and Modify path of Github root
code D:\github\gitsw\Config\root

# Check github.com
code D:\github\gitsw\Config\server

# Check and Modify GUI theme
code D:\github\gitsw\Config\theme

# Check and Modify list of users
code D:\github\gitsw\Config\users

# Write Github personal access token
code D:\github\gitsw\Config\token
```

## 6. Test

