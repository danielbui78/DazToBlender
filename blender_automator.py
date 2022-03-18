import bpy
import os
import DTB
import json
from DTB import Environment

def main():
    DTB.Global.bNonInteractiveMode = 1;
    sDtuFolderPath = "c:/BridgeOutput/Product_80857/";
    sDtuFilenamePath = os.path.join(sDtuFolderPath, "KentHair.dtu");

    oDtu = DTB.DataBase.DtuLoader();
    with open(sDtuFilenamePath, "r") as data:
        oDtu.dtu_dict = json.load(data)
    
    DTB.Global.clear_variables()
    DTB.Global.setHomeTown(sDtuFolderPath)
    DTB.Global.load_asset_name()
    DTB.Util.decideCurrentCollection('ENV')

    DTB.Environment.ReadFbx(sDtuFilenamePath, 0, 0, oDtu)
    print("Test complete.")

main();
