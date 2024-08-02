import pygame
from sys import exit
import os
'''We are not using a dictionary in version 0.0.5, using functions as much as possible and using a dictonary to determine gravity on the platforms.'''
def make_surface(width,height,color = "white"):
    '''width,height, color, it will make a surface and return the desired object'''
    object  = pygame.Surface((width,height))
    object.fill(color)
    return object

def make_rect(object,xcord, ycord):
    '''object, xcord, ycord, makes a rectangle and returns coordinates from any object including text etc'''
    rect = object.get_rect(midbottom  = (xcord,ycord))
    return rect
def make_image(path):
    '''file path, Must pass a path in single quotations marks'''
    objectload_path = os.path.abspath(path)
    objectload = pygame.image.load(objectload_path).convert_alpha()
    return objectload
def three_hundred_ground(player_rect):
    '''player rect, call when there is no holes on the ground and you want the ground to be 300'''
    if player_rect.bottom >=300:
        player_rect.bottom = 300
        return player_rect.bottom
def enemy_1_movement(enemy1_rect):
    '''enemy1_req, takes the rect and moves it 1 '''
    enemy1_rect.x = enemy1_rect.x - 5
    if enemy1_rect.x <= 0:
        enemy1_rect.x = 800 
        return enemy1_rect
    return enemy1_rect
def make_font_text(size,text_to_add, color = "white"):
    '''size, text (in quotes), color: takes a size and a text to add to return a text, we can use this to display any text'''
    font_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/font/Pixeltype.ttf')
    font = pygame.font.Font(font_path,size)
    game_text= font.render(text_to_add,False, color)
    return game_text
def collision(player_rect,enemy1_rect,lifes):
    '''player_rect,enemy_rect,lifes, will check for collision and return lifes minus 1'''
    if player_rect.colliderect(enemy1_rect):   
        print("collision")
        lifes = lifes - 1
        return lifes
    return lifes 
def platform_gravity(player_rect,platform_rec1,stat_dic,player_gravity):
    '''player_rec,platform_rec,dictionary(stat_dic'''
    plat  = True
    player_rect.bottom = platform_rec1.top
    print(player_rect.y)
    stat_dic["player_gravity"] = stat_dic["player_gravity"] - 1
    stat_dic["on_platform"] = True
def game_name(viewable):
    '''call it to put the name of the game on screen'''
    mia_name = make_font_text(70,"Mia's Game v 0.0.5 (optimized)")
    mia_name_rect = make_rect(mia_name,400,300)
    pygame.draw.rect(viewable, 'black', mia_name_rect,border_radius=40)
    pygame.draw.rect(viewable, 'Orange', mia_name_rect,width=6,border_radius=40,)
    viewable.blit(mia_name,mia_name_rect)
def death_by_fall(player_rect,lifes):
    '''player_rect, lifes : in parts that have death by fall, use this'''
    lifes = lifes - 1
    return lifes
'''here to main are all the scenes, mess with this if you just wanna change what is displayed'''
'''first load background things with no rectangle, then rectangle stuff'''
def scene_neg_1(viewable):
    '''viewable: Here we have the scene that happens when we go backwards in the name '''
    viewable.fill("Red")
    initial_greeting = make_font_text(30,"I TOLD YOU TO GO THAT WAY >:( BAD BAD BAD ->>>> GO NOW ","Black")
    initial_greeting_rect = make_rect(initial_greeting,300,100)
    viewable.blit(initial_greeting,initial_greeting_rect)

def scene_0(viewable):
    '''viewable: here is the initial scene that shows up when starting the game'''
    viewable.fill(("#ffb3ba"))
    game_name(viewable) 
    initial_greeting = make_font_text(30,"Hello welcome! use the arrows to move and space to jump","Black")
    initial_greeting_rect = make_rect(initial_greeting,276,100)
    viewable.blit(initial_greeting,initial_greeting_rect)
    initial_greeting_2 = make_font_text(30,"Use the platforms(now black) to avoid enemies! do not die!","Black")
    initial_greeting_2_rect = make_rect(initial_greeting_2,282,135)
    viewable.blit(initial_greeting_2,initial_greeting_2_rect)
    initial_greeting_3 = make_font_text(30,"Head -->> that way. PRESS SPACE AND THEN ARROWS ONE AFTER THE OTHER","Black")
    initial_greeting_3_rect = make_rect(initial_greeting_3,350,170)
    viewable.blit(initial_greeting_3,initial_greeting_3_rect)
          
def scene_1(viewable):
    '''viewable: must pass on where it will end up at, second scene of the game '''
    sky_surface = make_surface(800,300,"Blue")
    viewable.blit(sky_surface,(0,0))
    cloud = make_image('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/cloud.png')
    viewable.blit(cloud,(0,0))
    viewable.blit(cloud,(200,40))
    viewable.blit(cloud,(300,0))
    viewable.blit(cloud,(450,40))                  #positionx,positiony,width,height
    pygame.draw.ellipse(viewable,"Gold",pygame.Rect(600,100,150,150))
    ground = make_image('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/groundfinal.png')
    viewable.blit(ground,(0,300))
    game_name(viewable)
    
def scene_2(viewable,player_rect,stat_dic,player_gravity):
    '''viewable: third scene of the scene'''
    viewable.fill("pink")
    game_name(viewable)
    ground = make_image('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/groundfinal.png')
    viewable.blit(ground,(0,300))
    hidding_sun = make_image('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/sunhidding.png')
    viewable.blit(hidding_sun, (200,100))
    platform1 = make_surface(100,50,"black")
    platform_rec1 = make_rect(platform1,200,200)
    viewable.blit(platform1,platform_rec1)
    stat_dic["on_platform"] = False
    if player_rect.colliderect(platform_rec1):
        platform_gravity(player_rect, platform_rec1,stat_dic,player_gravity)
    platform2 = make_surface(100,50,"black")
    platform_rec2 = make_rect(platform1,450,200)
    viewable.blit(platform2,platform_rec2)
    if player_rect.colliderect(platform_rec2):
        platform_gravity(player_rect, platform_rec2,stat_dic,player_gravity)

