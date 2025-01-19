'''
scene.py

Owen Ziegler
16 Jan 2025

Description:
General class for all Scenes (menu, settings, duel, pre-duel, results, etc.) to use.
Contains all the entities on a given scene, and manages their event handling.

Each Scene has three layers: background fill color, image, and entity. Entities are held in the self.entities array, and are drawn in index-ascending order. The last entity in the array will be on top.
'''
import pygame
import entity

class Scene:
    def __init__(self,window, sceneManager):
        self.window = window
        self.color = None
        self.image = None
        self.sceneManager = sceneManager
        self.bounds = pygame.Rect(0,0,window.get_width(),window.get_height())
        self.colorLayer = pygame.Surface((self.bounds.width,self.bounds.height))
        self.imageLayer = pygame.Surface((self.bounds.width,self.bounds.height))
        #self.entityLayer = pygame.Surface((self.bounds.width,self.bounds.height), pygame.SRCALPHA) #not currently used. Entity layers and HUD layers may come later, or in child classes.
        #self.entityLayer.set_alpha(0)
        self.entities = []

    #draw function
    def draw(self):
        #draw background stuff first
        if self.color: #only draw if color != None
            self.window.blit(self.colorLayer, self.bounds)
        if self.image: #only draw if image != None
            self.window.blit(self.imageLayer, self.bounds)
        #draw entities
        for entity in self.entities:
            entity.draw(self.window)

    #add entity
    def addEntity(self, entity, index=None):
        if not index: #if no index, append
            self.entities.append(entity)
        elif index < 0 or index > len(self.entities): #if invalid index, append
            self.entities.append(entity)
        else: #otherwise, insert entity at specified index
            self.entities.insert(index, entity)

    #delete entity
    def deleteEntity(self, index):
        if index < 0 or index >= len(self.entities): #if invalid index, return -1
            return -1
        else:
            self.entities.pop(index)

    #setters
    def setBackgroundColor(self, color):
        self.color = color
        self.colorLayer.fill(color)

    def setBackgroundImage(self, image):
        self.image = image
        self.imageLayer = pygame.transform.scale(pygame.image.load(image),(self.bounds.width, self.bounds.height))

    #getters
    def getBackroundColor(self):
        return self.color
    
    def getBackgroundImage(self):
        return self.image
    
    def getColorLayerAlpha(self):
        return self.colorLayer.get_alpha()
    
    def getImageLayerAlpha(self):
        return self.imageLayer.get_alpha
    
    def getEntity(self, index): #get a specific entity
        if index < 0 or index >= len(self.entities):
            return -1 #invalid index
        else:
            return self.entities[index]

    def getEntityList(self): #get all entities in a list
        return self.entities
    
    def getEntityCount(self): #get a count of all entities in the screen
        return len(self.entities)