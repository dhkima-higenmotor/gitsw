import os

def read_config(file_name):
    with open('./Config/'+file_name,'r') as f:
        lines = f.read().splitlines()
    f.close()
    return lines

def git_clone(server,organ,repo,user,token,root,gitpath):
    URL_SOURCE = "https://"+user+":"+token+"@"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"/"+repo
    if os.path.isdir(PATH_TARGET):
        print("# Already exist : \n"+PATH_TARGET)
        return -1
    else:
        print("# Clone starts from : \n"+URL_SOURCE)
        os.system(gitpath+"\git.exe clone "+URL_SOURCE+" "+PATH_TARGET)
        os.system(gitpath+"\git.exe lfs install --local")
        print("# Clone finished into : \n"+PATH_TARGET)
        return 0

def git_pull(repo,root,gitpath):
    PATH_TARGET = root+"/"+repo
    if os.path.isdir(PATH_TARGET):
        os.system(gitpath+"\git.exe pull")
        print("# Pull finished into : \n"+PATH_TARGET)
        return 0
    else:
        print("# Not exists : \n"+PATH_TARGET)
        return -1

def git_push(gitpath):
    os.system(gitpath+"\git.exe push")
    return 0

def git_make(server,organ,repo,user,token,root,gitpath,exepath):
    URL_SOURCE = "https://"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"\\"+repo
    # Make new repository on Github.com
    ##os.system("gh repo create --public "+repo)
    #os.system("gh repo create --internal "+organ+"/"+repo)
    ##print("# Made new remote repository : \n"+URL_SOURCE)
    # Clone
    ##error = git_clone(server,organ,repo,user,token,root,gitpath)
    ##print("# Clone to : \n"+PATH_TARGET)
    # Init
    error = 0
    if error==0:
        print("# Initializing... \n")
        #os.system(gitpath+"\git.exe lfs install --local")
        os.system("copy "+exepath+"\\Dotfiles\\_gitattribute "+PATH_TARGET+"\\.gitattribute")
        print("copy "+exepath+"\\Dotfiles\\_gitattribute "+PATH_TARGET+"\\.gitattribute")
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
        os.system(gitpath+"\git.exe push")
        #os.system(gitpath+"\git.exe push --set-upstream origin HEAD")
        #print(gitpath+"\git.exe push --set-upstream origin HEAD")
        print("# Finished. \n")
        return 0
    else:
        print("# Fail. \n")
        return -1

def current_path():
    currentpath = os.getcwd()
    confpath = currentpath+"\\Config\\exepath"
    f = open(confpath,'w')
    f.write(currentpath)
    f.close()
    return currentpath

