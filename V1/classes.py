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
                pass
        def roll_dice(self):
            return random.randint(1,6)+random.randint(1,6)

        def buy_road(self, user_answer):
            #check resources
            #ask user yes/no
            #ask user where
            #update road, player
            pass

        def buy_settlements(self,user_answer,  regions):
            #check resources
            #ask user yes/no
            #ask user where
            #update region, player
            pass

        def upgrade_settlement(self, user_answer):
            #check resources
            #ask user yes/no
            #ask user where
            #update settlement, player
            pass

        def move_robber(self):

            #ask region, player_to_rob, resource_to_rob
            #update region
            #update player resources
            pass

        #(Trade with players)
        #(Trade with bank)
        #(Accept trade)
        #(Refuse trade)
        #(Buy development card)



class Region:

    types_to_resources={'4': 'bricks', '3':'grain', '1':'lumber', '5':'ore', '2':'wool'}  #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)
    

    def __init__(self, name,dice_number, region_type, position, coordinates):
        self.position=position
        self.coordinates=coordinates
        self.region_type=region_type
        self.resource_type=self.types_to_resources[region_type]
        self.name=name
        self.dice_number=dice_number
        self.robber=0
        self.vertices={p: Settlement() for p in ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']}
        self.edges={p: Road() for p in ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']}

    def give_resources(self):
        if self.region_type==6 or self.robber!=0:
            pass

        for s in self.vertices:
            if s[0]!=None:
                s[0].resources[self.resource_type]+=1*s[2].multiplier


    # Attributes (version 3)

    #     Owner(s) (dictionary with key: player name and value: 0/1 for town/city)
    #     Vertices (initialized as a dictionary [0-5]) with value [owner, buildable, occupied]?
    #     Edges (initialized as a dictionary [0-5]) with value [owner, buildable, occupied]?
    #     (Ports)

    # Methods (version 3)
    #     Give resources to players



class Road:

    def __init__(self, *args):
        self.owner=None
        self.regions=[name for name in args]
        self.level=0 #0=empty, 1=road exists

    def assign_owner(self, owner):
        self.owner=owner
        self.level=1

    # Methods (version 3)
    #     Assign_owner
    #     Assign_region
    #     Get_owner
    #     Get_regions



class Settlement:

    #each player has X settlements and Y roads at the beggining
    def __init__(self, *args):
        self.multiplier=0 #level = multiplier?
        self.owner=None
        self.regions=[name for name in args]
        self.level=0
        
    # Attributes (version 3)
    #     Owner
    #     Multiplier (initialized as 1 → becomes 2 when town is upgraded to city)
    #     Level (Town or City (initialized as 0 - town))
    #     Regions it belongs to
    #     (Port(initialized as null))

    def assign_owner(self, owner)
        self.owner=owner
        self.multiplier=1
        self.level=1

    def upgrade(self):
        self.level=2
        self.multiplier=2


class Settlement_Location:

    def __init__(self, position):
        self.coordinates=some_function(position)
        self.settlement=None



    def assign_settlement(self, settlement):
        self.settlement=settlement

class Road_Location:

    def __init__(self, position):
        self.coordinates=some_function(position)
        self.road=None



    def assign_settlement(self, road):
        self.road=road


    



class Board:

    def __init__(self):
        
        self.region_position=tuple(range(0, 19))
        self.region_types=[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]
        random.shuffle(self.region_types)
        #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)

        self.region_coordinates={'1': (2,0,0), '2': (1,0,1), '3':(0,2,0), '4':(0,1,1), '5': (0,2,0), '6':(-1,1,0), '7':(-2,0,0), '8':(-1,0,-1), '9':(0,0,-2), 
                                '10': (0,-1,-1), '11': (-2,0,0), '12': (1,-1,0), '13':(1,0,0), '14':(0,0,1), '15': (0,1,0), '16':(-1,0,0), '17':(0,0,-1), 
                                '18':(0,-1,0), '19':(0,0,0)}
        self,region_name=(('a',5) , ('b',2) , ('c',6), ('d',3), ('e',8), ('f',10), ('g',9), ('h',12), ('i',11), 
                            ('j',4), ('k',8), ('l',10), ('m',9), ('n',4), ('o',5), ('p',6), ('q',3), ('r',11))
        self.regions_list=[Region(self.region_name[k][0], self.region_name[k][1], self.region_types[k], 
                                    self.region_position[k], self.region_coordinates(str(self.region_position[k])) ) for k in range(len(self.regions_name))]


        def assign_robber(self):
            self.region_list[random.randint(0,19)].robber==1

        
        #show(V2?)



class Game:

    def __init__(self, names):
        for name in names:
            self.players={name:Player(name)}
            self.scores=[self.players[player].points for player in self.players]
            self.winning_condition=0
        self.board=Board()


        def declare_winner(self, current_player):
                if self.players[current_player].points>10:
                    print(f'player {current_player} wins the game !')
                    return 1

        def turn(self, player):
            self.dice_result=player.roll_dice()
            if self.dice_result==7:
                            self.board.assign_robber()
                player.move_robber()
                
            #give resources to each players
            player.buy_road()
            player.buy_settlements()
            player.upgrade_settlement()
            

        def rounds(self):
            while True:
                for player in self.players:
                    turn(self.players[player])
                    self.winning_condition=declare_winner(player)
                    if self.winning_condition!=0:
                        break
                    print(f'the scores are {self.scores}')
            print(f'the scores are {self.scores}')

            
                    




























