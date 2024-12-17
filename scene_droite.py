import pygame


class SceneDroite:

    def __init__(self,screen,game):

        self.game = game
        self.screen = screen
        self.screen_height = screen.get_height()
        self.origine = (self.screen_height,0)
        self.width = self.screen.get_width() - self.screen_height
        self.pos_blanc = (self.screen_height+((1/8)*self.width),self.screen_height/8)
        self.pos_noir = (self.screen_height+((5/8)*self.width),self.screen_height/8)
        self.timer_noir = 30*60
        self.timer_blanc = 30*60
        self.timer_noir_minute = ''
        self.timer_blanc_minute = ''
        self.coup_joue_blanc = []
        self.piece_blanc_manger = []
        self.coup_joue_noir = []
        self.piece_noir_manger = []
        self.font = pygame.font.Font('pieces_echecs/gau_font_cube/GAU_cube_B.TTF', self.width//14)

    def temp_blanc_reduction(self):
        self.timer_blanc -= 1

    def temp_noir_reduction(self):
        self.timer_noir -= 1

    def maj_temps_minute(self):
        self.timer_blanc_minute = str(self.timer_blanc//60)+':'+('0' if self.timer_blanc%60<10 else '') + str(self.timer_blanc%60)
        self.timer_noir_minute = str(self.timer_noir//60)+':'+('0' if self.timer_noir%60<10 else '') +str(self.timer_noir%60)

    def update(self):
        self.maj_temps_minute()
        text_blanc = self.timer_blanc_minute
        text_noir = self.timer_noir_minute
        self.screen.blit(self.font.render(text_blanc, True, (255,255,255)), self.pos_blanc)
        self.screen.blit(self.font.render(text_noir, True, (255, 255, 255)), self.pos_noir)

"""import pygame
pygame.init()
screen = pygame.display.set_mode((128, 128))
clock = pygame.time.Clock()

counter, text = 20, '10'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.USEREVENT:
            counter -= 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
    pygame.display.flip()
    clock.tick(60)"""