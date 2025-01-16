'''
entity.py

Owen Ziegler
16 Jan 2025

Description:
General-use Entity class, extensible for any non-static or interactable screen element.
No event handling included.
Three layers: background color, image, text, drawn in that order.
'''
import pygame

class Entity():
    def __init__(self, width, height, left, top, font=None, text=None, textColor=None, image=None, color=None):
        #rectangle setup
        self.bounds = pygame.Rect(width,height,left,top)
        #text layer setup
        self.font = pygame.font.Font(font)
        self.text = text
        self.textColor = textColor
        self.textLayer = pygame.Surface((width,height))
        if text:
            self.textLayer = self.font.render(text,True,self.textColor)
        else:
            self.textLayer.set_alpha(0)
        #image layer setup
        self.image = image #source location of image, encoded as string
        self.imageLayer = pygame.Surface((width,height))
        if image:
            self.imageLayer = pygame.transform.scale(pygame.image.load(image), (self.bounds.width, self.bounds.height))
        else:
            self.imageLayer.set_alpha(0)
        #color layer setup
        self.color = color
        self.colorLayer = pygame.Surface((width,height))
        if color:
            self.colorLayer.fill(color)
        else:
            self.colorLayer.set_alpha(0)

    #draw
    def draw(self, screen):
        screen.blit(self.colorLayer, self.bounds)
        screen.blit(self.imageLayer, self.bounds)
        screen.blit(self.textLayer, self.bounds)

    #handle events
    def event(self, event):
        print(event.type)
        return
    
    #getters
    def getWidth(self):
        return self.bounds.width
    
    def getHeight(self):
        return self.bounds.width

    def getLeft(self):
        return self.bounds.left

    def getTop(self):
        return self.bounds.top
    
    def getText(self):
        return self.text
    
    def getTextColor(self):
        return self.textColor
    
    def getImage(self):
        return self.image
    
    def getColor(self):
        return self.color
    
    #setters
    def setText(self, text):
        self.text = text
        self.textLayer = self.font.render(text, True, self.textColor)

    def setTextColor(self, textColor):
        self.textColor = textColor
        self.textLayer = self.font.render(self.text, True, textColor)
    
    def setTextLayerAlpha(self, alpha):
        self.textLayer.set_alpha(alpha)

    def setImage(self, image): #implement error handling later
        self.image = image
        self.imageLayer = pygame.image.load(image)
    
    def setImageLayerAlpha(self, alpha):
        self.imageLayer.set_alpha(alpha)

    def setColor(self, color):
        self.color = color
        self.colorLayer.fill(color)

    def setColorLayerAlpha(self, alpha):
        self.imageLayer.set_alpha(alpha)

    def resize(self, width, height):
        self.setWidth(width)
        self.setHeight(height)

    def translate(self, left, top):
        self.setLeft(left)
        self.setTop(top)

    def setWidth(self, width):
        self.bounds.width = width
        self.textLayer = pygame.transform.scale(self.textLayer, (self.bounds.width, self.bounds.height))
        self.imageLayer = pygame.transform.scale(self.imageLayer, (self.bounds.width, self.bounds.height))
        self.colorLayer = pygame.transform.scale(self.colorLayer, (self.bounds.width, self.bounds.height))

    def setHeight(self, height):
        self.bounds.height = height
        self.textLayer = pygame.transform.scale(self.textLayer, (self.bounds.width, self.bounds.height))
        self.imageLayer = pygame.transform.scale(self.imageLayer, (self.bounds.width, self.bounds.height))
        self.colorLayer = pygame.transform.scale(self.colorLayer, (self.bounds.width, self.bounds.height))

    def setLeft(self,left):
        self.bounds.left = left

    def setTop(self, top):
        self.bounds.top = top