def scene_3(viewable,player_rect,stat_dic,player_gravity):
    '''viewable, player_rect,stat_dic,player_gravity: we pass on the viewable, the rect of player in order to check for collision, stat dictinary to show true if it is on 
    practform and the prayer gravity that must change when when on the platform because otherwise gravity continues to increase'''
    viewable.fill("#36454F")
    ground = make_image('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/images/groundfinal.png')
    ground_rect = make_rect(ground,100,400)
    viewable.blit(ground,ground_rect) 
    if player_rect.colliderect(ground_rect):
        platform_gravity(player_rect, ground_rect,stat_dic,player_gravity)
    
def main():
    '''main loop of the game we start enemy 1 and player rect hereand allow the controls to work while game is active, only needs to be called and not changed thus I 
    left it in the main without making it a function'''
    pygame.init()
    viewable = pygame.display.set_mode((800,400))
    pygame.display.set_caption("Mia's Game")
    clock = pygame.time.Clock()
    game_active = True
    stat_dic = {}
    stat_dic["on_platform"] = False

    '''Working with a font: I imported a font from the internet designed for pixel art. Import font using the path, initialize it using pygame,
       and 70 is the size of the font'''
    font_path = os.path.abspath('C:/Users/marti/Documents/Eder Martinez/x/Projects/Python/mias_game/font/Pixeltype.ttf')
    font = pygame.font.Font(font_path,70)

    enemy1 = make_surface(100,50,"orange")
    enemy1_rect = make_rect(enemy1,900,300)
    player_make = make_surface(50,100,'Orange')
    player_rect = make_rect(player_make,40,300)
    lifes = 100
    scene = 0

    stat_dic["player_gravity"] = 0
    player_right = 0
    player_left = 0

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
                        stat_dic["player_gravity"] = -20
                        print("jump")
                    if event.key == pygame.K_SPACE and stat_dic["on_platform"] == True: #and player_rect.bottom == 300:
                        stat_dic["player_gravity"] = -20
                        print("jumpv2")
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
                        stat_dic["player_gravity"] = -20
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    enemy1_rect.left = 900
                    lifes = 100
                    player_rect.x = 20
                    player_left = 0
                    player_right = 0
                    scene = 0
        '''This is easier to mess with here, instead of making a list and checking the items in it to get a return from a fuction or a dictionary,
        for now this will be enough, as the game grows we might switch it'''
        '''We use scene_picker to add because if we direcly both check and change x, we end up in a weird loop'''
        scene_picker_to_add = player_rect.x
        print(f"{scene_picker_to_add}x is, y is {player_rect.y}. {scene} is scene,  ")
        if scene_picker_to_add == 820:
            scene = scene + 1
        elif scene_picker_to_add == -20:
            if scene == 1:
                scene == scene
                player_rect.x = 800
            if scene == -1:
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
            if lifes < 0:
                game_active = False
            '''check for lifes, add the score and add beta text'''
            score = font.render(f"Life : {lifes}% left",False,'Black')
            score_rect = score.get_rect(center = (200,50))
            '''This is the controlls, it will add or subtract etc from the player rect, outside of scenes because it is always true'''
            player_rect.x += player_right
            player_rect.x += player_left
            stat_dic["player_gravity"] += 1
            player_rect.y += stat_dic["player_gravity"]
            #if lifes < 0:
              #    game_active = False
            '''all scenes here'''
            if scene == -1:
                scene_neg_1(viewable)
                three_hundred_ground(player_rect)
                viewable.blit(player_make,player_rect)
                viewable.blit(score,score_rect)
            if scene == 0:
                scene_0(viewable)
                three_hundred_ground(player_rect)
                viewable.blit(player_make,player_rect)
            if scene == 1:    
                scene_1(viewable)
                three_hundred_ground(player_rect)
                viewable.blit(player_make,player_rect)
                viewable.blit(enemy1,enemy1_rect)
                enemy_1_movement(enemy1_rect)
                viewable.blit(score,score_rect)
                lifes = collision(player_rect,enemy1_rect,lifes)
            if scene == 2:
                scene_2(viewable,player_rect,stat_dic,stat_dic["player_gravity"])
                three_hundred_ground(player_rect)
                viewable.blit(player_make,player_rect)
                viewable.blit(score,score_rect)
                viewable.blit(enemy1,enemy1_rect)
                enemy_1_movement(enemy1_rect)
                
                lifes = collision(player_rect,enemy1_rect,lifes)
                print(f"{player_rect.y} y of player is, {stat_dic['player_gravity']}gravity")
                print(stat_dic)
            '''Check if it we have life so if we don't game active will be false meaning it will change the while loop'''
            if scene == 3:
                scene_3(viewable,player_rect,stat_dic,stat_dic["player_gravity"])
                viewable.blit(player_make,player_rect)
                viewable.blit(score,score_rect)
                if player_rect.y > 600: 
                    lifes  = death_by_fall(player_rect,lifes)
        else:
            viewable.fill('Yellow')
            game_over = make_font_text(70,"Game Over, press bar to continue","black")
            game_over_req = make_rect(game_over,400,200)
            viewable.blit(game_over,game_over_req)

        '''do not forget this to update!!!'''
        pygame.display.update()
        clock.tick(60)
 
main()