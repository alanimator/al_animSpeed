import maya.cmds as cmds
import maya.OpenMaya as om

'''
import animSpeed
animSpeed.startUI()
'''

class animSpeedUI(object):
    
    #constructor
    def __init__(self):
        self.window = "animSpeed"
        self.title = "AnimSpeed"
        
        
        #close old window is open
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window)
            
        #create new window
        self.window = cmds.window(self.window, title = self.title, width = 200, height=100,resizeToFitChildren=True)
        cmds.columnLayout(adjustableColumn = True)
        
        self.cubeCreateBtn = cmds.button(label = "0.5", command=self.slowSpeed)
        self.cubeCreateBtn = cmds.button(label = "1", command=self.normSpeed, bgc=(1, 1, 0))
        self.cubeCreateBtn = cmds.button(label = "2", command=self.fastSpeed)
        self.cubeCreateBtn = cmds.button(label = "4", command=self.quicklySpeed)
         
        cmds.showWindow()
        
    def slowSpeed(self, *args):
        cmds.playbackOptions(e=True, playbackSpeed=0, maxPlaybackSpeed=0.5, by=0.5)
        om.MGlobal.displayWarning("Playback speed set to 0.5")
    
    def normSpeed(self, *args):
        cmds.playbackOptions(e=True, playbackSpeed=1, maxPlaybackSpeed=1, by=1)
        om.MGlobal.displayWarning("Playback speed set to 1")
    
    def fastSpeed(self, *args):
        cmds.playbackOptions(e=True, playbackSpeed=2, maxPlaybackSpeed=2, by=2)
        om.MGlobal.displayWarning("Playback speed set to 2")
    
    def quicklySpeed(self, *args):
        cmds.playbackOptions(e=True, playbackSpeed=3, maxPlaybackSpeed=4, by=4)
        om.MGlobal.displayWarning("Playback speed set to 4")

def startUI():
    animSpeedUI()
