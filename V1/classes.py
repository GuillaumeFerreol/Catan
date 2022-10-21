import numpy as np
from cmath import sqrt
import random




class Player:
    def __init__(self, name):
        self.name=name
        self.resources ={'brick': 0, 'grain':0, 'lumber': 0, 'ore':0, 'wool':0} #Resources (initialized as 0) 
        self.points=0
        self.settlements=[]
        self.roads=[]
        #(Ports)

    #Methods (version 3)
        def pass_round(self, user_answer):#Pass the round
                pass
        def roll_dice(self):
            return random.randint(1,6)+random.randint(1,6)

        def buy_road(self, road):
            #check resources

            #update road, player
            pass

        def buy_settlements(self,  settlement):
            #check resources
            #ask user where
            #update region, player
            pass

        def upgrade_settlement(self, settlement):
            #check resources
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
    

    def __init__(self, id,dice_number, region_type,  coordinates):
        self.coordinates=coordinates
        self.region_type=region_type
        self.resource_type=self.types_to_resources[region_type]
        self.id=id
        self.dice_number=dice_number
        self.robber=0
        self.vertices={p:  None for p in ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']}
        self.edges={p: None for p in ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']}

    def give_resources(self):
        if self.region_type==6 or self.robber!=0:
            pass

        for s in self.vertices:
            if s[0]!=None:
                s[0].resources[self.resource_type]+=1*s[2].multiplier

    def assign_vertex(self, vertex):
        pass

    def assign_edge(self, edge):
        pass


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

    def assign_owner(self, owner):
        self.owner=owner
        self.multiplier=1
        self.level=1

    def upgrade(self):
        self.level=2
        self.multiplier=2




    



class Board:

    def __init__(self):
        
        self.region_position=tuple(range(0, 19))
        self.region_types=[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6]#desert needs to have 7 
        random.shuffle(self.region_types)
        #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)

        self.region_coordinates={'1': (-1,-sqrt(3)), '2': (0,-sqrt(3)), '3':(1,-sqrt(3)), '4':(3.5,-sqrt(3/4)), '5': (2,0), '6':(3.5, sqrt(3/4)), '7':(3.5,sqrt(3/4)), '8':(1,sqrt(3)), '9':(-1,sqrt(3)), 
                                '10': (-3.5,sqrt(3/4)), '11': (-2,0), '12': (-3.5,-sqrt(3/4)), '13':(-0.5,-sqrt(3/4)), '14':(0.5,-sqrt(3/4)), '15': (1,0), '16':(0.5,sqrt(3/4)), '17':(-0.5,sqrt(3/4)), 
                                '18':(-1,0), '19':(0,0)} #change

        self.region_numbering=(('a',5) , ('b',2) , ('c',6), ('d',3), ('e',8), ('f',10), ('g',9), ('h',12), ('i',11), 
                            ('j',4), ('k',8), ('l',10), ('m',9), ('n',4), ('o',5), ('p',6), ('q',3), ('r',11))
        self.regions=[]
        self.proximity_vector={(-0.5,-sqrt(3/4)):(('v5', 'v4', 'e4'), ('v2', 'v1', 'e1')), 
                                (0.5,-sqrt(3/4)):(('v4', 'v3', 'e3'), ('v1', 'v6', 'e6')), 
                                (1,0):(('v3', 'v2', 'e2'), ('v6', 'v5', 'e5'))} 
        
    def assign_robber(self):
        self.region_list[random.randint(0,19)].robber==1

    def setup_roads_settlements(self, region1, region2):
        vector=region1.coordinates[0]-region2.coordinates[0], region1.coordinates[1]-region2.coordinates[1]
        if vector in self.proximity_vector:
            if self.proximity_vector[vector][1][2]==None:
                region1.edges[self.proximity_vector[vector][0][2]]=Road(region1.id, region2.id).regions
                region2.edges[self.proximity_vector[vector][1][2]]=region1.edges[self.proximity_vector[vector][0][2]]
            else:
                region2.edges[self.proximity_vector[vector][1][2]].append(region1.id)
                region1.edges[self.proximity_vector[vector][0][2]]=region2.edges[self.proximity_vector[vector][1][2]]

            if self.proximity_vector[vector][1][0]==None:
                region1.vertices[self.proximity_vector[vector][0][0]]=Settlement(region1.id, region2.id).regions
                region2.vertices[self.proximity_vector[vector][1][0]]=region1.vertices[self.proximity_vector[vector][0][0]]
            else:
                region2.vertices[self.proximity_vector[vector][1][0]].append(region1.id)
                region1.vertices[self.proximity_vector[vector][0][0]]=region2.vertices[self.proximity_vector[vector][1][0]]

            if self.proximity_vector[vector][1][1]==None:
                region1.vertices[self.proximity_vector[vector][0][1]]=Settlement(region1.id, region2.id).regions
                region2.vertices[self.proximity_vector[vector][1][1]]=region1.vertices[self.proximity_vector[vector][0][1]]
            else:
                region2.vertices[self.proximity_vector[vector][1][1]].append(region1.id)
                region1.vertices[self.proximity_vector[vector][1][0]]=region2.vertices[self.proximity_vector[vector][1][1]]


        if -vector in self.proximity_vector:
            if self.proximity_vector[-vector][1][2]==None:
                region1.edges[self.proximity_vector[-vector][0][2]]=Road(region1.id, region2.id).regions
                region2.edges[self.proximity_vector[-vector][1][2]]=region1.edges[self.proximity_vector[-vector][0][2]]
            else:
                region2.edges[self.proximity_vector[-vector][1][2]].append(region1.id)
                region1.edges[self.proximity_vector[-vector][0][2]]=region2.edges[self.proximity_vector[-vector][1][2]]

            if self.proximity_vector[-vector][1][0]==None:
                region1.vertices[self.proximity_vector[-vector][0][0]]=Settlement(region1.id, region2.id).regions
                region2.vertices[self.proximity_vector[-vector][1][0]]=region1.vertices[self.proximity_vector[-vector][0][0]]
            else:
                region2.vertices[self.proximity_vector[-vector][1][0]].append(region1.id)
                region1.vertices[self.proximity_vector[-vector][0][0]]=region2.vertices[self.proximity_vector[-vector][1][0]]

            if self.proximity_vector[-vector][1][1]==None:
                region1.vertices[self.proximity_vector[-vector][0][1]]=Settlement(region1.id, region2.id).regions
                region2.vertices[self.proximity_vector[-vector][1][1]]=region1.vertices[self.proximity_vector[-vector][0][1]]
            else:
                region2.vertices[self.proximity_vector[-vector][1][1]].append(region1.id)
                region1.vertices[self.proximity_vector[-vector][1][0]]=region2.vertices[self.proximity_vector[-vector][1][1]]            


        
        
        

    def setup_board(self):
        for k in range(len(self.region_coordinates)):
            self.regions.append(Region(self.region_numbering[k][0], self.region_numbering[k][1], self.region_types[k], 
        self.region_coordinates(str(self.region_position[k]))))

        for p in self.regions:
            for q in self.regions:
                if p is q:
                    continue
                self.setup_roads_settlements(p,q)
        
        self.regions=Region.instances
        self.roads=Road.instances
        self.settlements=Settlement.instances
        
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

            
                    




























