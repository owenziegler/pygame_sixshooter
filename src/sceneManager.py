'''
sceneManager.py

Owen Ziegler
18 January 2025

Description:
Scene manager class. Holds the value of the current scene being displayed.
'''

class SceneManager:
    def __init__(self, initialScene):
        self.currentScene = initialScene
    
    def getCurrentScene(self):
        return self.currentScene
    
    def setCurrentScene(self, newScene):
        self.currentScene = newScene