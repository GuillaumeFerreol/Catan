import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import random




import numpy as np
from math import sqrt
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
 

        def buy_road(self, road):
            road.owner=self.name
            self.roads.append[road]
            self.resources['brick']-=1
            self.resources['lumber']-=1


        def buy_settlements(self,  settlement):
            settlement.owner=self.name
            self.settlements.append[settlement]
            self.resources['brick']-=1
            self.resources['lumber']-=1
            self.resources['wool']-=1
            self.resources['grain']-=1

        def upgrade_settlement(self, settlement):
            settlement.multiplier=2
            self.resources['ore']-=3
            self.resources['grain']-=2



            #ask region, player_to_rob, resource_to_rob
            #update region
            #update player resources
            pass

        #(Trade with players)
        #(Trade with bank)
        #(Accept trade)
        #(Refuse trade)
        #(Buy development card)

class Robber:
    def __init__(self):
        self.region=None



class Region:

    types_to_resources={'4': 'bricks', '3':'grain', '1':'lumber', '5':'ore', '2':'wool', '6':None}  #forest=1 (lumber), pasture=2 (wool), fields=3 (grain), hills=4 (brick), mountain=5 (ore), desert=6 (None)
    

    def __init__(self, id, dice_number, region_type, coordinates):
        self.coordinates=coordinates
        self.region_type=region_type
        self.resource_type=self.types_to_resources[str(region_type)]
        self.id=id
        self.dice_number=dice_number
        self.robber=0
        self.vertices={p:  None for p in ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']}
        self.edges={p: None for p in ['e1', 'e2', 'e3', 'e4', 'e5', 'e6']}

    




    # Attributes (version 3)

    #     Owner(s) (dictionary with key: player name and value: 0/1 for town/city)
    #     Vertices (initialized as a dictionary [0-5]) with value [owner, buildable, occupied]?
    #     Edges (initialized as a dictionary [0-5]) with value [owner, buildable, occupied]?
    #     (Ports)

    # Methods (version 3)
    #     Give resources to players



class Road:

    def __init__(self,coordinates, *args):
        self.owner=None
        self.regions=[name for name in args]
        self.level=0 #0=empty, 1=road exists
        self.connected_roads=[]
        self.connected_settlements=[]
        self.coordinates=coordinates

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
    def __init__(self,coordinates, *args):
        self.multiplier=0 #level = multiplier?
        self.owner=None
        self.regions=[name for name in args]
        self.level=0
        self.connected_roads=[]
        self.connected_settlements=[]
        self.coordinates=coordinates
        
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
                    region1.edges[self.proximity_vector[self.vector][0][2]]=Road(tuple(np.array(region1.coordinates)+np.array(self.edge_coordinate_mapping[self.proximity_vector[self.vector][0][2]])),region1.id, region2.id, )
                    region2.edges[self.proximity_vector[self.vector][1][2]]=region1.edges[self.proximity_vector[self.vector][0][2]] #adding the already created road to the other region
                    self.roads.append(region1.edges[self.proximity_vector[self.vector][0][2]]) #adding the newly created road to the list of 
                else:
                    region2.edges[self.proximity_vector[self.vector][1][2]].regions.append(region1.id) #appending a region id to road.region which is a list containing all regions sharing that edge
                    region1.edges[self.proximity_vector[self.vector][0][2]]=region2.edges[self.proximity_vector[self.vector][1][2]]
        

            if region1.vertices[self.proximity_vector[self.vector][0][0]]==None:
                if region2.vertices[self.proximity_vector[self.vector][1][0]]==None:
                    region1.vertices[self.proximity_vector[self.vector][0][0]]=Settlement(tuple(np.array(region1.coordinates)+np.array(self.vertex_coordinate_mapping[self.proximity_vector[self.vector][0][0]])),region1.id, region2.id)
                    region2.vertices[self.proximity_vector[self.vector][1][0]]=region1.vertices[self.proximity_vector[self.vector][0][0]]
                    self.settlements.append(region1.vertices[self.proximity_vector[self.vector][0][0]]) #adding the newly created settlement to the list of settlements
                else:
                    region2.vertices[self.proximity_vector[self.vector][1][0]].regions.append(region1.id)
                    region1.vertices[self.proximity_vector[self.vector][0][0]]=region2.vertices[self.proximity_vector[self.vector][1][0]]
            else:
                region1.vertices[self.proximity_vector[self.vector][0][0]].regions.append(region2.id)
                region2.vertices[self.proximity_vector[self.vector][1][0]]=region1.vertices[self.proximity_vector[self.vector][0][0]]


            if region1.vertices[self.proximity_vector[self.vector][0][1]]==None:
                if region2.vertices[self.proximity_vector[self.vector][1][1]]==None:
                    region1.vertices[self.proximity_vector[self.vector][0][1]]=Settlement(tuple(np.array(region1.coordinates)+np.array(self.vertex_coordinate_mapping[self.proximity_vector[self.vector][0][1]])),region1.id, region2.id)
                    region2.vertices[self.proximity_vector[self.vector][1][1]]=region1.vertices[self.proximity_vector[self.vector][0][1]]
                    self.settlements.append(region1.vertices[self.proximity_vector[self.vector][0][1]]) #adding the newly created settlement to the list of settlements
                else:
                    region2.vertices[self.proximity_vector[self.vector][1][1]].regions.append(region1.id)
                    region1.vertices[self.proximity_vector[self.vector][1][0]]=region2.vertices[self.proximity_vector[self.vector][1][1]]
            else:
                region1.vertices[self.proximity_vector[self.vector][0][1]].regions.append(region2.id)
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
                    p.edges[q]=Road(tuple(np.array(p.coordinates)+np.array(self.edge_coordinate_mapping[q])),p.id)
                    self.roads.append(p.edges[q]) #adding the newly created road to the list of roads      
            for q in self.vertex_coordinate_mapping:
                if p.vertices[q]==None:
                    self.k+=1
                    p.vertices[q]=Settlement(tuple(np.array(p.coordinates)+np.array(self.vertex_coordinate_mapping[q])),p.id) 
                    self.settlements.append(p.vertices[q])#adding the newly created settlement to the list of settlements
        self.connections()
        self.robber=Robber()
        for x in self.regions:
            if x.dice_number == 7:
                self.robber.location=x
                x.robber=1
        









if __name__=='__main__':
    board=Board()
    board.setup_board()
    plt.figure(figsize= (10,10), dpi=80)
    plt.ylim(-3, 3)
    plt.xlim(-3,3)
    x=[x.coordinates[0] for x in board.regions]
    y=[x.coordinates[1] for x in board.regions]
    plt.scatter(x,y)
    x1=[x.coordinates[0] for x in board.settlements]
    y1=[x.coordinates[1] for x in board.settlements]
    plt.scatter(x1,y1, c='red')
    x3=[x.coordinates[0] for x in board.roads]
    y3=[x.coordinates[1] for x in board.roads]
    plt.scatter(x3,y3, c='green')
    plt.scatter(board.settlements[0].coordinates[0],board.settlements[0].coordinates[1], c='red')
    plt.show()
    
    plt.figure(figsize= (10,10), dpi=80)
    plt.ylim(-3, 3)
    plt.xlim(-3,3)
    plt.scatter(board.settlements[0].coordinates[0],board.settlements[0].coordinates[1], c='red')
    for x in board.settlements[0].connected_settlements:
        plt.scatter(x.coordinates[0], x.coordinates[1], c='green')
    for y in board.settlements[0].connected_roads:
        plt.scatter(y.coordinates[0], y.coordinates[1], c='blue')
    plt.show()

    plt.figure(figsize= (10,10), dpi=80)
    plt.ylim(-3, 3)
    plt.xlim(-3,3)
    plt.scatter(board.roads[1].coordinates[0],board.roads[1].coordinates[1], c='red')
    for x in board.roads[1].connected_settlements:
        plt.scatter(x.coordinates[0], x.coordinates[1], c='green')
    for y in board.roads[1].connected_roads:
        plt.scatter(y.coordinates[0], y.coordinates[1], c='blue')
    plt.show()

    

