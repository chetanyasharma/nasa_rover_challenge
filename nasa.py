import time
from getch import getch, pause #only................ for............. linux/unix............. systems

#will restart the programme to take the input of corresponding rover11
def restart():
    print("for next rover data anytime hit :   a   : \n or hit return to continue ")
    if getch() == 'a':# reads keyboard enterd key
        nasa_start()
    else:
        pass
#function for north face
def north(cardinal_point,x_cor,y_cor):
    print(x_cor,y_cor,cardinal_point)
    restart()
    direction=input("enter direction \n")#takes rovers movement input from user one by one
    if direction.upper() =='R':
        cardinal_point = 'E'
        east(cardinal_point,x_cor,y_cor)
    if direction.upper() =='L':
        cardinal_point = 'W'
        west(cardinal_point,x_cor,y_cor)
    if direction.upper() =='M':
        y_cor = y_cor + 1
        if y_cor > grid_area_y:
            print("rover going out of range.Please enter the directions carefully !!!")
            north(cardinal_point,x_cor,y_cor)
        else:
            print(x_cor,y_cor,cardinal_point)
            north(cardinal_point,x_cor,y_cor)
    else:
        print("enter only single character R, L , M ")
        print(x_cor,y_cor,cardinal_point)

#function for east face
def east(cardinal_point,x_cor,y_cor):
    print(x_cor,y_cor,cardinal_point)
    restart()
    direction=input("enter direction \n")
    if direction.upper() =='R':
        cardinal_point = 'S'
        south(cardinal_point,x_cor,y_cor)
    if direction.upper() =='L':
        cardinal_point = 'N'
        north(cardinal_point,x_cor,y_cor)
    if direction.upper() =='M':
        x_cor = x_cor + 1
        if x_cor > grid_area_x:
            print("rover going out of range.Please enter the directions carefully !!!")
            east(cardinal_point,x_cor,y_cor)
        else:
            print(x_cor,y_cor,cardinal_point)
            east(cardinal_point,x_cor,y_cor)
    else:
        print(x_cor,y_cor,cardinal_point)

#function for west face
def west(cardinal_point,x_cor,y_cor):
    print(x_cor,y_cor,cardinal_point)
    restart()
    direction=input("enter direction \n")
    if direction.upper() =='R':
        cardinal_point = 'N'
        north(cardinal_point,x_cor,y_cor)
    if direction.upper() =='L':
        cardinal_point = 'S'
        south(cardinal_point,x_cor,y_cor)
    if direction.upper() =='M':
        x_cor = x_cor - 1
        if x_cor < 0:
            print("rover going out of range.Please enter the directions carefully !!!")
            west(cardinal_point,x_cor,y_cor)
        else:
            print(x_cor,y_cor,cardinal_point)
            west(cardinal_point,x_cor,y_cor)
    else:
        print(x_cor,y_cor,cardinal_point)

#function for south face
def south(cardinal_point,x_cor,y_cor):
    print(x_cor,y_cor,cardinal_point)
    restart()
    direction=input("enter direction \n")
    if direction.upper() =='R':
        cardinal_point = 'W'
        west(cardinal_point,x_cor,y_cor)
    if direction.upper() =='L':
        cardinal_point = 'E'
        east(cardinal_point,x_cor,y_cor)
    if direction.upper() =='M':
        y_cor = y_cor - 1
        if y_cor < 0:
            print("rover going out of range.Please enter the directions carefully !!!")
            south(cardinal_point,x_cor,y_cor)
        else:
            print(x_cor,y_cor,cardinal_point)
            south(cardinal_point,x_cor,y_cor)
    else:
        print(x_cor,y_cor,cardinal_point)

#function for starting the script
def nasa_start():
    x_cor = int(input("enter x coordinate \n"))
    y_cor = int(input("enter y coordinate \n"))
    cp = input("enter th face as \n NORTH -- n \n SOUTH -- s \n WEST -- w \n EAST -- e \n ")
    cardinal_point = cp.upper() # uppercase the inputs
    if cardinal_point == "N":
        north(cardinal_point,x_cor,y_cor)
    if cardinal_point == "E":
        east(cardinal_point,x_cor,y_cor)
    if cardinal_point == "W":
        west(cardinal_point,x_cor,y_cor)
    if cardinal_point == "S":
        south(cardinal_point,x_cor,y_cor)
    else:
        print("wrong data entered")

grid_area_x = int(input("enter your grid area for x \n"))
grid_area_y = int(input("enter your grid area for y \n"))
nasa_start() #calling function nasa_start
