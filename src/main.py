'''
main.py

Owen Ziegler
15 Jan 2025

Description:
Game class, main driver of the program
'''
import pygame
from entity import Entity
from scene import Scene
from sceneManager import SceneManager
#constants
SCREENWIDTH = 640
SCREENHEIGHT = 480
FPS = 60

class Game:
    def __init__(self):
        #initialization
        pygame.init()
        self.window = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("sixshooter")
        #icon = pygame.image.load('imagepath') #fill in later
        #pygame.display.set_icon(icon)
        self.sceneManager = SceneManager('scene1')
        self.scene1 = Scene(self.window, self.sceneManager)
        self.scene1.setBackgroundColor((255,0,255))
        self.scene2 = Scene(self.window, self.sceneManager)
        self.scene2.setBackgroundColor((0,255,255))
        self.scenes = {'scene1':self.scene1, 'scene2':self.scene2}
        
    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.sceneManager.setCurrentScene('scene2')
                if event.type == pygame.KEYUP:
                    self.sceneManager.setCurrentScene('scene1')
            self.scenes[self.sceneManager.getCurrentScene()].draw()
            pygame.display.update()
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = Game()
    game.run()