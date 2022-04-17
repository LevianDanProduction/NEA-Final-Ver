import pygame



class Display():



    def __init__(self):
        self.displayWidth = 512
        self.displayHeight = 256
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.numRow = 32
        self.numCol = 64
        self.size = 16

        self.basicX = self.displayWidth / self.numCol
        self.basicY = self.displayHeight / self.numRow
        self.gameDisplay = pygame.display.set_mode((self.displayWidth,self.displayHeight))
        pygame.display.set_caption('Chip 8')

        self.gridImage = [[0 for x in range(self.numRow)] for y in range(self.numCol)]

    def drawScreen(self,screen, grid, basicX, basicY):  # draw rectangles from grid array
        for i in range(self.numRow):
            for j in range(self.numCol):
                if grid[j][i]:
                    pygame.draw.rect(screen, (255, 255, 255), (j * basicX, i * basicY, basicX, basicY))

    def update(self,newScreen):
        self.gameDisplay.fill(self.black)
        self.drawScreen(self.gameDisplay, newScreen, self.basicX, self.basicY)
        pygame.display.flip()

    

def createDisplay():
    return Display()



