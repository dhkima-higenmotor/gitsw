import PySimpleGUI as sg
import os

# Internal functions
import git_operation

# Theme
sg.theme(git_operation.read_config('theme')[0])
sg.set_options(font=git_operation.read_config('font')[0])

# Config
NAME_SIZE = 17
BUTTON_WIDTH = 8
INPUT_WIDTH = 40
OUTPUT_WIDTH = 60
LIST_MODE = git_operation.read_config('modes')
LIST_USERS = git_operation.read_config('users')
LIST_ORGANS = git_operation.read_config('organs')
LIST_ORGANS.extend(LIST_USERS)
LIST_REPOS = git_operation.read_config('repos')
LIST_BRANCH = LIST_USERS.copy()
LIST_BRANCH.insert(0,'main')
LIST_COMMIT = git_operation.read_config('commits')
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
    [name('1.MODE'), sg.Combo(values=LIST_MODE,default_value=LIST_MODE[0],size=(INPUT_WIDTH,1),key='-MODE-',enable_events=True)],
    [name('2.USER'), sg.Combo(values=LIST_USERS,default_value=LIST_USERS[0],size=(INPUT_WIDTH,1),key='-USER-',enable_events=True)],
    [name('3.ORGANIZATION'), sg.Combo(values=LIST_ORGANS,default_value=LIST_ORGANS[0],size=(INPUT_WIDTH,1),key='-ORGAN-',enable_events=True)],
    [name('4.REPOSITORY'), sg.Combo(values=LIST_REPOS,default_value=LIST_REPOS[0],size=(INPUT_WIDTH,1),key='-REPO-',enable_events=True)],
    [name(''), sg.Button('MAKE',key='-MAKE-',size=(BUTTON_WIDTH,1)), sg.Button('CLONE',key='-CLONE-',size=(BUTTON_WIDTH,1)), sg.Button('PULL',key='-PULL-',size=(BUTTON_WIDTH,1))],
    [name('5.BRANCH'), sg.Combo(values=LIST_BRANCH,default_value=LIST_BRANCH[0],size=(INPUT_WIDTH,1),key='-CHANGE_BRANCH-',enable_events=True)],
    [name('6.MERGE'), sg.Combo(values=LIST_BRANCH,default_value=LIST_BRANCH[1],size=(INPUT_WIDTH,1),key='-CHANGE_MERGE-',enable_events=True)],
    [name(''), sg.Button('MERGE',key='-MERGE-',size=(BUTTON_WIDTH,1))],
    [name('7.LOCK'), sg.Button('LOCK',key='-LOCK-',size=(BUTTON_WIDTH,1)), sg.Button('UNLOCK',key='-UNLOCK-',size=(BUTTON_WIDTH,1))],
    [name('8.SOLIDWORKS'), sg.Button('START',key='-START-',size=(BUTTON_WIDTH,1))],
    [name('9.ADD'), sg.Button('ADD',key='-ADD-',size=(BUTTON_WIDTH,1)), sg.Button('ADD_ALL',key='-ADD_ALL-',size=(BUTTON_WIDTH,1))],
    [name('10.COMMIT+PUSH'), sg.Combo(values=LIST_COMMIT,default_value=LIST_COMMIT[0],size=(INPUT_WIDTH,1),key='-COMMIT_MESSAGE-',enable_events=True)],
    [name(''), sg.Button('COMMIT',key='-COMMIT-',size=(BUTTON_WIDTH,1)), sg.Button('PUSH',key='-PUSH-',size=(BUTTON_WIDTH,1))]
]

right_column = [
    [name('11.OUTPUT')],
    [sg.Output(key='-OUTPUT-',size=(OUTPUT_WIDTH,19))],
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
    elif event=='-MODE-':
        print(values)
    elif event=='-USER-':
        print(values)
    elif event=='-ORGAN-':
        print(values)
    elif event=='-REPO-':
        print(values)
    elif event=='-MAKE-':
        git_operation.git_make(SERVER,values["-ORGAN-"],values["-REPO-"],values["-USER-"],TOKEN,ROOT,GITPATH,EXEPATH)
    elif event=='-CLONE-':
        git_operation.git_clone(SERVER,values["-ORGAN-"],values["-REPO-"],values["-USER-"],TOKEN,ROOT,GITPATH)
    elif event=='-PULL-':
        git_operation.git_pull(values["-REPO-"],ROOT,GITPATH)
    elif event=='-CHANGE_BRANCH-':
        print(values)
    elif event=='-CHANGE_MERGE-':
        print(values)
    elif event=='-MERGE-':
        print(values)
    elif event=='-LOCK-':
        print(values)
    elif event=='-UNLOCK-':
        print(values)
    elif event=='-START-':
        print(values)
    elif event=='-ADD-':
        print(values)
    elif event=='-ADD_ALL-':
        print(values)
    elif event=='-COMMIT_MESSAGE-':
        print(values)
    elif event=='-COMMIT-':
        print(values)
    elif event=='-PUSH-':
        print(values)
    elif event=='-CLEAR-':
        window['-OUTPUT-'].update('')    
    elif event=='-ABOUT-':
        print('\n# event = ABOUT')
        sg.popup('GitSW V01', 'Author : dhkima@higenmotor.com', 'Source : https://codeberg.org/dymaxionkim/gitsw')

window.close()
