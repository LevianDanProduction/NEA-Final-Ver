import pygame
from displaych8 import Display
import opfinder, font, opdefiner



"""
0x000-0x1FF - Chip 8 interpreter (contains font set in emu)
0x050-0x0A0 - Used for the built in 4x5 pixel font set (0-F)
0x200-0xFFF - Program ROM and work RAM
"""

class CPU(): #will handle everything

    START_ADDRESS =0x200
    
    WORD_SIZE_IN_BYTES = 2
    ARITHMETIC_FLAG_REGISTER_ADDRESS = 0xF
    FRAME_BUFFER_WIDTH = 64
    FRAME_BUFFER_HEIGHT = 32
    
    def __init__(self):
        self.ram = [0]*4096 # the one and only memory in bytes (4KB)
        self.V = [0]*16 # general registers
        self.delayTimer = 0 # timer
        self.soundTimer = 0 # buzz sound timer
        self.stack = [] # instruction stack
        self.keys = set()# keyboard states logger
        self.chipFont = []
        self.drawSwitch = False
        
    
    def emulationInit(self): #starts up registers/memory
        self.pc = 0x200 #program counter
        self.opcode = 0 # opcode
        self.I = 0 # index register
        self.sp = 0 # stack pointer
        #self.coderunner = op.FDEOP()

        self.ci = None #current instruction
        self.cw = 0 #current word
        self.screenbuffer = [[bool()] * 32 for i in range(64)]
        

        self._load_font()

        
        
    def emulate(self): #the cycle FDE and timer
        self.coderunner.feDeEx( self.ram, self.pc, self.opcode, self.I)
        #print("MEMMMMMMMORRRRRY")
        #print(self.ram)

    def load(self,rom,bufferSize): #loads game/rom into memory
        self.buffer = 0
        for i in range(bufferSize-1):
            self.ram[i + 512] = self.buffer[i]
        #nt("MEMMMMMMMORRRRRY")
        #print(self.ram)

    def draw(self,screen):
        """self.screenbuffer = screen.gridImage"""
        screen.update(self.screenbuffer) 
        self.drawSwitch = False



    def key_down(self, key):
        #This method sets a key as pressed
        if key not in self.keys:
            self.keys.add(key)
 
    def key_up(self, key):
        #This method sets a key as released
        if key in self.keys:
            self.keys.remove(key)
 
    def move_to_next_instruction(self):
        #this method will move the program counter forward to the next instruction
        self.pc += CPU.WORD_SIZE_IN_BYTES
 
    def move_to_previous_instruction(self):
        #this method will move the program counter backward to the previous instruction
        self.pc -= CPU.WORD_SIZE_IN_BYTES
 
    def load_rom(self, rom_bytes):
        #this will load rom bytes into main memory/RAM
        for i, byte_value in enumerate(rom_bytes):
            self.ram[CPU.START_ADDRESS + i] = byte_value
        #print("MEMMMMMMMORRRRRY")
        #print(self.ram)
 
    def set_arithmetic_flag(self):
        #this method will set the arithmetic flag to 1
        self.V[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 1
 
    def clear_arithmetic_flag(self):
        #this method will set the arithmetic flag to 0
        self.V[self.ARITHMETIC_FLAG_REGISTER_ADDRESS] = 0
 
    def emulate_cycle(self):
        #this method will run one cpu cycle
        self.cw = self.fetch_word()
        #if self.cw == 0:
        #   self.cw = 224
 
        opcode_ = opdefiner.Opcode(self.cw)
        self.opcode = opfinder.find_operation(self.cw)
 
        self.move_to_next_instruction()
        self.opcode(opcode_, self)
        #print("MEMMMMMMMORRRRRY")
        #print(self.ram)
 
    def fetch_word(self):
        #this method will load the next two bytes of ram into one 16 bit value - the current opcode
        word = self.ram[self.pc] << 8 | self.ram[self.pc + 1]
        #print ("word: ", word)
        return word
 
    def update_timers(self):
        #this method will decrement any timers that are above 0 by 1
        if self.delayTimer > 0:
            self.delayTimer -= 1
 
    def _load_font(self):
        #this method loads the font data into main memory/RAM
        offset = 0x0
        for item in font.DATA:
            self.ram[offset] = item
            offset += 1

    def showStats(self):
        print("Program Counter: ", self.pc)
        for i in range(15):
            print(("V"+str(i)),":", self.V[i])
        print("currentStack: ", self.stack)
        print("CurrentOpcode: ", self.opcode)
        print("CurrentInstruction: ", self.ci)
        print("CurrentWord: ",self.cw)
        print("IndexRegister: ", self.I)
        print("StackPointer: ",self.sp)
        



"""

        

def loadGraphics():
    screen = Display()
    return screen

chip = CPU()

def mainLoad():
    global screen
    global clock
    screen = loadGraphics() # sets up the screen and input system
    #loadInput()
    chip.emulationInit() # starts up the emulator
    chip.load("example",0) # loads up game
    clock = pygame.time.Clock() #times everything 
    pygame.init()


def mainRun():
    chip.emulate_cycle() # FDE Cycle

mainLoad()

crashed = False




while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)
    for _ in range(8): # is looped 8 times in order increase the display Hz to around 480 Hz -> 60fps * 8
        mainRun()

    #soon to add update to delay timers 
    
    if chip.drawSwitch == True:
        chip.draw() # redraws graphics when flag is true
    #chip.setKeys() # stores key states

    clock.tick(60)

pygame.quit()
quit()    
        

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
| 0x000 to 0x1FF|
| Reserved for  |
|  interpreter  |
+---------------+= 0x000 (0) Start of Chip-8 RAM








"""

