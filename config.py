import PySimpleGUI as sg
import os

# Internal functions
import git_operation

# Config
NAME_SIZE = 16
BUTTON_WIDTH = 12
INPUT_WIDTH = 27
OUTPUT_WIDTH = 40
OUTPUT_HEIGHT = 15

LIST_COMMIT = git_operation.read_config('list_commit')
FONT = git_operation.read_config('font')[0]
GITPATH = git_operation.read_config('gitpath')[0]
LIST_ORGANS = git_operation.read_config('list_organs')
LIST_REPOS = git_operation.read_config('list_repos')
ROOT = git_operation.read_config('root')[0]
SERVER = git_operation.read_config('server')[0]
THEME = git_operation.read_config('theme')[0]
TOKEN = git_operation.read_config('token')[0]
LIST_USERS = git_operation.read_config('list_users')

# Theme
sg.theme(THEME)
sg.set_options(font=FONT)

# GUI Name Width
def name(name):
    dots = NAME_SIZE-len(name)-2
    return sg.Text(name+' '*dots,size=(NAME_SIZE,1),justification='r',pad=(0,0))

# Read and Display OUTPUT
def display(file_name):
    if os.path.isfile(".\\Config\\"+file_name):
        with open('.\\Config\\'+file_name,'r') as f:
            lines = f.read()
        f.close()
        window['-OUTPUT-'].update(lines)
        return 0
    else:
        window['-OUTPUT-'].update("")
        return -1
 
# Save Config
def save_config():
    for i in ["-FONT-", "-GITPATH-", "-ROOT-", "-SERVER-", "-THEME-", "-TOKEN-", "-LIST_COMMIT-", "-LIST_ORGANS-", "-LIST_REPOS-", "-LIST_USERS-"]:
        if values[i] == True:
            file_name = i
            file_name = file_name.strip("-")
            file_name = file_name.lower()
            f = open('.\\Config\\'+file_name,'w')
            f.write(values["-OUTPUT-"])
            f.close()
    return 0

# GUI Layout
left_column = [
    [sg.Radio('FONT',1,key="-FONT-",enable_events=True,default=True)],
    [sg.Radio('GITPATH',1,key="-GITPATH-",enable_events=True)],
    [sg.Radio('ROOT',1,key="-ROOT-",enable_events=True)],
    [sg.Radio('SERVER',1,key="-SERVER-",enable_events=True)],
    [sg.Radio('THEME',1,key="-THEME-",enable_events=True)],
    [sg.Radio('TOKEN',1,key="-TOKEN-",enable_events=True)],
    [sg.Radio('LIST_USERS',1,key="-LIST_USERS-",enable_events=True)],
    [sg.Radio('LIST_COMMIT',1,key="-LIST_COMMIT-",enable_events=True)],
    [sg.Radio('LIST_ORGANS',1,key="-LIST_ORGANS-",enable_events=True)],
    [sg.Radio('LIST_REPOS',1,key="-LIST_REPOS-",enable_events=True)]
]

right_column = [
    [sg.Multiline(default_text=FONT,key='-OUTPUT-',size=(OUTPUT_WIDTH,OUTPUT_HEIGHT))],
    [sg.Button('SAVE',key='-SAVE-',size=(BUTTON_WIDTH,1)), sg.Button('EXIT',key='-EXIT-',size=(BUTTON_WIDTH,1))]
]

layout = [
    [
        sg.Column(left_column),
        sg.VSeperator(),
        sg.Column(right_column)
    ]
]

window = sg.Window('GitSW - Config', layout)

while True:
    event, values = window.read() 
    if event==sg.WIN_CLOSED or event=='-EXIT-':
        break
    elif event=='-FONT-':
        display('font')
    elif event=='-GITPATH-':
        display('gitpath')
    elif event=='-ROOT-':
        display('root')
    elif event=='-SERVER-':
        display('server')
    elif event=='-THEME-':
        display('theme')
    elif event=='-TOKEN-':
        display('token')
    elif event=='-LIST_COMMIT-':
        display('list_commit')
    elif event=='-LIST_USERS-':
        display('list_users')
    elif event=='-LIST_ORGANS-':
        display('list_organs')
    elif event=='-LIST_REPOS-':
        #display('list_repos')
        window['-OUTPUT-'].update("wgfwergfew????????????????")
    elif event=='-SAVE-':
        save_config()

window.close()
