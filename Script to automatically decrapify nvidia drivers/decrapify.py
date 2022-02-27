import os
import shutil

default_folders = ["Display.Driver","Display.Nview","Display.Optimus","Display.Update","FrameViewSDK","GFExperience","GFExperience.NvStreamSrv","HDAudio","MSVCRT","nodejs","NvBackend","NvContainer","NVI2","NvModuleTracker","NVPCF","NvTelemetry","NvVAD","NvvHCI","PhysX","PPC","ShadowPlay","ShieldWirelessController","Update.Core","decrapify.py","EULA.txt","ListDevices.txt","setup.cfg","setup.exe"]
folders = ["Display.Nview","Display.Optimus","Display.Update","FrameViewSDK","GFExperience.NvStreamSrv","nodejs","NvBackend","NvContainer","NvModuleTracker","NVPCF","NvTelemetry","NvVAD","NvvHCI","PPC","ShadowPlay","ShieldWirelessController","Update.Core"]

path = os.getcwd()
dirs = os.listdir(path)

if len(default_folders) != len(dirs):
    print("This version of the driver have additional folders, please change the list inside the script")
    exit()

for folder in dirs:
    for key in folders:
        if folder == key:
            path_current = path+"\\"+key
            shutil.rmtree(path_current, ignore_errors=False, onerror=None)