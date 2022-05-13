import pygame
import pygame_menu

pygame.init()
pygame.font.init()
font1 = pygame.font.Font(None, 35)
class GameSprite(pygame.sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(player_image), (wight, height)) #вместе 55,55 - параметры
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed


back = (200, 255, 255) 
win_width = 600
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
window.fill(back)

clock = pygame.time.Clock()
FPS = 60

racket1 = Player('900-9007408_manfred-scrat-woolly-mammoth-sid-ice-age-.png', 30, 200, 4, 50, 150)
racket2 = Player('900-9007408_manfred-scrat-woolly-mammoth-sid-ice-age-.png', 520, 200, 4, 50, 150)
ball = GameSprite('monkey-d-luffy-one-piece.png', 300, 250, 3, 110, 90)

lose1 = font1.render('Player 1 lose', True, (180, 0 , 0))
lose2 = font1.render('Player 2 lose', True, (180, 0 , 0))
def start_the_game():
    game = True
    finish = False
    score_p1 = 0
    score_p2 = 0
    score1 = font1.render(str(score_p1), True, (180, 0 , 0))
    score2 = font1.render(str(score_p2), True, (180, 0 , 0))
    speed_x = 4
    speed_y = 4
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game = False
        if finish != True:
            window.fill(back)
            window.blit(score1, (80,50))     
            window.blit(score2, (500,50)) 
            racket1.reset()
            racket2.reset()
            ball.reset()
            racket1.update_l()
            racket2.update_r()
            ball.rect.x += speed_x
            ball.rect.y += speed_y
            if pygame.sprite.collide_rect(racket1, ball) or pygame.sprite.collide_rect(racket2, ball):
                speed_x *= -1
            if ball.rect.y > win_height - 50 or ball.rect.y < 0:
                speed_y *= -1
            if ball.rect.x < 0:
                ball.rect.x, ball.rect.y = 300, 250
                speed_x *= -1
                speed_y *= -1
                score_p2 += 1
                score2 = font1.render(str(score_p2), True, (180, 0 , 0))
                #window.blit(lose1, (200, 200))
            if ball.rect.x > win_width:
                ball.rect.x, ball.rect.y = 300, 250
                speed_x *= -1
                speed_y *= -1
                score_p1 += 1
                score1 = font1.render(str(score_p1), True, (180, 0 , 0))
                #window.blit(lose2, (200, 200))
            if score_p1 == 6:
                finish = True
                window.blit(lose2, (200, 200))
            if score_p2 == 6:
                finish = True
                window.blit(lose1, (200, 200))
        pygame.display.update()
        clock.tick(FPS)
def menu():
    menu = pygame_menu.Menu('Welcome', 600, 500,
                       theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(window)
menu()