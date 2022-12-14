# Import library
import pygame
import random as rd 
from pygame import mixer

# Initialize pygame
pygame.init()

# Colors
background_color = ( 200, 0, 0 )
player_color = (255, 255, 255)
ball_color = (255, 255, 200)
line_color = (255, 255, 255)

# Players size
players_width = 20
players_height = 100

# Player 1 coordinates
player_1_x = 50
player_1_y = 300 - (players_height/2)
player_1_y_speed = 0

# Player 2 coordinates
player_2_x = 1200 - players_width
player_2_y = 300
player_2_y_speed = 0

# Ball coordinates
ball_x = 625
ball_y = 375
ball_radius = 20

ball_speed_x = 1
ball_speed_y = 1

# window size
screen_width = 1250
screen_height = 750

# size variable
size = ( screen_width, screen_height )

# Display the window
screen = pygame.display.set_mode( size )

# Icon
icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

# Title
pygame.display.set_caption("Pong Game")

# Score variable
player_1_score = 0
player_2_score = 0

# Score font
score_font = pygame.font.Font("font.otf", 32)

# Win font
win_font = pygame.font.Font("font.otf", 64)

# score position in the screen - Player 1
player_1_score_x = 10
player_1_score_y = 10

# Score position in the screen - Player 2
player_2_score_x = screen_width - 165
player_2_score_y = 10

# Win text position
win_x = 250
win_y = 300

# Player 1 score function 
def show_score_1(x,y):
    score1 = score_font.render("Player 1: " + str(player_1_score), True, (0, 0, 0))
    screen.blit( score1, (x, y) )

# Player 2 score function 
def show_score_2(x,y):
    score2 = score_font.render("Player 2: " + str(player_2_score), True, (0, 0, 0))
    screen.blit( score2, (x, y) )



# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player key controls

        # Checks for KEYDOWN event
        if event.type == pygame.KEYDOWN:

            # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = -1

            if event.key == pygame.K_s:
                player_1_y_speed = 1

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = -1

            if event.key == pygame. K_DOWN:
                player_2_y_speed = 1

        if event.type == pygame.KEYUP:

                # Player 1
            if event.key == pygame.K_w:
                player_1_y_speed = 0

            if event.key == pygame.K_s:
                player_1_y_speed = 0

            # Player 2
            if event.key == pygame.K_UP:
                player_2_y_speed = 0

            if event.key == pygame. K_DOWN:
                player_2_y_speed = 0

    # Player movement
    player_1_y += player_1_y_speed
    player_2_y += player_2_y_speed

    # Players boundaries

    # Player 1
    if player_1_y <= 0:
        player_1_y = 0

    if player_1_y >= screen_height - players_height:
        player_1_y = screen_height - players_height

    # Player 2
    if player_2_y <= 0:
        player_2_y = 0

    if player_2_y >= screen_height - players_height:
        player_2_y = screen_height - players_height

    # Ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball boundaries: top or buttom
    if ball_y > (screen_height - ball_radius) or ball_y < ball_radius:
        ball_speed_y *= -1 

    # Ball boundaries (rigth or left) and score update
    if ball_x > screen_width:

        player_1_score += 1
        lose_sound = mixer.Sound("invalid-selection.wav")
        lose_sound.play()

        ball_x = screen_width/2
        ball_y = screen_width/2
        ball_speed_x *= rd.choice([-1, 1])

    elif ball_x < 0:

        player_2_score += 1
        lose_sound = mixer.Sound("invalid-selection.wav")
        lose_sound.play()
        
        ball_x = screen_width/2
        ball_y = screen_width/2
        ball_speed_x *= rd.choice([-1, 1])

   

    # Fill screen with color
    screen.fill( background_color )

    # Drawin area

    # Define the player 1 - left: rectangle
    player_1 = pygame.draw.rect( screen, player_color, (player_1_x, player_1_y, players_width, players_height ))

    # Define the player 2 - left: rectangule
    player_2 = pygame.draw.rect( screen, player_color, (player_2_x, player_2_y, players_width, players_height ))

    # Draw the ball
    ball = pygame.draw.circle( screen, ball_color, (ball_x, ball_y), ball_radius)

    # Draw the center line
    pygame.draw.aaline(screen, line_color, (screen_width/2,0), (screen_width/2, screen_height))

    # Colitions
    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1
        ball_sound = mixer.Sound("pong.wav")
        ball_sound.play()

 # Player win
    if player_1_score == 10:

        ball_y = 2000
        ball_speed_x = 0
        ball_speed_y = 0
        player_1_y_speed = 0
        player_2_y_speed = 0
        win_text = win_font.render(" Player 1 Win", True, (0, 0, 0))
        screen.blit(win_text, (win_x, win_y))

    elif player_2_score == 10:

        ball_y = 2000
        ball_speed_x = 0
        ball_speed_y = 0
        player_1_y_speed = 0
        player_2_y_speed = 0
        win_text = win_font.render(" Player 2 Win", True, (0, 0, 0))
        screen.blit(win_text, (win_x, win_y))



    # Call the show_score_1 function
    show_score_1(player_1_score_x, player_1_score_y)

    # Call the show_score_1 function
    show_score_2(player_2_score_x, player_2_score_y)
    # Refresh the window
    pygame.display.flip()

