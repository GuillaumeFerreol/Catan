import numpy as np
from math import sqrt
import random
import tkinter as tk
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk




class Player:
    def __init__(self, name):
        self.name=name
        self.resources ={'brick': 0, 'grain':0, 'lumber': 0, 'ore':0, 'wool':0} #Resources (initialized as 0) 
        self.points=0
        self.settlements=[]
        self.roads=[]
        self.image_roads=[]
        self.image_settlement=None
        self.images_city=None

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
        






class Game:

    def __init__(self, board, GUI):
        self.players={}
        for name in ['player1', 'player2', 'player3', 'player4']:
            self.players[name]=Player(name)
            self.scores=[self.players[player].points for player in self.players]
            self.winning_condition=0
            self.board=board
        self.GUI=GUI






class GUI:
    def __init__(self):
        self.board=Board()
        self.master = tk.Tk()
        self.game=Game(self.board, self)
        
        
        self.frame = tk.LabelFrame(self.master, text = "Coords Here", relief = tk.FLAT)
        self.frame.grid(sticky = tk.NSEW)

        self.map = tk.Canvas(
            self.frame, 
            highlightthickness = 0, background = "dodgerblue",
            width = 1000, height = 1000, takefocus = 1,
            scrollregion = "-500 -500 500 500")
        self.map.grid(sticky = tk.NSEW, row=0, column=0)


        self.panel = tk.Canvas(
            self.frame, 
            highlightthickness = 0, background = "wheat",
            width = 500, height = 1000, takefocus = 1)
        self.panel.grid(sticky = tk.NSEW, row=0, column=1)

        self.rescale=195

        self.button_robber=dict()
        self.button_settlement=dict()
        self.button_road=dict()


        self.robber = PhotoImage(file="V2/PNGs/Additional_elements/robber.png")

        

        self.start_button= Button(self.panel, text='START GAME', command=self.start_game, bg="green")
        self.start_button.place(in_=self.panel,x=200,y=450, height=100, width=100 )


        self.robber = PhotoImage(file="V2/PNGs/Additional_elements/robber.png")
        for player in self.game.players:
            self.game.players[player].image_roads.append(PhotoImage(file=f"V2/PNGs/builds/{ self.game.players[player].name}/road1.png"))
            self.game.players[player].image_roads.append(PhotoImage(file=f"V2/PNGs/builds/{ self.game.players[player].name}/road2.png"))
            self.game.players[player].image_roads.append(PhotoImage(file=f"V2/PNGs/builds/{ self.game.players[player].name}/road3.png"))
            self.game.players[player].image_city = PhotoImage(file=f"V2/PNGs/builds/{ self.game.players[player].name}/city.png")
            self.game.players[player].image_settlement=PhotoImage(file=f"V2/PNGs/builds/{ self.game.players[player].name}/colony.png")


        self.road_rotation={(0.25, round(sqrt(3/4)/2,10)): 1, (1/2, 0): 0, (0.25, round(-sqrt(3/4)/2,10)): 2, (-0.25, round(-sqrt(3/4)/2,10)): 1, (-1/2, -0): 0, (-0.25, round(sqrt(3/4)/2,10)): 2}
        


    def start_game(self):
        self.start_button.destroy()
        self.board.setup_board()

        self.resource_type = dict()
        self.number=dict()
        for region in self.board.regions:

            self.resource_type[region]=ImageTk.PhotoImage(Image.open(f"V2/PNGs/Resources/{region.resource_type}.png").resize((200,226)))
            self.number[region] = ImageTk.PhotoImage(Image.open(f"V2/PNGs/Numbers/{region.dice_number}.png").resize((220,249)))
        self.setup_map()
        self.setup_panel()




        
 
    def move_robber(self,region):
        self.map.move(self.robber_image, (region.coordinates[0]-self.board.robber.region.coordinates[0])*self.rescale, (region.coordinates[1]-self.board.robber.region.coordinates[1])*self.rescale)
        self.board.move_robber(region)
        for x in self.button_robber.values():
            x.state(['disabled'])
            x.place_forget()
        self.enable_button(self.place_robber)

    def place_settlement(self,settlement, player=None):
        self.settlement_image=self.game.players['player1'].image_settlement
        self.map.create_image(settlement.coordinates[0]*self.rescale, settlement.coordinates[1]*self.rescale, image = self.settlement_image)
        for x in self.button_settlement.values():
            x.place_forget()
        self.enable_button(self.place_robber)

    def place_road(self, road, player=None):
        self.vector=(round(road.coordinates[0]-road.regions[0].coordinates[0],10), round(road.coordinates[1]-road.regions[0].coordinates[1],10) )
        self.road_image=self.game.players['player1'].image_roads[self.road_rotation[self.vector]]
        self.map.create_image(road.coordinates[0]*self.rescale, road.coordinates[1]*self.rescale, image = self.road_image)
        for x in self.button_road.values():
            x.place_forget()
        self.enable_button(self.place_robber)       



    def place_image_region(self, region):
        self.map.create_image(region.coordinates[0]*self.rescale, region.coordinates[1]*self.rescale, image = self.resource_type[region])
        self.map.create_image(region.coordinates[0]*self.rescale, region.coordinates[1]*self.rescale, image = self.number[region])
        self.button_robber[region]= ttk.Button(self.map, text='move here',command=lambda : self.move_robber(region))
        self.button_robber[region].place(in_=self.map, x=region.coordinates[0]*self.rescale+480, y=region.coordinates[1]*self.rescale+480)
        self.button_robber[region].place_forget()
    
    def create_button_vertices(self, settlement):
        self.button_settlement[settlement]=ttk.Button(self.map ,text='set',command=lambda : self.place_settlement(settlement))
        self.button_settlement[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale+480, y=settlement.coordinates[1]*self.rescale+480)
        self.button_settlement[settlement].place_forget()

    def create_button_edges(self, road):
        self.button_road[road]=ttk.Button(self.map,text='road',command=lambda : self.place_road(road))
        self.button_road[road].place(in_=self.map, x=road.coordinates[0]*self.rescale+480, y=road.coordinates[1]*self.rescale+480)
        self.button_road[road].place_forget()


    def show_buttons_robber(self):
        for region in self.button_robber:
            self.button_robber[region].place(in_=self.map, x=region.coordinates[0]*self.rescale+480, y=region.coordinates[1]*self.rescale+480)
            self.button_robber[region].state(['!disabled'])
        self.disable_button(self.place_robber)
    
    def show_buttons_settlements(self):
        for settlement in self.button_settlement:#change to available button settlements
            self.button_settlement[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale+480, y=settlement.coordinates[1]*self.rescale+480)
        self.disable_button(self.place_robber)

    def show_buttons_roads(self):
        for road in self.button_road:
            self.button_road[road].place(in_=self.map, x=road.coordinates[0]*self.rescale+480, y=road.coordinates[1]*self.rescale+480)
        self.disable_button(self.place_robber)
    
    def disable_button(self, *args):
        for button in args:
            button.state(['disabled'])

    def enable_button(self, *args):
        for button in args:
            button.state(['!disabled'])    


    def setup_panel(self):
        self.place_robber=ttk.Button(self.panel, text='MOVE ROBBER',command=self.show_buttons_robber )
        self.place_robber.place(in_=self.panel, x=50, y=50)


    def setup_map(self):
        for region in self.board.regions:
            self.place_image_region(region)
        
        for settlement in self.board.settlements:
            self.create_button_vertices(settlement)
        for road in self.board.roads:
            self.create_button_edges(road)



        self.robber_image=self.map.create_image(self.board.robber.region.coordinates[0]*self.rescale, self.board.robber.region.coordinates[1]*self.rescale, image = self.robber)
        



    def build_GUI(self):

        self.master.mainloop()


if __name__=='__main__':
    window=GUI()
    window.build_GUI()
