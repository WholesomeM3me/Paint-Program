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

    #extract the data
    (event, background, drawColor, lineWidth, keepGoing) = myData
    #print myData
    if event.key == pygame.K_a:
        #red
        red = red + 15
        drawColor = (red, green, blue)
        if red == 255 :
            red = 0
        
    elif event.key == pygame.K_s:
        #green 
        green = green + 15
        drawColor = (red, green, blue)
        if green == 255 :
            green = 0
            
    elif event.key == pygame.K_d:
        #blue
        blue = blue + 15
        drawColor = (red, green, blue)
        if blue == 255 :
            blue = 0
    
    #return all values 
    myData = (event, background, drawColor, lineWidth, keepGoing)
    return myData

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Paint Program")
    
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 10
    
    while keepGoing:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEMOTION:
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
