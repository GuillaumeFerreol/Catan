import numpy as np
from math import sqrt
import random




class Player:
    def __init__(self, name, settlements, roads):
        self.name=name
        self.resources ={'brick': 20, 'grain':20, 'lumber': 20, 'ore':20, 'wool':20} #Resources (initialized as 0) 
        self.points=0
        self.settlements=[]
        self.roads=[]
        self.image_roads=[]
        self.image_settlement=None
        self.images_city=None
        self.available_settlements=[s for s in settlements]
        self.available_roads=[r for r in roads]



    def buy_road(self, road, round):
        road.owner=self.name
        self.roads.append(road)
        if round==1:
            self.resources['brick']-=1
            self.resources['lumber']-=1


    def buy_settlement(self,  settlement, round):
        settlement.owner=self.name
        settlement.multiplier=1
        self.settlements.append(settlement)
        self.points+=1
        if round==1:
            self.resources['brick']-=1
            self.resources['lumber']-=1
            self.resources['wool']-=1
            self.resources['grain']-=1

    def upgrade_settlement(self, settlement):
        settlement.upgrade()
        self.points+=1
        self.resources['ore']-=3
        self.resources['grain']-=2





class Robber:
    def __init__(self):
        self.region=None



class Region:

    types_to_resources={'4': 'brick', '3':'grain', '1':'lumber', '5':'ore', '2':'wool', '6':'desert'}  #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)
    

    def __init__(self, id, dice_number, region_type, coordinates):
        self.coordinates=coordinates
        self.region_type=region_type
        self.resource_type=self.types_to_resources[str(region_type)]
        self.id=id
        self.dice_number=dice_number
        self.robber=0
        self.vertices={p:  None for p in ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']}
        self.edges={p: None for p in ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']}

    


class Road:

    def __init__(self,coordinates, *args):
        self.owner=None
        self.regions=[name for name in args]
        self.connected_roads=[]
        self.connected_settlements=[]
        self.coordinates=coordinates



class Settlement:

    def __init__(self,coordinates, *args):
        self.multiplier=0 
        self.owner=None
        self.regions=[name for name in args]
        self.connected_roads=[]
        self.connected_settlements=[]
        self.coordinates=coordinates


    def upgrade(self):
        self.multiplier=2





class Board:

    def __init__(self):
        
        self.region_position=tuple(range(0, 19))
        self.region_types=[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5]#desert needs to have 7 
        random.shuffle(self.region_types)
        self.region_types.append(6)
        #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)

        self.region_coordinates={'1': (-1,-sqrt(3)), '2': (0,-sqrt(3)), '3':(1,-sqrt(3)), '4':(1.5,-sqrt(3/4)), '5': (2,0), '6':(1.5, sqrt(3/4)), '7':(1,sqrt(3)), '8':(0,sqrt(3)), '9':(-1,sqrt(3)), 
                                '10': (-1.5,sqrt(3/4)), '11': (-2,0), '12': (-1.5,-sqrt(3/4)), '13':(-0.5,-sqrt(3/4)), '14':(0.5,-sqrt(3/4)), '15': (1,0), '16':(0.5,sqrt(3/4)), '17':(-0.5,sqrt(3/4)), 
                                '18':(-1,0), '19':(0,0)} #change

        self.region_numbering=[('a',5) , ('b',2) , ('c',6), ('d',3), ('e',8), ('f',10), ('g',9), ('h',12), ('i',11), 
                            ('j',4), ('k',8), ('l',10), ('m',9), ('n',4), ('o',5), ('p',6), ('q',3), ('r',11), ('desert',7)]
        self.region_parameter=[(x,y) for x,y in zip(self.region_types,self.region_numbering)]
        random.shuffle(self.region_parameter)
        self.regions=[]
        self.roads=[]
        self.settlements=[]
        self.proximity_vector={(-0.5,-sqrt(3/4)):(('v4', 'v5', 'e4'), ('v2', 'v1', 'e1')), 
                                (0.5,-sqrt(3/4)):(('v4', 'v3', 'e3'), ('v6', 'v1', 'e6')), 
                                (1,0):(('v2', 'v3', 'e2'), ('v6', 'v5', 'e5')),
                                (0.5,sqrt(3/4)):(('v2', 'v1', 'e1'),('v4', 'v5', 'e4')), 
                                (-0.5, sqrt(3/4)):(('v6', 'v1', 'e6'),('v4', 'v3', 'e3')), 
                                (-1,0):(('v6', 'v5', 'e5'),('v2', 'v3', 'e2'))} 
        self.edge_coordinate_mapping={'e1':(0.25, sqrt(3/4)/2),'e2':(1/2, 0), 'e3':(0.25, -sqrt(3/4)/2), 'e4':(-0.25, -sqrt(3/4)/2), 'e5':(-1/2, -0), 'e6':(-0.25, sqrt(3/4)/2)}
        self.vertex_coordinate_mapping={'v1':(0, 1/sqrt(3)),'v2':(1/2, 1/(2*sqrt(3))), 'v3':(1/2, -1/(2*sqrt(3))), 'v4':(0, -1/sqrt(3)), 'v5':(-1/2, -1/(2*sqrt(3))), 'v6':(-1/2, 1/(2*sqrt(3)))}
        self.connection_vertices_vertices={'v1':('v6', 'v2'),'v2':('v1', 'v3'),'v3':('v2', 'v4'),
                                            'v4':('v3', 'v5'),'v5':('v4', 'v6'),'v6':('v5', 'v1')}
        self.connection_vertices_edges={'v1':('e6', 'e1'),'v2':('e1', 'e2'),'v3':('e2', 'e3'),
                                            'v4':('e3', 'e4'),'v5':('e4', 'e5'),'v6':('e5', 'e6')}
        self.connection_edges_vertices={'e1':('v1', 'v2'),'e2':('v2', 'v3'),'e3':('v3', 'v4'),
                                            'e4':('v4', 'v5'),'e5':('v5', 'v6'),'e6':('v6', 'v1')}
        self.connection_edges_edges={'e1':('e6', 'e2'),'e2':('e1', 'e3'),'e3':('e2', 'e4'),
                                            'e4':('e3', 'e5'),'e5':('e4', 'e6'),'e6':('e5', 'e1')}
        

        
    def setup_roads_settlements(self, region1, region2):
        self.vector=region2.coordinates[0]-region1.coordinates[0], region2.coordinates[1]-region1.coordinates[1]
        if self.vector in self.proximity_vector:
            if region1.edges[self.proximity_vector[self.vector][0][2]]==None:
                if region2.edges[self.proximity_vector[self.vector][1][2]]==None:
                    region1.edges[self.proximity_vector[self.vector][0][2]]=Road(tuple(np.array(region1.coordinates)+np.array(self.edge_coordinate_mapping[self.proximity_vector[self.vector][0][2]])),region1, region2 )
                    region2.edges[self.proximity_vector[self.vector][1][2]]=region1.edges[self.proximity_vector[self.vector][0][2]] #adding the already created road to the other region
                    self.roads.append(region1.edges[self.proximity_vector[self.vector][0][2]]) #adding the newly created road to the list of 
                else:
                    region2.edges[self.proximity_vector[self.vector][1][2]].regions.append(region1) #appending a region id to road.region which is a list containing all regions sharing that edge
                    region1.edges[self.proximity_vector[self.vector][0][2]]=region2.edges[self.proximity_vector[self.vector][1][2]]
        

            if region1.vertices[self.proximity_vector[self.vector][0][0]]==None:
                if region2.vertices[self.proximity_vector[self.vector][1][0]]==None:
                    region1.vertices[self.proximity_vector[self.vector][0][0]]=Settlement(tuple(np.array(region1.coordinates)+np.array(self.vertex_coordinate_mapping[self.proximity_vector[self.vector][0][0]])),region1, region2)
                    region2.vertices[self.proximity_vector[self.vector][1][0]]=region1.vertices[self.proximity_vector[self.vector][0][0]]
                    self.settlements.append(region1.vertices[self.proximity_vector[self.vector][0][0]]) #adding the newly created settlement to the list of settlements
                else:
                    region2.vertices[self.proximity_vector[self.vector][1][0]].regions.append(region1)
                    region1.vertices[self.proximity_vector[self.vector][0][0]]=region2.vertices[self.proximity_vector[self.vector][1][0]]
            else:
                region1.vertices[self.proximity_vector[self.vector][0][0]].regions.append(region2)
                region2.vertices[self.proximity_vector[self.vector][1][0]]=region1.vertices[self.proximity_vector[self.vector][0][0]]


            if region1.vertices[self.proximity_vector[self.vector][0][1]]==None:
                if region2.vertices[self.proximity_vector[self.vector][1][1]]==None:
                    region1.vertices[self.proximity_vector[self.vector][0][1]]=Settlement(tuple(np.array(region1.coordinates)+np.array(self.vertex_coordinate_mapping[self.proximity_vector[self.vector][0][1]])),region1, region2)
                    region2.vertices[self.proximity_vector[self.vector][1][1]]=region1.vertices[self.proximity_vector[self.vector][0][1]]
                    self.settlements.append(region1.vertices[self.proximity_vector[self.vector][0][1]]) #adding the newly created settlement to the list of settlements
                else:
                    region2.vertices[self.proximity_vector[self.vector][1][1]].regions.append(region1)
                    region1.vertices[self.proximity_vector[self.vector][1][0]]=region2.vertices[self.proximity_vector[self.vector][1][1]]
            else:
                region1.vertices[self.proximity_vector[self.vector][0][1]].regions.append(region2)
                region2.vertices[self.proximity_vector[self.vector][1][1]]=region1.vertices[self.proximity_vector[self.vector][0][1]]


    def connections(self): 
        for region in self.regions:
            for v in region.vertices:
                for k in [0,1]:
                    if region.vertices[self.connection_vertices_vertices[v][k]] not in region.vertices[v].connected_settlements:
                        region.vertices[v].connected_settlements.append(region.vertices[self.connection_vertices_vertices[v][k]])
                    if region.edges[self.connection_vertices_edges[v][k]] not in region.vertices[v].connected_roads:
                        region.vertices[v].connected_roads.append(region.edges[self.connection_vertices_edges[v][k]])

            for v in region.edges:
                for k in [0,1]:
                    if region.edges[self.connection_edges_edges[v][k]] not in region.edges[v].connected_roads:
                        region.edges[v].connected_roads.append(region.edges[self.connection_edges_edges[v][k]])
                    if region.vertices[self.connection_edges_vertices[v][k]] not in region.edges[v].connected_settlements:
                        region.edges[v].connected_settlements.append(region.vertices[self.connection_edges_vertices[v][k]])  
                        
                    
                    



    def setup_board(self):

        for k in range(0,19):
            self.regions.append(Region(self.region_parameter[k][1][0],self.region_parameter[k][1][1],self.region_parameter[k][0], self.region_coordinates[str(k+1)]))

        for i in range(len(self.regions)): #creating all inner roads and settlements and assigning them to the relative regions
            for j in range(len(self.regions)):
                self.setup_roads_settlements(self.regions[i],self.regions[j])

                # create outer roads and settlements and assign them to the respective region

        self.k=0
        for p in self.regions:
            for q in self.edge_coordinate_mapping:
                if p.edges[q]==None:
                    p.edges[q]=Road(tuple(np.array(p.coordinates)+np.array(self.edge_coordinate_mapping[q])),p)
                    self.roads.append(p.edges[q]) #adding the newly created road to the list of roads      
            for q in self.vertex_coordinate_mapping:
                if p.vertices[q]==None:
                    self.k+=1
                    p.vertices[q]=Settlement(tuple(np.array(p.coordinates)+np.array(self.vertex_coordinate_mapping[q])),p) 
                    self.settlements.append(p.vertices[q])#adding the newly created settlement to the list of settlements
        self.connections()
        self.robber=Robber()
        for x in self.regions:
            if x.dice_number == 7:
                self.robber.region=x
                x.robber=1

    
    def move_robber(self, region):
        self.robber.region.robber=0
        self.robber.region=region
        region.robber=1
        

    def round0_available_settlements(self, player):
        player.available_settlements = self.settlements.copy()
        self.settlements_to_remove=[]
        for v in player.available_settlements: #v stands for vertex
            if v.owner != None:
                self.settlements_to_remove.append(v)
        for v in self.settlements_to_remove:
             for cv in v.connected_settlements:
                 if cv in player.available_settlements:
                     player.available_settlements.remove(cv)

        for s in self.settlements_to_remove:
            player.available_settlements.remove(s)

                   


    def round0_available_roads (self, player):
        player.available_roads = self.roads.copy()
        self.roads_to_remove=[]
        for r in player.available_roads: #r stands for road
            if (player.name not in [cs.owner for cs in r.connected_settlements]) and (player.name not in [cr.owner for cr in r.connected_roads]):
                self.roads_to_remove.append(r)
            if r.owner!=None and (r not in self.roads_to_remove):
                self.roads_to_remove.append(r)
        for r in self.roads_to_remove:
            player.available_roads.remove(r)
            



    def round_available_settlements (self, player):
        player.available_settlements = self.settlements.copy()
        self.settlements_to_remove=[]
        for v in player.available_settlements: #v stands for vertex
            if v.owner != None:
                self.settlements_to_remove.append(v)
        for v in self.settlements_to_remove:
             for cv in v.connected_settlements:
                 if cv in player.available_settlements:
                     player.available_settlements.remove(cv) 

        for s in self.settlements_to_remove:
            player.available_settlements.remove(s)

        self.settlements_to_remove=[]
        for s in  player.available_settlements:
            if player.name not in [cr.owner for cr in s.connected_roads]: 
                self.settlements_to_remove.append(s)
        
        for s in self.settlements_to_remove:
            player.available_settlements.remove(s)
        


    def round_available_roads (self, player):
        player.available_roads = self.roads.copy()
        self.roads_to_remove=[]
        for r in player.available_roads: #r stands for road
            if (player.name not in [cs.owner for cs in r.connected_settlements]) and (player.name not in [cr.owner for cr in r.connected_roads]):
                self.roads_to_remove.append(r)
            if r.owner!=None and (r not in self.roads_to_remove):
                self.roads_to_remove.append(r)
        for r in self.roads_to_remove:
            player.available_roads.remove(r)






class Game:

    def __init__(self, board, GUI):
        self.board=board
        self.players={}
        for name in ['player1', 'player2', 'player3', 'player4']:
            self.players[name]=Player(name, self.board.settlements, self.board.roads)
            self.scores=[self.players[player].points for player in self.players]
            self.winning_condition=0
        self.current_player=None
        self.GUI=GUI


    #fix indentation
    def declare_winner(self, current_player):
        if self.players[current_player].points>5: 
            return 1
        else:
            return 0

    def start_game(self):
        self.round_zero()
        self.rounds()
        self.GUI.display_winner(self.current_player)

    def round_zero(self):
        for player in self.players:
            self.turn_zero(player)
        for player in [player for player in self.players][::-1]:
            self.turn_zero(player)
        self.give_resources_round0()


        
    def buy_settlement(self):
        self.GUI.show_buttons_settlements(round=0)
        
    def buy_road(self):
        self.GUI.show_buttons_roads(round=0)


    def rounds(self):
        while self.winning_condition==0:
            for player in self.players:
                self.turn(player)
                self.winning_condition=self.declare_winner(player)
                if self.winning_condition!=0:
                    return None
        


    def turn_zero(self, player):
        self.current_player=player
        self.GUI.update_player_label()
        self.buy_settlement()
        self.buy_road()


    def turn(self, player):
        self.current_player=player
        self.GUI.update_player_label()
        self.dice_result= random.randint(1,6)+random.randint(1,6)
        self.GUI.update_dice_roll(self.dice_result)
        self.give_resources(self.dice_result)
        self.GUI.update_player_resources()
        if self.dice_result==7:
            self.GUI.action_place_robber()
        self.GUI.other_actions()

    def give_resources_round0(self):
        for player in self.players:
            self.get_resources_round0(self.players[player].settlements[1])

    def give_resources(self, dice):
        if dice==7:
            pass
        for player in self.players:
            for s in self.players[player].settlements:
                self.get_resources(s, dice)

    def get_resources_round0(self, settlement):
        for region in set(settlement.regions):
            if region.resource_type=='desert':
                continue
            self.players[settlement.owner].resources[region.resource_type]+=1*settlement.multiplier

    def get_resources(self, settlement, dice_result):
        for region in set(settlement.regions):
            if region.resource_type=='desert':
                continue
            if region.robber==1:
                continue
            if region.dice_number==dice_result:
                self.players[settlement.owner].resources[region.resource_type]+=1*settlement.multiplier
        
      
        
            





