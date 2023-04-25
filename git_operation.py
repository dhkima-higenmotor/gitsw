import os
from git import Repo

def read_config(file_name):
    with open('./Config/'+file_name,'r') as f:
        lines = f.read().splitlines()
    f.close()
    return lines

#def git_make():

def git_clone(server,organ,repo,user,token,root):
    URL_SOURCE = "https://"+user+":"+token+"@"+server+"/"+organ+"/"+repo+".git"
    PATH_TARGET = root+"/"+repo
    if os.path.isdir(PATH_TARGET):
        print("# Already exist : \n"+PATH_TARGET)
        return 0
    else:
        cloned_repo = Repo.clone_from(URL_SOURCE,PATH_TARGET,depth=1)
        print("# Clone Finished.")
        print(cloned_repo)
        return cloned_repo

def git_pull(repo,root):
    PATH_TARGET = root+"/"+repo
    repo = Repo(PATH_TARGET)
    o = repo.remotes.origin
    o.pull()
    print("# Pull Finished.")
    print(repo)
    return repo
