import mygit
import os.path

# Init Configs
conffile = "D:\\github\\gitsw\\conf.csv"

if os.path.isfile(conffile):
    conf = mygit.config(conffile)
    data = conf.read()
    for i in range(len(data)):
        print(f"{data[i][0]} : {data[i][1]}")
        if data[i][0] == "server":
            server = data[i][1]
        elif data[i][0] == "organ":
            organ = data[i][1]
        elif data[i][0] == "user":
            user = data[i][1]
        elif data[i][0] == "email":
            email = data[i][1]
        elif data[i][0] == "token":
            token = data[i][1]
        elif data[i][0] == "root":
            root = data[i][1]
        elif data[i][0] == "exepath":
            exepath = data[i][1]
        elif data[i][0] == "gitpath":
            gitpath = data[i][1]
        elif data[i][0] == "swpath":
            swpath = data[i][1]        
else:
    server  = "github.com"
    organ   = "mech-higenmotor"
    user    = "Your username"
    email   = "Your email"
    token   = "Github Personal Access Token"
    root    = "D:\github"
    exepath = "D:\github\gitsw"
    gitpath = "C:\Program Files\Git"
    swpath  = "C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS"

# Test
repo = "TEST"
MYGIT = mygit.mygit(server, organ, user, email, token, root, exepath, gitpath, swpath)
MYGIT.check_repo(repo)
print(token)
