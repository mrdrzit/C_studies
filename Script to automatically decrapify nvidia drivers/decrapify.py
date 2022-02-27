import os
import shutil

foldersi = ["Display.Driver","Display.Nview","Display.Optimus","Display.Update","FrameViewSDK","GFExperience","GFExperience.NvStreamSrv","HDAudio","MSVCRT","nodejs","NvBackend","NvContainer","NVI2","NvModuleTracker","NVPCF","NvTelemetry","NvVAD","NvvHCI","PhysX","PPC","ShadowPlay","ShieldWirelessController","Update.Core"]

folders = ["Display.Nview","Display.Optimus","Display.Update","FrameViewSDK","GFExperience.NvStreamSrv","nodejs","NvBackend","NvContainer","NvModuleTracker","NVPCF","NvTelemetry","NvVAD","NvvHCI","PPC","ShadowPlay","ShieldWirelessController","Update.Core"]

path = os.getcwd()
dirs = os.listdir(path)

for folder in dirs:
    for key in foldersi:
        if key != folder:
            print("This version of the driver have additional folders, please change the list inside the script")
            exit()

for folder in dirs:
    for key in folders:
        if folder == key:
            shutil.rmtree(path, ignore_errors=False, onerror=None)