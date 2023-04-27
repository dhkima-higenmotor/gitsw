import os

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
        print("# No exists : "+PATH_TARGET)
        return -1

def git_clone(server,organ,repo,user,token,root,gitpath):
    URL_SOURCE = "https://"+user+":"+token+"@"+server+"/"+organ+"/"+repo+".git"
    URL_SOURCE2 = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        print("# Already exist : "+PATH_TARGET)
        return -1
    else:
        try:
            print("# Clone starts from : \n"+URL_SOURCE)
            os.system(gitpath+"\git.exe clone "+URL_SOURCE+" "+PATH_TARGET)
            print(gitpath+"\git.exe clone "+URL_SOURCE2+" "+PATH_TARGET)
            os.chdir(PATH_TARGET)
            os.system(gitpath+"\git.exe lfs install --local")
            print(gitpath+"\git.exe lfs install --local")
            return 0
        except:
            print("")
            print("# No Repo : "+URL_SOURCE2)
            return -2

def git_pull(repo,root,gitpath):
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath+"\git.exe fetch --all")
        print(gitpath+"\git.exe fetch --all")
        os.system(gitpath+"\git.exe pull --all")
        print(gitpath+"\git.exe pull --all")
        return 0
    else:
        print("# Not exists : \n"+PATH_TARGET)
        return -1

def git_make(server,organ,repo,user,token,root,gitpath,exepath):
    URL_SOURCE = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        print("# Already exist : "+PATH_TARGET)
        return -1
    else:
        # Make new repository on Github.com
        #os.system("gh repo create --public "+repo)
        #print("gh repo create --public "+repo)
        os.system("gh repo create --internal "+organ+"/"+repo)
        print("gh repo create --internal "+organ+"/"+repo)
        # Clone
        error = git_clone(server,organ,repo,user,token,root,gitpath)
        print("# Clone to : \n"+PATH_TARGET)
        os.chdir(PATH_TARGET)
        # Init
        if error==0:
            print("# Initializing... \n")
            os.system(gitpath+"\git.exe lfs install --local")
            print(gitpath+"\git.exe lfs install --local")
            os.system("copy "+exepath+"\\Dotfiles\\_gitattributes "+PATH_TARGET+"\\.gitattributes")
            print("copy "+exepath+"\\Dotfiles\\_gitattributes "+PATH_TARGET+"\\.gitattributes")
            os.system("copy "+exepath+"\\Dotfiles\\_gitignore "+PATH_TARGET+"\\.gitignore")
            print("copy "+exepath+"\\Dotfiles\\_gitignore "+PATH_TARGET+"\\.gitignore")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"/README.md")
            print("echo "+"# "+repo+">"+PATH_TARGET+"/README.md")
            os.system("mkdir "+PATH_TARGET+"\\3D")
            print("mkdir "+PATH_TARGET+"\\3D")
            os.system("echo "+"# "+repo+">"+PATH_TARGET+"\\3D\\README.md")
            print("echo "+"# "+repo+">"+PATH_TARGET+"\\3D\\README.md")
            # 1st Push
            os.system(gitpath+"\git.exe add --all")
            print(gitpath+"\git.exe add --all")
            os.system(gitpath+"\git.exe commit -m \"1st\"")
            print(gitpath+"\git.exe commit -m \"1st\"")
            os.system(gitpath+"\git.exe push --set-upstream origin HEAD")
            print(gitpath+"\git.exe push --set-upstream origin HEAD")
            print("\n")
            print("Check [Archives]:[Include Git LFS objects in archives] in this address :\n")
            print("https://"+server+"/"+organ+"/"+repo+"/settings")
            return 0
        else:
            print("# Fail. \n")
            return -1

def git_push(repo,root,gitpath,commit_message,change_branch):
    PATH_TARGET = root+"\\"+repo
    os.chdir(PATH_TARGET)
    os.system(gitpath+"\git.exe checkout "+change_branch)
    print(gitpath+"\git.exe checkout "+change_branch)
    os.system(gitpath+"\git.exe add --all")
    print(gitpath+"\git.exe add --all")
    os.system(gitpath+"\git.exe commit -m \""+commit_message+"\"")
    print(gitpath+"\git.exe commit -m \""+commit_message+"\"")
    os.system(gitpath+"\git.exe push --all")
    print(gitpath+"\git.exe push --all")
    #os.system(gitpath+"\git.exe push -u origin "+change_branch)
    #print(gitpath+"\git.exe push -u origin "+change_branch)
    print("# Finished. \n")
    return 0

def git_branch(repo,root,gitpath,change_branch):
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath+"\git.exe branch "+change_branch)
        print(gitpath+"\git.exe branch "+change_branch)
        os.system(gitpath+"\git.exe checkout "+change_branch)
        print(gitpath+"\git.exe checkout "+change_branch)
        return 0
    else:
        print("# Not exists : \n"+PATH_TARGET)
        return -1

def git_merge(repo,root,gitpath,change_branch,change_merge):
    PATH_TARGET = root+"\\"+repo
    if os.path.isdir(PATH_TARGET):
        os.chdir(PATH_TARGET)
        os.system(gitpath+"\git.exe checkout "+change_branch)
        print(gitpath+"\git.exe checkout "+change_branch)
        os.system(gitpath+"\git.exe merge -Xtheirs "+change_merge)
        return 0
    else:
        print("# Not exists : \n"+PATH_TARGET)
        return -1