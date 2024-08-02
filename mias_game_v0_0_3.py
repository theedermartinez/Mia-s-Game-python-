import pygame
import os
from sys import exit

#Here we start the game, set a size for the display, create a caption and use a clock to update (at the end of the code)
pygame.init()
viewable = pygame.display.set_mode((800,400))
pygame.display.set_caption("Mia's Game")
clock = pygame.time.Clock()
game_active = True

#Working with a font: I imported a font from the internet designed for pixel art. Import font using the path, initialize it using pygame, and 70 is the size of the font
font_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/font/Pixeltype.ttf')
font = pygame.font.Font(font_path,70)

#Backround and elements: I decided to initialize using os and an absolute path because python was not liking my relative paths plus I wanted to make sure
#I knew what I was grabbing
'''Imported stuff'''
sky_surface = pygame.Surface((800,300))
sky_surface.fill("#87CEEB")

cloud_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/cloud.png')
cloud = pygame.image.load(cloud_path).convert_alpha()

ground_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/groundfinal.png')
ground = pygame.image.load(ground_path).convert_alpha()

hidding_sun_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/sunhidding.png')
hidding_sun = pygame.image.load(hidding_sun_path).convert_alpha()

home_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/house.png')
home = pygame.image.load(home_path).convert_alpha()

#Render name of game
mia_name = font.render("Mia's Game V 0.01",False, 'White')
mia_name_rec = mia_name.get_rect(center = (400,100))

#Game information
instruction_1 = font.render("Instructions: Use the arrows to move and space to jump", False, "White")
instruction_1_rect = instruction_1.get_rect(center = (100,250))
instruction_1pt2 = font.render("move to -> and do well, good luck :))", False, "White")
instruction_1pt2_rect = instruction_1pt2.get_rect(center = (200,280))

#render score
lifes = 100

#Gave over 
game_over = font.render("Game_Over: Press bar to continue", False,"Black")
game_over_req = game_over.get_rect(center = (400,200))

#Enemy Surfaces: Created a surface using pygame built-in
enemy1 =pygame.Surface((100,50))
enemy1.fill("Orange") 
enemy1_rect = enemy1.get_rect(midbottom = (600,300))
enemy2 = pygame.Surface((150,50))
enemy2.fill("Blue")
enemy2_rect = enemy2.get_rect(midbottom = (500,300))
 
#Score

#Enemy Variables: are manipulated to change the position of enemies
enemy1_x_position = 900
enemy1_y_position = 300

#Player Variables:
player_make = pygame.Surface((50,100))
player_make.fill("White")
player_rect = player_make.get_rect(midbottom = (40,300)) #Makes a rectagle around the surface
'''
Rectangle vs Surface: Allows you to place item using midbottom or any position instead of only doing it 
from the top left
'''
#Gravity 
player_gravity = 0
player_right = 0
player_left = 0
scene = 3

#Platform maker
platform1  = pygame.Surface((100,50))
platform1.fill("Black")
platform_rec1 =  platform1.get_rect(midbottom = (400,200))

