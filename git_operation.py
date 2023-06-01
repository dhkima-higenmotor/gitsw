import os
import webbrowser

def read_config(file_name):
    with open('./Config/'+file_name,'r') as f:
        lines = f.read().splitlines()
    f.close()
    return lines

def current_path():
    currentpath = os.getcwd()
    confpath = currentpath+"\\Config\\exepath"
    f = open(confpath,'w')
    f.write(currentpath)
    f.close()
    return currentpath

def sw_start():
    SLDWORKS = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SLDWORKS.exe"
    os.system('"'+SLDWORKS+'"')
    return 0

def files_start(repo,root):
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system("start "+PATH_TARGET)
        return 0
    else:
        os.system("start "+root)
        print(f"\n# No exists : {PATH_TARGET}")
        return -1

def git_clone(server,organ,repo,user,token,root,gitpath):
    URL_SOURCE = "https://"+user+":"+token+"@"+server+"/"+organ+"/"+repo+".git"
    URL_SOURCE2 = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        print(f"\n# Already exist : {PATH_TARGET}")
        return -1
    else:
        try:
            print(f"\n# Clone starts from : \n{URL_SOURCE}")
            gitpath2 = '"'+gitpath+"\git.exe"+'"'
            os.system(gitpath2+" clone "+URL_SOURCE+" "+PATH_TARGET)
            print(f"\ngit clone {URL_SOURCE2} {PATH_TARGET}")
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" lfs install --local")
            print(f"\ngit lfs install --local")
            return 0
        except:
            print(f"\n# No Repo : {URL_SOURCE2}")
            return -2

def git_pull(repo,root,gitpath):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        try:
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" fetch --all")
            print(f"\ngit fetch --all")
            os.system(gitpath2+" pull --all")
            print(f"\ngit pull --all")
            return 0
        except:
            print(f"\n# No Repo : {PATH_TARGET}")
            return -2
    else:
        print(f"\n# Not exists : \n{PATH_TARGET}")
        return -1

def git_make(server,organ,repo,user,token,root,gitpath,exepath):
    #URL_SOURCE = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = f"{root}\\{repo}"
    gitpath2 = f"'{gitpath}\\git.exe'"
    if os.path.isdir(PATH_TARGET):
        print(f"\n# Already exist : {PATH_TARGET}")
        return -1
    else:
        # Make new repository on Github.com
        os.system("gh repo create --internal "+organ+"/"+repo)
        print(f"gh repo create --internal {organ}/{repo}")
        # Clone
        error = git_clone(server,organ,repo,user,token,root,gitpath)
        print(f"\n# Clone to : \n{PATH_TARGET}")
        os.chdir(PATH_TARGET)
        # Init
        if error==0:
            print(f"\n# Initializing... \n")
            os.system(gitpath2+" lfs install --local")
            print(f"\ngit lfs install --local")
            os.system("copy "+exepath+"\\Dotfiles\\_gitattributes "+PATH_TARGET+"\\.gitattributes")
            print(f"\ncopy {exepath}\\Dotfiles\\_gitattributes {PATH_TARGET}\\.gitattributes")
            os.system("copy "+exepath+"\\Dotfiles\\_gitignore "+PATH_TARGET+"\\.gitignore")
            print(f"\ncopy {exepath}\\Dotfiles\\_gitignore {PATH_TARGET}\\.gitignore")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"/README.md")
            print(f"\necho # {repo} > {PATH_TARGET}/README.md")
            os.system("mkdir "+PATH_TARGET+"\\3D")
            print(f"\nmkdir {PATH_TARGET}\\3D")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"\\3D\\README.md")
            print(f"\necho # {repo} > {PATH_TARGET}\\3D\\README.md")
            # 1st Push
            os.system(gitpath2+" add --all")
            print(f"\ngit add --all")
            os.system(gitpath2+" commit -m '1st'")
            print(f"\ngit commit -m '1st'")
            os.system(gitpath2+" push --set-upstream origin HEAD")
            print(f"\ngit push --set-upstream origin HEAD")
            print(f"\n# Check [Archives]:[Include Git LFS objects in archives] in this address :\n")
            print(f"https://{server}/{organ}/{repo}/settings")
            print(f"\n# Check Repository Setting to use LFS :")
            print(f"https://{server}/{organ}/{repo}/settings")
            webbrowser.open("https://"+server+"/"+organ+"/"+repo+"/settings")
            return 0
        else:
            print(f"\n# Fail. \n")
            return -1

def git_push(repo,root,gitpath,commit_message,change_branch):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        try:
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" checkout "+change_branch)
            print(f"\ngit checkout {change_branch}")
            os.system(gitpath2+" add --all")
            print(f"\ngit add --all")
            print(f"\ngit status")
            os.system(gitpath2+" status")
            temp = f"{gitpath2} commit -m '{commit_message}'"
            os.system(temp)
            print(f"\ngit commit -m '{commit_message}'")
            print(f"\ngit status")
            os.system(gitpath2+" status")
            os.system(gitpath2+" push")
            print(f"\ngit push")
            print(f"\n# Push Finished. \n")
            return 0
        except:
            print(f"\n# No Repo : {URL_SOURCE2}")
            return -2
    else:
        print(f"\n# Not exists : \n{PATH_TARGET}")
        return -1

def git_branch(repo,root,gitpath,change_branch):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath2+" branch "+change_branch)
        print(f"\ngit branch {change_branch}")
        os.system(gitpath2+" checkout "+change_branch)
        print(f"\ngit checkout {change_branch}")
        return 0
    else:
        print(f"\n# Not exists : \n{PATH_TARGET}")
        return -1

def git_merge(repo,root,gitpath,change_branch,change_merge):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath2+" checkout "+change_branch)
        print(f"\ngit checkout {change_branch}")
        os.system(gitpath2+" merge -Xtheirs "+change_merge)
        print(f"\ngit merge -Xtheirs {change_merge}")
        return 0
    else:
        print(f"\n# Not exists : \n{PATH_TARGET}")
        return -1