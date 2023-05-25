import PySimpleGUI as sg
import csv
import mysw

# Get BOM
ASSY = mysw.assy("D:\\git\\ARES-P", "ARES-P05", [], 1)
BOM = ASSY.getBOM()
#print(BOM)

# Save csv
with open('mysw_test.csv', 'w', newline='') as f:
    write = csv.writer(f) 
    write.writerows(BOM)

# Table GUI
sg.set_options(font=("D2Coding",12))
BOM = ASSY.readBOM("mysw_test.csv")

toprow = ['0','1','2','3','4'.'5'.'6'.'7'.'8'.'9']
tbl1 = sg.Table(values=BOM,
    headings=toprow,
    auto_size_columns=True,
    display_row_numbers=True,
    justification='left', key='-TABLE-',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)

layout = [[tbl1],
          [sg.Button('CLICK',key='-CLICK-')]]
window = sg.Window("Table Demo", layout, size=(800,600), resizable=True)

while True:
    event, values = window.read()
    print("event:", event, "values:", values)
    if event == sg.WIN_CLOSED:
        break
    elif '+CLICKED+' in event:
        pass
    elif event=='-CLICK-':
        sg.popup(f"{values['-TABLE-']}")

window.close()