while True:
    ##allows player to exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #check if any buttion was pressed and then see what button was pressed 
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                if event.key == pygame.K_RIGHT:
                    player_right =+ 5
                    print("right")
                else:
                    player_right = 0 
                if event.key == pygame.K_LEFT:
                    player_left =- 5
                    print("left")
                else:
                    player_left = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player_right = 0
                elif event.key == pygame.K_LEFT:
                    player_left = 0
            #Mouse click player jumps
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy1_rect.left = 900
                lifes = 100
                player_rect.x = 20
                player_left = 0
                player_right = 0
                scene = 1
                


    '''
    Squares are used for 3 main purpuses, collision, moving stuff around by using an anchor point and text background
    and decoration
    '''
   #using different stages to play the game (player)
    scene_picker_to_add = player_rect.x
    
    if scene_picker_to_add == 820:
        scene = scene + 1
    elif scene_picker_to_add == -20:
        if scene == 1:
            scene == scene
            player_rect.x = 20
        else:
            scene = scene - 1
            enemy1_rect.x = 900

    if player_rect.x == 820:
        player_rect.x = 0
    elif player_rect.x == -20:
         player_rect.x = 800
    


    if game_active:
        #We render here to update the text and we check for the gravity 300 and lives checker
        score = font.render(f"Life : {lifes}% left",False,'Black')
        score_rec = score.get_rect(center = (200,50))
        if player_rect.bottom >=300:
            player_rect.bottom = 300
        if lifes < 0:
            game_active = False
        #Scene changer here
        if scene == 1: 
            viewable.blit(sky_surface,(0,0))
            viewable.blit(cloud,(0,0))
            viewable.blit(cloud,(200,40))
            viewable.blit(cloud,(300,0))
            viewable.blit(cloud,(450,40))
            pygame.draw.ellipse(viewable,"Gold",pygame.Rect(600,200,150,150))
            viewable.blit(ground,(0,300))
            viewable.blit(ground,(400,300))
            viewable.blit(score,score_rec)
            pygame.draw.rect(viewable, 'black', mia_name_rec,border_radius=40)
            pygame.draw.rect(viewable, 'Orange', mia_name_rec,width=6,border_radius=40,)
            viewable.blit(mia_name,mia_name_rec)
            
            #enemies update the position of them
            viewable.blit(player_make,(player_rect))
            
            viewable.blit(enemy1,(enemy1_rect))
            enemy1_rect.x = enemy1_rect.x - 4
            player_rect.x += player_right
            player_rect.x += player_left
            player_gravity += 1
            player_rect.y += player_gravity

            if enemy1_rect.x <= 0:
                enemy1_rect.x = 800 

            if player_rect.colliderect(enemy1_rect):
                print("collision")
                lifes = lifes - 1
                print(lifes)
            
        if scene == 2:
            viewable.fill("Orange")
            viewable.blit(ground, (0,300))
            viewable.blit(hidding_sun, (200,100))
            viewable.blit(platform1,platform_rec1)
            viewable.blit(score,score_rec)
            viewable.blit(player_make,(player_rect))
            viewable.blit(enemy2,(enemy2_rect))
                    
            #Gravity
            player_rect.x += player_right
            player_rect.x += player_left
            player_gravity += 1
            player_rect.y += player_gravity

            #on platforms  
            if player_rect.colliderect(platform_rec1):
                plat  = True
                player_rect.bottom = platform_rec1.top
                print(player_rect.y)
                player_gravity -= 1
                print(f"gravity {player_gravity}")
    
            #enemy 2 features
            enemy2_rect.x = enemy2_rect.x - 4
            if enemy2_rect.x <= 0:
                enemy2_rect.x = 800
            if player_rect.colliderect(enemy2_rect):
                print("collision")
                lifes = lifes - 1
                
        if scene == 3:
            step_1 = pygame.Surface((50,50))
            step_1.fill("Orange")
            step_1_rec = step_1.get_rect(midbottom = (700,290))

            viewable.fill("Dark Gray")
            viewable.blit(home, (580,0))
            pygame.draw.rect(viewable, 'black', mia_name_rec,border_radius=40)
            pygame.draw.rect(viewable, 'Orange', mia_name_rec,width=6,border_radius=40,)
            viewable.blit(mia_name,mia_name_rec)
            viewable.blit(ground, (0,300))
            viewable.blit(score,score_rec)
            viewable.blit(player_make,(player_rect))
            viewable.blit(step_1,step_1_rec)
            
            
            player_rect.x += player_right
            player_rect.x += player_left
            player_gravity += 1
            player_rect.y += player_gravity

            if player_rect.colliderect(step_1_rec,):
                plat  = True
                player_rect.bottom = step_1_rec.top
                print(player_rect.y)
                player_gravity -= 1
                print(f"gravity {player_gravity}")
            '''
            print(f"player y is {player_rect.y} gravity is {player_gravity}")
            if player_rect.x > 700:
                print(f"player y is {player_rect.y} gravity is {player_gravity}")
                player_gravity = -5
                if player_rect.y < 200:
                    print("in the if stmt")
                    player_rect.bottom = 200
            '''   


       
    else:
        viewable.fill('Yellow')
        viewable.blit(game_over,game_over_req)
            

     #Updates game to 60 using the Clock feature
    pygame.display.update()
    clock.tick(60)

    