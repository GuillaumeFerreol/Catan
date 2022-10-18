import numpy as np

import random




class Player:
    def __init__(self, name):
        self.name=name
        self.resources ={'brick': 0, 'grain':0, 'lumber': 0, 'ore':0, 'wool':0} #Resources (initialized as 0)
        self.regions = [] #Regions (initialized as 0)
        self.points=0
        self.settlements=[]
        self.cities=[]
        self.roads=[]
        #(Ports)

    #Methods (version 3)
        def pass_round(self, user_answer):#Pass the round

        def roll_dice(self):
            return random.randint(1,6)+random.randint(1,6)

        def buy_road(self, user_answer):

        def buy_settlements(self,user_answer,  regions):

        def upgrade_settlement(self, user_answer):


        def move_robber(self, region, player_to_steal, resource_to_steal):


        #(Trade with players)
        #(Trade with bank)
        #(Accept trade)
        #(Refuse trade)
        #(Buy development card)



class Region:

    def __init__(self, name, resource, position):
        self.position=position
        self.resource=resource
        self.name=name
        self.owner={}
        self.robber=0
    Attributes (version 3)

        Owner(s) (dictionary with key: player name and value: 0/1 for town/city)
        Robber 
        Vertices (initialized as a dictionary [0-5])
        Edges (initialized as a dictionary [0-5])
        (Ports)

    Methods (version 3)
        Give resources to players



class Road:

    def __init__(self, ):
    Attributes (version 3)
        Owner
        Regions it belongs to 


    Methods (version 3)
        Assign_owner
        Assign_region
        Get_owner
        Get_regions



class Settlement:

    def __init__(self, ):
    Attributes (version 3)
        Owner
        Multiplier (initialized as 1 → becomes 2 when town is upgraded to city)
        Level (Town or City (initialized as 0 - town))
        Regions it belongs to
        (Port(initialized as null))

    Methods (version 3)
        Pass the round
        Assign owner
        Assign multiplayer 
        Buy roads
        Buy settlements



class Board:

    def __init__(self, ):
        self.regions_name=('a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s')
        self.region_position=(k for k in range(0, 19))
        self.resources_list=[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
        random.shuffle(self.resources_list)
        random.shuffle(self.region_position)
        #forest=1, pasture=2, fields=3, hills=4, mountain=5, desert=6
        self.regions_list=[Region(self.regions_name[k], self.resources_list[k], self.region_position[k] ) for k in range(len(self.regions_name))]





    Attributes (version 3)
        Regions (list of regions)

    Methods (version 3)
        Assign robber
        show(V2?)



class Game:

    def __init__(self, names):
        for name in names:
            self.players={name:Player(name)}
            self.scores=[self.players[player].points for player in self.players]
            self.winning_condition=0


        def declare_winner(self, current_player):
                if self.players[current_player].points>10:
                    print(f'player {current_player} wins the game !')
                    return 1

        def turn(self, player):
            self.dice_result=player.roll_dice()
            #give resources to each players
            player.buy_road()
            player.buy_settlements(regions)
            player.upgrade_settlement()
            player.move_robber(region, player_to_rob, resource_to_rob)

        def rounds(self):
            while True:
                for player in self.players:
                    turn(self.players[player])
                    self.winning_condition=declare_winner(player)
                    if self.winning_condition!=0:
                        break
                    print(f'the scores are {self.scores}')
            print(f'the scores are {self.scores}')
                    




























