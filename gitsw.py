import PySimpleGUI as sg
import os

# Internal functions
import git_operation

# Theme
sg.theme(git_operation.read_config('theme')[0])
sg.set_options(font=git_operation.read_config('font')[0])

# Config
NAME_SIZE = 16
BUTTON_WIDTH = 8
INPUT_WIDTH = 27
OUTPUT_WIDTH = 40
LIST_USERS = git_operation.read_config('list_users')
LIST_ORGANS = git_operation.read_config('list_organs')
LIST_REPOS = git_operation.read_config('list_repos')
LIST_BRANCH = LIST_USERS.copy()
LIST_BRANCH.append("main")
LIST_COMMIT = git_operation.read_config('list_commit')
SERVER = git_operation.read_config('server')[0]
ROOT = git_operation.read_config('root')[0]
TOKEN = git_operation.read_config('token')[0]
#os.system("set GH_TOKEN="+TOKEN)
GITPATH = git_operation.read_config('gitpath')[0]
git_operation.current_path()
EXEPATH = git_operation.read_config('exepath')[0]

# GUI Name Width
def name(name):
    dots = NAME_SIZE-len(name)-2
    return sg.Text(name+' '*dots,size=(NAME_SIZE,1),justification='r',pad=(0,0))

# GUI Layout
left_column = [
    [name('1.USER'), sg.Combo(values=LIST_USERS,default_value=LIST_USERS[0],size=(INPUT_WIDTH,1),key='-USER-',enable_events=True)],
    [name('2.ORGANIZATION'), sg.Combo(values=LIST_ORGANS,default_value=LIST_ORGANS[0],size=(INPUT_WIDTH,1),key='-ORGAN-',enable_events=True)],
    [name('3.REPOSITORY'), sg.Combo(values=LIST_REPOS,default_value=LIST_REPOS[0],size=(INPUT_WIDTH,1),key='-REPO-',enable_events=True)],
    [name(''), sg.Button('MAKE',key='-MAKE-',size=(BUTTON_WIDTH,1)), sg.Button('CLONE',key='-CLONE-',size=(BUTTON_WIDTH,1)), sg.Button('PULL',key='-PULL-',size=(BUTTON_WIDTH,1))],
    [name('4.BRANCH'), sg.Combo(values=LIST_BRANCH,default_value=LIST_BRANCH[0],size=(INPUT_WIDTH,1),key='-CHANGE_BRANCH-',enable_events=True)],
    [name('5.MERGE ↑'), sg.Combo(values=LIST_BRANCH,default_value=LIST_BRANCH[1],size=(INPUT_WIDTH,1),key='-CHANGE_MERGE-',enable_events=True)],
    [name(''), sg.Button('MERGE',key='-MERGE-',size=(BUTTON_WIDTH,1))],
    [name('6.START'), sg.Button('SLDWORKS',key='-SLDWORKS-',size=(BUTTON_WIDTH,1)), sg.Button('FILES',key='-FILES-',size=(BUTTON_WIDTH,1))],
    [name('7.PUSH'), sg.Combo(values=LIST_COMMIT,default_value=LIST_COMMIT[0],size=(INPUT_WIDTH,1),key='-COMMIT_MESSAGE-',enable_events=True)],
    [name(''), sg.Button('PUSH',key='-PUSH-',size=(BUTTON_WIDTH,1))]
]

right_column = [
    [name('OUTPUT')],
    [sg.Output(key='-OUTPUT-',size=(OUTPUT_WIDTH,13))],
    [sg.Button('CLEAR',key='-CLEAR-',size=(BUTTON_WIDTH,1)), sg.Button('ABOUT',key='-ABOUT-',size=(BUTTON_WIDTH,1)), sg.Button('EXIT',key='-EXIT-',size=(BUTTON_WIDTH,1))]
]

layout = [
    [
        sg.Column(left_column),
        sg.VSeperator(),
        sg.Column(right_column)
    ]
]

window = sg.Window('GitSW - Github Client for Solidworks', layout)

while True:
    event, values = window.read() 
    if event==sg.WIN_CLOSED or event=='-EXIT-':
        break
    #elif event=='-USER-':
        #print(values)
    #elif event=='-ORGAN-':
    #elif event=='-REPO-':
    elif event=='-MAKE-':
        git_operation.git_make(SERVER,values["-ORGAN-"],values["-REPO-"],values["-USER-"],TOKEN,ROOT,GITPATH,EXEPATH)
    elif event=='-CLONE-':
        git_operation.git_clone(SERVER,values["-ORGAN-"],values["-REPO-"],values["-USER-"],TOKEN,ROOT,GITPATH)
    elif event=='-PULL-':
        git_operation.git_pull(values["-REPO-"],ROOT,GITPATH)
    elif event=='-CHANGE_BRANCH-':
        git_operation.git_branch(values["-REPO-"],ROOT,GITPATH,values["-CHANGE_BRANCH-"])
    #elif event=='-CHANGE_MERGE-':
    elif event=='-MERGE-':
        git_operation.git_merge(values["-REPO-"],ROOT,GITPATH,values["-CHANGE_BRANCH-"],values["-CHANGE_MERGE-"])
    elif event=='-SLDWORKS-':
        git_operation.sw_start()
    elif event=='-FILES-':
        git_operation.files_start(values["-REPO-"],ROOT)
    #elif event=='-COMMIT_MESSAGE-':
    elif event=='-PUSH-':
        git_operation.git_push(values["-REPO-"],ROOT,GITPATH,values["-COMMIT_MESSAGE-"],values["-CHANGE_BRANCH-"])
    elif event=='-CLEAR-':
        window['-OUTPUT-'].update('')    
    elif event=='-ABOUT-':
        window['-OUTPUT-'].update('')
        window['-OUTPUT-'].update("# GitSW\n# Github Client for Solidworks\n# Author : \ndhkima@higenmotor.com\n# Source : \nhttps://codeberg.org/dymaxionkim/gitsw\n# Mirror : \nhttps://github.com/dhkima-higenmotor/gitsw\n# Manual : \nhttps://codeberg.org/dymaxionkim/gitsw/src/branch/main/Manual")

window.close()
