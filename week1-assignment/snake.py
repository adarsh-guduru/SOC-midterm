import pygame, random
from pygame.math import Vector2

class Fruit():
    def __init__(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x,self.y)
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x*cell_size),int(self.pos.y*cell_size),cell_size,cell_size)
        screen.blit(apple, fruit_rect)
    
    def reposition(self):
        self.x = random.randint(0, cell_number-1)
        self.y = random.randint(0, cell_number-1)
        self.pos = Vector2(self.x,self.y)

class Snake():
    def __init__(self):
        self.body = [Vector2(9,10),Vector2(8,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
        self.change = False
    
        self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()
        self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()   
        self.tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha() 
        self.tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()   
        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()  
        self.body_topleft = pygame.image.load("Graphics/body_topleft.png").convert_alpha()     
        self.body_topright = pygame.image.load("Graphics/body_topright.png").convert_alpha() 
        self.body_bottomright = pygame.image.load("Graphics/body_bottomright.png").convert_alpha() 
        self.body_bottomleft = pygame.image.load("Graphics/body_bottomleft.png").convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('sound/crunch.mp3')

    def move_snake(self):
        if not self.change:
            new_body = self.body[:-1]
            new_body.insert(0,self.body[0]+self.direction)
            self.body = new_body
        else:
            new_body = self.body[:]
            new_body.insert(0,self.body[0]+self.direction)
            self.body = new_body
            self.change = False

    def draw_snake(self):
        self.snake_head_update()

        for index,block in enumerate(self.body):
            snake_part = pygame.Rect(int(block.x * cell_size),int(block.y*cell_size),cell_size,cell_size)
            if index == 0:
                screen.blit(self.head,snake_part)

            elif 0< index< len(self.body)-1:
                prev_pos = self.body[index-1] - block
                next_pos = self.body[index+1] - block
                if prev_pos == (-1,0):
                    if next_pos == (1,0):
                        screen.blit(self.body_horizontal,snake_part)
                    elif next_pos == (0,-1):
                        screen.blit(self.body_topleft,snake_part)
                    else:
                        screen.blit(self.body_bottomleft,snake_part)
                elif prev_pos == (1,0):
                    if next_pos == (-1,0):
                        screen.blit(self.body_horizontal,snake_part)
                    elif next_pos == (0,-1):
                        screen.blit(self.body_topright,snake_part)
                    else:
                        screen.blit(self.body_bottomright,snake_part)
                elif prev_pos == (0,1):
                    if next_pos == (1,0):
                        screen.blit(self.body_bottomright,snake_part)
                    elif next_pos == (0,-1):
                        screen.blit(self.body_vertical,snake_part)
                    else:
                        screen.blit(self.body_bottomleft,snake_part)
                else:
                    if next_pos == (1,0):
                        screen.blit(self.body_topright,snake_part)
                    elif next_pos == (0,1):
                        screen.blit(self.body_vertical,snake_part)
                    else:
                        screen.blit(self.body_topleft,snake_part)
            else:
                self.tail_pos = self.body[-1] - self.body[-2]
                if self.tail_pos == (1,0):
                    screen.blit(self.tail_right,snake_part)
                elif self.tail_pos == (-1,0):
                    screen.blit(self.tail_left,snake_part)
                elif self.tail_pos == (0,1):
                    screen.blit(self.tail_down,snake_part)
                else:
                    screen.blit(self.tail_up,snake_part)

    def snake_head_update(self):
        self.head_pos = self.body[0] - self.body[1]
        if self.head_pos == (1,0):
            self.head = self.head_right
        elif self.head_pos == (-1,0):
            self.head = self.head_left
        elif self.head_pos == (0,1):
            self.head = self.head_down
        else:
            self.head = self.head_up

    def reset(self):
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(1,0)

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def update_body(self):
        self.change = True

class Button():
    def __init__(self,x,y,image,scale):
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(image, (int(w*scale),int(h*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image,(self.rect.x,self.rect.y))
        return action

class Main_game():
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.run = True
        self.highscore = 0
        self.score = 0
        self.playing = False
        self.start_btn = Button(350,100,start_img,0.8)
        self.exit_btn = Button(350,600,exit_img,0.8)
    
    def draw_element(self):
        if self.playing:
            self.draw_grass()
            self.draw_score()
            self.fruit.draw_fruit()
            self.snake.draw_snake()
        else:
            screen.fill((202,228,241))

            font = pygame.font.SysFont(None,60)

            if self.start_btn.draw():
                self.playing = True

            high = font.render('High Score ' + str(self.highscore), False, pygame.Color('purple'))
            high_rect = high.get_rect()
            high_rect.center = (400,300)
            screen.blit(high,high_rect)

            score = font.render('Your Score ' + str(self.score), False, pygame.Color('silver'))
            score_rect = score.get_rect()
            score_rect.center = (400,500)
            screen.blit(score,score_rect)

            if self.exit_btn.draw():
                self.run = False

            
            



    def update(self):
        if self.playing:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()
        
    def check_collision(self):
        if self.snake.body[0] == self.fruit.pos:
            self.fruit.reposition()
            self.snake.update_body()
            self.snake.play_crunch_sound()
        
        while(True):
            done = 0
            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.reposition()
                    done = 1
                    break
            if(done==1):
                continue
            break

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def game_over(self):
        self.playing = False
        self.score = len(self.snake.body) - 3
        if(self.highscore < len(self.snake.body) - 3):
            self.highscore = len(self.snake.body) - 3
        self.snake.reset()

    def draw_grass(self):
        grass_color = (167,209,61)
        for row in range(cell_number):
            if row%2==0:
                for col in range(cell_number):
                    if col%2==0:
                        grass_rect = pygame.Rect(col * cell_size, row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2!=0:
                        grass_rect = pygame.Rect(col * cell_size, row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size*cell_number)-40
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)

        apple_pos = apple.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(apple_pos.left,apple_pos.top,apple_pos.width+score_rect.width+6,apple_pos.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        screen.blit(score_surface,score_rect)
        screen.blit(apple,apple_pos)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
    


#pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#images
apple = pygame.image.load('Graphics/apple.png').convert_alpha()
start_img = pygame.image.load('Graphics/start_btn.png').convert_alpha()
exit_img = pygame.image.load('Graphics/exit_btn.png').convert_alpha()

#game font
game_font = pygame.font.Font(None,25)

main_game = Main_game()

screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,200)

main_game.run = True

while main_game.run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.run = False

        if event.type == screen_update:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
    if main_game.run:
        screen.fill(pygame.Color('green'))
        main_game.draw_element()
        pygame.display.update()

    clock.tick(60)
pygame.quit()