import maya.cmds as cmds

def colorChanger():
    selection = cmds.ls(sl=True)
    if len(selection) <1:
        print("Select something")
    else:
        pickColor = int(input())
        for shape in selection:
            selectionShape = cmds.listRelatives(shape, s=True)
            cmds.setAttr(selectionShape[0]+ ".overrideEnabled", True)
            cmds.setAttr(selectionShape[0]+ ".overrideColor", pickColor)       
colorChanger()
