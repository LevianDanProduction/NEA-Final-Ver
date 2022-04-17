import pygame
from displaych8 import Display
import opfinder, font, opdefiner
from chipCPU import CPU
import rom_loader
import keyboard_input

#If opening the emulator directly, it will use File Explorer to load code
f = open("settings.txt", "r")
read = f.read()
if str(read)== "1": 
    FileBrowser = 1
else:
    FileBrowser = 0

def loadGraphics():
    screen = Display()
    return screen

chip = CPU()
screen = 0
def mainLoad():
    global screen
    global clock
    screen = loadGraphics() # sets up the screen and input system
    #loadInput()
    chip.emulationInit() # starts up the emulator
    if FileBrowser == 1:
        rombyteform = rom_loader.LoadBrowse()
    else:
        rombyteform = rom_loader.LoadTemp("temp")
    chip.load_rom(rombyteform) # loads up game
    clock = pygame.time.Clock() #times everything 
    pygame.init()


def mainRun():
    chip.emulate_cycle() # FDE Cycle

mainLoad()

crashed = False


while not crashed:
    keyboard_input.handle_input(chip)#keyboard

    for _ in range(8): # is looped 8 times in order increase the display Hz to around 480 Hz -> 60fps * 8
        mainRun()

    chip.update_timers() #updates delay timers
    
    if chip.drawSwitch == True:
        chip.draw(screen) #redraws graphics when flag is true
                            
    #chip.setKeys() # stores key states

    clock.tick(60)

pygame.quit()
quit()    
        
"""
+---------------+= 0xFFF (4095) End of Chip-8 RAM
|               |
|               |
|               |
|               |
|               |
| 0x200 to 0xFFF|
|     Chip-8    |
| Program / Data|
|     Space     |
|               |
|               |
|               |
+- - - - - - - -+= 0x600 (1536) Start of ETI 660 Chip-8 programs
|               |
|               |
|               |
+---------------+= 0x200 (512) Start of most Chip-8 programs
| 0x000 to 0x1FF|5
| Reserved for  |
|  interpreter  |
+---------------+= 0x000 (0) Start of Chip-8 RAM

"""



