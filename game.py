""" paint.py 
    a simple paint program"""

import pygame

red = 0
blue = 0
green = 0

def checkKeys(myData):
    """test for various keyboard inputs"""
    global red
    global green
    global blue

    background = (0, 0, 0)
    
    #extract the data
    (event, background, drawColor, lineWidth, keepGoing) = myData
    #print myData
    if event.key == pygame.K_1:
        #red
        red = red + 17
        if red > 255 :
            red = 0
        
    elif event.key == pygame.K_2:
        #green 
        green = green + 17
        if green > 255 :
            green = 0
            
    elif event.key == pygame.K_3:
        #blue
        blue = blue + 17
        if blue > 255 :
            blue = 0
    drawColor = (red, green, blue)
    #return all values 
    myData = (event, background, drawColor, lineWidth, keepGoing)
    return myData

def main():
    #making everything work
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint Program")
    #set up background
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 10

    #constantly updating the progam
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            #code for getting mouse position
            #on left click, draws a point
            if event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(background, drawColor, lineStart, lineEnd, lineWidth)
                lineStart = lineEnd
            elif event.type == pygame.KEYDOWN:
                myData = (event, background, drawColor, lineWidth, keepGoing)
                myData = checkKeys(myData)
                (event, background, drawColor, lineWidth, keepGoing) = myData
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
