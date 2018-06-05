from gipozero import Button, LED, PWMLED

Red_button = Button(21)
Green_button = Button(25)
Blue_button = Button(18)
Red_light = PWMLED(22)
Green_light = PWMLED(6)
Blue_light = PWMLED(19)

def Sense_button_pressed(color):
    """Finds whether the red, blue, or green buttons were pressed and relays that to Arcade"""
    if color == "Red":
        return Red
    elif color == "Green":
        return Green
    elif color == "Blue":
        return Blue

def Brighten_and_dim_lights(red, green, blue, color_to_change):
    """Takes inputs from pygame determining what needs to be brightened or dimmed and gives that to the RGB LED"""
    if color_to_change == "red":
        if red == 0:
            Red_light.value = 0
            break
        else:
            Red_light.value = (red/17)/17#Because we are increasing the RGB value by 17 every time, I divide it by 17 twice.
            break                       #The first one takes it to how many times the button has been pressed. The second gets a fraction determining how bright the LED is
    elif color_to_change == "green":
        if green == 0:
            Green_light.value = 0
            break
        else:
            Green_light.value = (green/17/)/17 #I do likewise with the other colors
            break
    elif color_to_change == "blue":
        if blue == 0:
            Blue_light.value = 0
            break
        else:
            Blue_light.value = (blue/17)/17
            break
    
    
