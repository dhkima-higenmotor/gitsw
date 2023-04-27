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
        print("\n# No exists : "+PATH_TARGET)
        return -1

def git_clone(server,organ,repo,user,token,root,gitpath):
    URL_SOURCE = "https://"+user+":"+token+"@"+server+"/"+organ+"/"+repo+".git"
    URL_SOURCE2 = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        print("\n# Already exist : "+PATH_TARGET)
        return -1
    else:
        try:
            print("\n# Clone starts from : \n"+URL_SOURCE)
            gitpath2 = '"'+gitpath+"\git.exe"+'"'
            os.system(gitpath2+" clone "+URL_SOURCE+" "+PATH_TARGET)
            print("\n"+gitpath2+" clone "+URL_SOURCE2+" "+PATH_TARGET)
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" lfs install --local")
            print("\n"+gitpath2+" lfs install --local")
            return 0
        except:
            print("\n# No Repo : "+URL_SOURCE2)
            return -2

def git_pull(repo,root,gitpath):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        try:
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" fetch --all")
            print("\n"+gitpath2+" fetch --all")
            os.system(gitpath2+" pull --all")
            print("\n"+gitpath2+" pull --all")
            return 0
        except:
            print("\n# No Repo : "+PATH_TARGET)
            return -2
    else:
        print("\n# Not exists : \n"+PATH_TARGET)
        return -1

def git_make(server,organ,repo,user,token,root,gitpath,exepath):
    #URL_SOURCE = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        print("\n# Already exist : "+PATH_TARGET)
        return -1
    else:
        # Make new repository on Github.com
        os.system("gh repo create --internal "+organ+"/"+repo)
        print("gh repo create --internal "+organ+"/"+repo)
        # Clone
        error = git_clone(server,organ,repo,user,token,root,gitpath)
        print("\n# Clone to : \n"+PATH_TARGET)
        os.chdir(PATH_TARGET)
        # Init
        if error==0:
            print("\n# Initializing... \n")
            os.system(gitpath2+" lfs install --local")
            print("\n"+gitpath2+" lfs install --local")
            os.system("copy "+exepath+"\\Dotfiles\\_gitattributes "+PATH_TARGET+"\\.gitattributes")
            print("\ncopy "+exepath+"\\Dotfiles\\_gitattributes "+PATH_TARGET+"\\.gitattributes")
            os.system("copy "+exepath+"\\Dotfiles\\_gitignore "+PATH_TARGET+"\\.gitignore")
            print("\ncopy "+exepath+"\\Dotfiles\\_gitignore "+PATH_TARGET+"\\.gitignore")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"/README.md")
            print("\necho "+"# "+repo+">"+PATH_TARGET+"/README.md")
            os.system("mkdir "+PATH_TARGET+"\\3D")
            print("\nmkdir "+PATH_TARGET+"\\3D")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"\\3D\\README.md")
            print("\necho "+"# "+repo+">"+PATH_TARGET+"\\3D\\README.md")
            # 1st Push
            os.system(gitpath2+" add --all")
            print("\n"+gitpath2+" add --all")
            os.system(gitpath2+" commit -m '1st'")
            print("\n"+gitpath2+" commit -m '1st'")
            os.system(gitpath2+" push --set-upstream origin HEAD")
            print("\n"+gitpath2+" push --set-upstream origin HEAD")
            print("\n# Check [Archives]:[Include Git LFS objects in archives] in this address :\n")
            print("https://"+server+"/"+organ+"/"+repo+"/settings")
            print("\n# Check Repository Setting to use LFS :")
            print("https://"+server+"/"+organ+"/"+repo+"/settings")
            webbrowser.open("https://"+server+"/"+organ+"/"+repo+"/settings")
            return 0
        else:
            print("\n# Fail. \n")
            return -1

def git_push(repo,root,gitpath,commit_message,change_branch):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        try:
            os.chdir(PATH_TARGET)
            os.system(gitpath2+" checkout "+change_branch)
            print("\n"+gitpath2+" checkout "+change_branch)
            os.system(gitpath2+" add --all")
            print("\n"+gitpath2+" add --all")
            os.system(gitpath2+" commit -m '"+commit_message+"'")
            print("\n"+gitpath2+" commit -m '"+commit_message+"'")
            os.system(gitpath2+" push --all")
            print("\n"+gitpath2+" push --all")
            print("\n# Push Finished. \n")
            return 0
        except:
            print("\n# No Repo : "+URL_SOURCE2)
            return -2
    else:
        print("\n# Not exists : \n"+PATH_TARGET)
        return -1

def git_branch(repo,root,gitpath,change_branch):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath2+" branch "+change_branch)
        print("\n"+gitpath2+" branch "+change_branch)
        os.system(gitpath2+" checkout "+change_branch)
        print("\n"+gitpath2+" checkout "+change_branch)
        return 0
    else:
        print("# Not exists : \n"+PATH_TARGET)
        return -1

def git_merge(repo,root,gitpath,change_branch,change_merge):
    PATH_TARGET = root+"\\"+repo
    gitpath2 = '"'+gitpath+"\git.exe"+'"'
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath2+" checkout "+change_branch)
        print("\n"+gitpath2+" checkout "+change_branch)
        os.system(gitpath2+" merge -Xtheirs "+change_merge)
        return 0
    else:
        print("\n# Not exists : \n"+PATH_TARGET)
        return -1