import win32com.client
import pythoncom
import re
import csv

class assy:
    def __init__(self, assyfiledir, assyfilename, list_component, row):
        self.assyfiledir = "D:\\github\\EMS\\3D"
        self.assyfilename = "EMS5"
        self.list_component = []
        self.row = 1

    def listComponent(self, component):
        comp1 = component.Name2
        comp1 = re.sub(r'-[0-9]*','',comp1)
        comp2 = comp1.split('/')
        self.list_component.append(comp2)
        self.row += 1
        for child in component.GetChildren:
            assy.listComponent(self, child)
        
    def getBOM(self):
        sldasm_name = f"{self.assyfiledir}\\{self.assyfilename}.SLDASM"
        # Connect to SolidWorks
        swApp = win32com.client.Dispatch("SldWorks.Application")
        # Open the assembly file
        f = swApp.getopendocspec(sldasm_name)
        assembly = swApp.opendoc7(f)
        # Get the assembly tree root component
        rootComponent = assembly.GetActiveConfiguration.GetRootComponent3(True)
        # Listing
        assy.listComponent(self, rootComponent)
        #print(list_component)
        # Close SW
        swApp.ExitApp()
        return self.list_component
    
    def readBOM(self, csvfile):
        data = list()
        f = open(csvfile,'r')
        rea = csv.reader(f)
        for row in rea:
            data.append(row)
        f.close
        return data