import random


class Board:

    def getSnakes():
        n = int(input().strip())
        snakes = dict()

        while n:
            head,tail = map(int,input().strip().split())
            snakes[head]=tail
            n-=1

        return snakes

    def getLadders():
        n = int(input().strip())
        ladder = dict()

        while n:
            start,end = map(int,input().strip().split())
            ladder[start]=end
            n-=1

        return ladder

    def rollDice():

        return random.randint(1,6)