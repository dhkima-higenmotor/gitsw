import win32com.client
import pythoncom
import re

working_dir = "D:\\github\\EMS\\3D"
assy_name = "EMS5"
sldasm_name = working_dir+"\\"+assy_name+".SLDASM"

# Connect to SolidWorks
swApp = win32com.client.Dispatch("SldWorks.Application")

# Open the assembly file
# Method 1
f = swApp.getopendocspec(sldasm_name)
assembly = swApp.opendoc7(f)
# Method 2
#openDoc     = swApp.OpenDoc6;
#arg1        = win32com.client.VARIANT(pythoncom.VT_BSTR, sldasm_name);
#arg2        = win32com.client.VARIANT(pythoncom.VT_I4, 2);
#arg3        = win32com.client.VARIANT(pythoncom.VT_I4, 1);
#arg5        = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 2);
#arg6        = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 128);
#assembly = openDoc(arg1, arg2, arg3, "", arg5, arg6);

# Get the assembly tree root component
rootComponent = assembly.GetActiveConfiguration.GetRootComponent3(True)




"""
# Create a new Excel workbook
excelApp = win32com.client.Dispatch("Excel.Application")

workbook = excelApp.Workbooks.Add() #엑셀 프로그램에 Workbook 추가(객체 설정)
worksheet = workbook.Worksheets("sheet1") #Worksheet 설정

# Write the assembly tree data to the Excel worksheet
row = 1
def write_component(component, level):
    global row
    comp1 = component.Name2
    comp1 = re.sub(r'-[0-999]','',comp1)
    comp2 = comp1.split('/')
    print(comp2)
    level3 = level
    for comp3 in comp2:
        worksheet.Cells(row, level3+1).Value = comp3
        level3 += 1
    row += 1
    for child in component.GetChildren:
        ##write_component(child, level+1)
        write_component(child, level)

write_component(rootComponent, 0)

# Save the Excel file
#workbook.SaveAs(working_dir+"\\"+assy_name+"_BOM.xlsx")
workbook.SaveAs(working_dir+"\\"+assy_name+"_BOM",6)

# Close Excel
excelApp.Quit()
"""


# List
LIST_COMPONENT = []
row = 1
def list_component(component):
    global LIST_COMPONENT
    global row
    comp1 = component.Name2
    comp1 = re.sub(r'-[0-999]','',comp1)
    comp2 = comp1.split('/')
    LIST_COMPONENT.append(comp2)
    row += 1
    for child in component.GetChildren:
        list_component(child)

list_component(rootComponent)
print(LIST_COMPONENT)


# Close SW
swApp.ExitApp()

