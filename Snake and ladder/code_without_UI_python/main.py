from service.Startgame import *


if __name__ == '__main__':
    obj = StartGame()
    winners = obj.play()
    i=1
    for x in winners:

        print(str(i)+" "+x)
        i+=1
        
