import maya.cmds as cmds

def renameTool():
        selection = cmds.ls(sl=True)
        if len(selection) <= 0:
           cmds.error("no selection")
        else:
           selectionInput = input("Name_##_Type")
           count = selectionInput.count("#")
           selectionPartition = selectionInput.partition(count * '#')
           for i in range(len(selection)):
               new_name = selectionPartition[0] + str(i+1).zfill(count) + selectionPartition[2]
               cmds.rename(selection[i],new_name)
               
renameTool()
