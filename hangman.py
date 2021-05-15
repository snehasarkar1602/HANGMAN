import pygame
import os
import math
import random

#setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Welcome to HANGMAN GAME!")

#button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i  // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A+i), True])

#letter font
LETTER_FONT = pygame.font.SysFont('comicsans',40)
WORD_FONT = pygame.font.SysFont('comicsans',60)
TITLE_FONT = pygame.font.SysFont('broadway',60)
FIRSTSCREEN_FONT = pygame.font.SysFont('comicsans',50)
LASTSCREEN_FONT = pygame.font.SysFont('algerian',60)
PLAYAGAIN_FONT = pygame.font.SysFont('comicsans',60)
CORRECTWORD_FONT = pygame.font.SysFont('algerian',40)

#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)


#game variable
hangman_status = 0
words = ["ASSAM", "BIHAR", "CHATTISGARH", "GOA", "GUJARAT", "HARAYANA", "JHARKHAND", "KARNATAKA", "KERALA", "MAHARASHTRA", "MANIPUR", "MEGHALAYA", "MIZORAM", "NAGALAND", "ODISHA", "PUNJAB", "RAJASTHAN", "SIKKIM", "TELANGANA", "TRIPURA", "UTTARAKHAND"]
word = random.choice(words)
guessed = []

#colours
WHITE = (255,255,255)
PINK = (240,128,128)
BLACK = (0,0,0)

def draw():
    win.fill(PINK)

    #draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "

        else:
            display_word += "_ "

    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))
    
    
    #draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    
    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(2000)
    win.fill(PINK)
    text = LASTSCREEN_FONT.render(message, 1, BLACK)
    win.blit(text, (240,213))
    pygame.display.update()
    pygame.time.delay(3000)


def correct_word(message):
    pygame.time.delay(2000)
    win.fill(PINK)
    text = CORRECTWORD_FONT.render(message, 1, BLACK)
    win.blit(text, (0,213))
    pygame.display.update()
    pygame.time.delay(6000)


def first_screen():
    win.fill(PINK)

    #draw message and ask user if they want to play
    text = FIRSTSCREEN_FONT.render("PRESS ANYWHERE ON THE SCREEN TO PLAY!", 1, BLACK)
    win.blit(text, (0,213))
    pygame.display.update()
    
def main():
    global hangman_status

    #setup game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(FPS)

        #quit game 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #to get the (x,y) coordinates of where the mouse button was clicked        
            if event.type ==  pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()
    
        won = True                    
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("YOU WON...!!!")
            break
        
        if hangman_status == 6:
            display_message("YOU LOST...!!!")
            correct_word(" THE CORRECT WORD IS " + str(word))
            break

#main menu rendering
while True:
    #setup game loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    clock.tick(FPS)

    first_screen()
    
    #check collision
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pos < (800,500):
                main()

       
pygame.quit()
