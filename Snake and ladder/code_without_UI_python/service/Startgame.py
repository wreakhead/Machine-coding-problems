

from model.Board import *

from model.Player import *


class StartGame:

    def getPlayers(self):
        no_of_players = int(input().strip())

        player_q = []

        while no_of_players:
            name = input().strip()
            player = Player(name)
            player_q.append(player)

            no_of_players-=1

        return player_q

    def check_Ladder_or_snake(self,pos,ladder,snakes):

        return ((pos in ladder) or (pos in snakes))

        
        


    def play(self):

        won = False

        winning_pos = 100

        snakes = Board.getSnakes()

        ladder = Board.getLadders()

        players_q = self.getPlayers()

        winners = []


        while len(players_q):


            curr_player = players_q.pop(0)
            
            print("Current Player "+ curr_player.name,end=" ")

            move = Board.rollDice()

            print("Dice roll "+str(move))

            curr_player.pos += move

            if curr_player.pos > winning_pos:
                curr_player.pos -= move

            else:
                
                print("Moved to "+str(curr_player.pos))

                while self.check_Ladder_or_snake(curr_player.pos,ladder,snakes):
                    if curr_player.pos in ladder:
                        print(curr_player.name+" got ladder "+str(curr_player.pos)+" to "+str(ladder[curr_player.pos]))
                        curr_player.pos = ladder[curr_player.pos]

                    if curr_player.pos in snakes:
                        print(curr_player.name+" bitten "+str(curr_player.pos)+" to "+str(snakes[curr_player.pos]))
                        curr_player.pos = snakes[curr_player.pos]    

                
                if curr_player.pos == winning_pos:
                    won = True
                        

            if won == False:    
                players_q.append(curr_player)
            else:
                winners.append(curr_player.name)
                won = False  
            

            print("----------")
        return winners    
