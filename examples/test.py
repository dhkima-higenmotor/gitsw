import PySimpleGUI as sg
import subprocess as sp

sg.set_options(font=('Noto Sans CJK KR', 12))
sg.theme("DarkBlue3")

layout = [
[sg.Multiline(default_text="메시지 표시",key="-TEXT-",size=(80,20),font=("D2Coding",10))],
[sg.Input(".",key="-INPUT-"), sg.FolderBrowse()],
[sg.Button("Subprocess",key="-SUB-"), sg.Button("Clear",key="-CLEAR-")]
]

window = sg.Window('Title', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "-SUB-":
        location = values["-INPUT-"]
        cmd = "dir /OG "+location.replace("/","\\")
        print(cmd)
        temp = sp.Popen(cmd, stdout=sp.PIPE, shell=True)
        data = temp.stdout.read().decode('EUC-KR')
        #print(data)
        window['-TEXT-'].update(data)
    elif event == "-CLEAR-":
        temp = sp.call("cls", shell=True)
        window['-TEXT-'].update("")
        #print(event, values)

window.close()
