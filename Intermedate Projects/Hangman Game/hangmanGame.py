import pygame 
pygame.init()

gameScreen_width=3000
gameScreen_height=3000
gameScreen=pygame.display.set_mode((gameScreen_width,gameScreen_height))
pygame.display.set_caption('HangMan')

clock=pygame.time.Clock()
gameExit=False

white=(255,255,255)
black=(0,0,0)
blue=(0,0,255)
green=(0,255,0)


vowels=["a","e","i","o","u"]

myfont=pygame.font.SysFont('Arial',50)


guesses_one=0
guesses_two=0
guesses_three=0
guesses_four=0
guesses_five=0
guesses_six=0
guessed=0

hangMan_Image=pygame.image.load('/home/geekerlink/Desktop/hangman_stand.png')


def hangMan_Upload(x,y):
    gameScreen.blit(hangMan_Image,(x,y))

def hangMan_Body(guesses_one,guesses_two,guesses_three,guesses_four,guesses_five,guesses_six):
    if guesses_one == 1 :
        pygame.draw.circle(gameScreen,blue,(1100,300),90)

    if guesses_two == 2 :
        pygame.draw.line(gameScreen,blue,(1100,320),(1100,650),5)

    if guesses_three == 3:
        pygame.draw.line(gameScreen,blue,(1100,650),(900,800),5)

    if guesses_four == 4:
        pygame.draw.line(gameScreen,blue,(1100,650),(1300,800),5)

    if guesses_five == 5:
        pygame.draw.line(gameScreen,blue,(1100,500),(900,350),5)

    if guesses_six == 6:
        pygame.draw.line(gameScreen,blue,(1100,500),(1300,350),5)
    

def blank_words(length_of_word,words):
    blank_xstart=1700
    blank_xend=1770
    for num in range(0,length_of_word):
        pygame.draw.line(gameScreen,black,(blank_xstart,1400),(blank_xend,1400),5)
        if blank_xend>=2950 and blank_xend<=3000:
            blank_xend=1700-50
            blank_xstart=blank_xend-70
        elif blank_xstart<1700:
            blank_xend=blank_xstart-50
            blank_xstart=blank_xend-70
        else:
            blank_xstart=blank_xend+50
            blank_xend=blank_xstart+70
    if blank_xstart<1700:
        blank_xstart=blank_xend+50
        blank_xend=blank_xstart+70
    else:
        blank_xstart=1700
        blank_xend=1770

    blank_positions=[blank_xstart,blank_xend]

    for num in range(0,length_of_word):
        if words[num] in vowels:
            pygame.draw.line(gameScreen,black,(blank_xstart,1430),(blank_xend,1470),5)
            pygame.draw.line(gameScreen,black,(blank_xend,1430),(blank_xstart,1470),5)
        
        blank_xstart=blank_xend+50
        blank_xend=blank_xstart+70

    return blank_positions

def print_words(length_of_word,words,blank_positions):
    if guessed == 1:
        hangMan_word=words
        letter_xstart=blank_positions[0]
        letter_xend=blank_positions[1]
        for letter in range(0,length_of_word):
            hangMan_letter=myfont.render(hangMan_word[letter],True,black)
            gameScreen.blit(hangMan_letter,(letter_xstart+20,1350))
            letter_xstart=letter_xend+50
            letter_xend=letter_xstart+70


    
        

while not gameExit:
    
    words="rendevouz"
    length_of_word=len(words)
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit=True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                guesses_one=1

            if event.key == pygame.K_t:
                guesses_two=2

            if event.key == pygame.K_r:
                guesses_three=3
                

            if event.key == pygame.K_l:
                guesses_four=4
                
            if event.key == pygame.K_a:
                guesses_five=5
                

            if event.key == pygame.K_j:
                guesses_six=6
            
            if event.key == pygame.K_g:
                guessed=1


            

    x=gameScreen_width *0.1
    y=gameScreen_height*0.1

    
    gameScreen.fill(white)
    hangMan_Upload(x,y)
    hangMan_Body(guesses_one,guesses_two,guesses_three,guesses_four,guesses_five,guesses_six)
    blank_positions=blank_words(length_of_word,words)
    print_words(length_of_word,words,blank_positions)
    
    pygame.display.update()
    clock.tick(60)


pygame.quit()
quit()