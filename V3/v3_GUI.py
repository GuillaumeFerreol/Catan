import tkinter as tk
from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
import numpy as np
from math import sqrt
import random


from v3_classes.classes import *



#This is the graphical user interface

class GUI:
    def __init__(self):
        self.board=Board()
        self.master = tk.Tk()
        self.game=Game(self.board, self)
        self.var=tk.IntVar()
        self.var_end_turn=tk.IntVar()
        self.round=0
        
        self.frame = tk.LabelFrame(self.master,relief = tk.FLAT)
        self.frame.grid(sticky = tk.NSEW)

        self.map = tk.Canvas(
            self.frame, 
            highlightthickness = 0, background = "dodgerblue",
            width = 1200, height = 1000, takefocus = 1,
            scrollregion = "-600 -500 600 500")
        self.map.grid(sticky = tk.NSEW, row=0, column=0)


        self.panel = tk.Canvas(
            self.frame, 
            highlightthickness = 0, background = "wheat",
            width = 500, height = 1000, takefocus = 1)
        self.panel.grid(sticky = tk.NSEW, row=0, column=1)

        self.rescale=195

        self.button_robber=dict()
        self.button_settlement=dict()
        self.button_city=dict()
        self.button_road=dict()


        self.robber = PhotoImage(file="V3/PNGs/Additional_elements/robber.png")

        
        
        self.start_button= Button(self.panel, text='START GAME', command=self.start_game, bg="green")
        self.start_button.place(in_=self.panel,x=200,y=450, height=100, width=100 )

        for player in self.game.players:
            self.game.players[player].image_roads.append(PhotoImage(file=f"V3/PNGs/builds/{ self.game.players[player].name}/road1.png"))
            self.game.players[player].image_roads.append(PhotoImage(file=f"V3/PNGs/builds/{ self.game.players[player].name}/road2.png"))
            self.game.players[player].image_roads.append(PhotoImage(file=f"V3/PNGs/builds/{ self.game.players[player].name}/road3.png"))
            self.game.players[player].image_city = PhotoImage(file=f"V3/PNGs/builds/{ self.game.players[player].name}/city.png")
            self.game.players[player].image_settlement=PhotoImage(file=f"V3/PNGs/builds/{ self.game.players[player].name}/colony.png")


        self.road_rotation={(0.25, round(sqrt(3/4)/2,10)): 1, (1/2, 0): 0, (0.25, round(-sqrt(3/4)/2,10)): 2, (-0.25, round(-sqrt(3/4)/2,10)): 1, (-1/2, -0): 0, (-0.25, round(sqrt(3/4)/2,10)): 2}
        
        self.RGB_players={'player1': 'green3', 'player2': 'red', 'player3': 'MediumOrchid2', 'player4': 'DodgerBlue2'}



    #creating the map when pressing the button 'start game'
    def start_game(self):
        self.start_button.destroy()
        self.board.setup_board()

        self.resource_type = dict()
        self.number=dict()
        for region in self.board.regions:

            self.resource_type[region]=ImageTk.PhotoImage(Image.open(f"V3/PNGs/Resources/{region.resource_type}.png").resize((200,226)))
            self.number[region] = ImageTk.PhotoImage(Image.open(f"V3/PNGs/Numbers/{region.dice_number}.png").resize((220,249)))
        self.setup_map()
        self.setup_panel()
        self.game.start_game()



        
    #moving the robber to a given region
    def move_robber(self,region):
        self.map.move(self.robber_image, (region.coordinates[0]-self.board.robber.region.coordinates[0])*self.rescale, (region.coordinates[1]-self.board.robber.region.coordinates[1])*self.rescale)
        self.board.move_robber(region)
        for x in self.button_robber.values():
            x.state(['disabled'])
            x.place_forget()
        self.enable_button(self.end_action_button)




    #placing settlements, roads and cities were the user clicked on the map
    def place_settlement(self,settlement):
        self.settlement_image=self.game.players[self.game.current_player].image_settlement
        self.game.players[self.game.current_player].buy_settlement(settlement, self.round) #replace with buy settlement method from player
        self.update_player_resources()
        self.map.create_image(settlement.coordinates[0]*self.rescale, settlement.coordinates[1]*self.rescale, image = self.settlement_image)
        for x in self.button_settlement.values():
            x.place_forget()
        self.enable_button(self.end_action_button)

    def place_city(self,settlement):
        self.city_image=self.game.players[self.game.current_player].image_city
        self.game.players[self.game.current_player].upgrade_settlement(settlement) #replace with buy settlement method from player
        self.update_player_resources()
        self.map.create_image(settlement.coordinates[0]*self.rescale, settlement.coordinates[1]*self.rescale, image = self.city_image)
        for x in self.button_city.values():
            x.place_forget()
        self.enable_button(self.end_action_button)


    def place_road(self, road):
        self.vector=(round(road.coordinates[0]-road.regions[0].coordinates[0],10), round(road.coordinates[1]-road.regions[0].coordinates[1],10) )
        self.game.players[self.game.current_player].buy_road(road, self.round) #replace with buy settlement method from player
        self.update_player_resources()
        self.road_image=self.game.players[self.game.current_player].image_roads[self.road_rotation[self.vector]]
        self.map.create_image(road.coordinates[0]*self.rescale, road.coordinates[1]*self.rescale, image = self.road_image)
        for x in self.button_road.values():
            x.place_forget()
        self.enable_button(self.end_action_button)      







    def place_image_region(self, region):
        self.map.create_image(region.coordinates[0]*self.rescale, region.coordinates[1]*self.rescale, image = self.resource_type[region])
        self.map.create_image(region.coordinates[0]*self.rescale, region.coordinates[1]*self.rescale, image = self.number[region])
        self.button_robber[region]= ttk.Button(self.map, text='move here',command=lambda : self.move_robber(region))
        self.button_robber[region].place(in_=self.map, x=region.coordinates[0]*self.rescale, y=region.coordinates[1]*self.rescale)
        self.button_robber[region].place_forget()
    




    #creating the buttons for settlements and cities (same coordinates since a city is an upgrades settlement) 
    def create_button_vertices(self, settlement, city):
        if city==0:
            self.button_settlement[settlement]=ttk.Button(self.map ,text='set',command=lambda : self.place_settlement(settlement))
            self.button_settlement[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale, y=settlement.coordinates[1]*self.rescale)
            self.button_settlement[settlement].place_forget()
        if city==1:
            self.button_city[settlement]=ttk.Button(self.map ,text='city',command=lambda : self.place_city(settlement))
            self.button_city[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale, y=settlement.coordinates[1]*self.rescale+480)
            self.button_city[settlement].place_forget()

    #creating the buttons for roads
    def create_button_edges(self, road):
        self.button_road[road]=ttk.Button(self.map,text='road',command=lambda : self.place_road(road))
        self.button_road[road].place(in_=self.map, x=road.coordinates[0]*self.rescale, y=road.coordinates[1]*self.rescale)
        self.button_road[road].place_forget()






    #showing the button on each region to move the robber
    def show_buttons_robber(self):
        for region in self.button_robber:
            self.button_robber[region].place(in_=self.map, x=region.coordinates[0]*self.rescale+570, y=region.coordinates[1]*self.rescale+480)
            self.button_robber[region].state(['!disabled'])
        self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
    


    #showing buttons to place settlements, cities and roads after performing some checks (enough resources 
    # and spot available to build for the current player)
    def show_buttons_settlements(self, round=1):
        self.current_player=self.game.current_player
        if round==0:
            self.board.round0_available_settlements(self.game.players[self.current_player])
            for settlement in self.game.players[self.current_player].available_settlements:#change to available button settlements
                self.button_settlement[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale+570, y=settlement.coordinates[1]*self.rescale+480)
            self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
        else:
            self.board.round_available_settlements(self.game.players[self.current_player])
            if (self.game.players[self.current_player].resources['brick']>0 and self.game.players[self.current_player].resources['grain']>0 
            and self.game.players[self.current_player].resources['wool']>0 and self.game.players[self.current_player].resources['lumber']>0):   
                if len(self.game.players[self.current_player].available_settlements)!=0:
                    for settlement in self.game.players[self.current_player].available_settlements:#change to available button settlements
                        self.button_settlement[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale+570, y=settlement.coordinates[1]*self.rescale+480)
                    self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                else:
                    self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                    self.enable_button(self.end_action_button)
            else:
                self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                self.enable_button(self.end_action_button)
        self.var.set(0)
        self.end_action_button.wait_variable(self.var)
        

    def show_buttons_roads(self, round=1):
        self.current_player=self.game.current_player
        if round==0:
            self.board.round0_available_roads(self.game.players[self.current_player])
            for road in self.game.players[self.current_player].available_roads:
                    self.button_road[road].place(in_=self.map, x=road.coordinates[0]*self.rescale+570, y=road.coordinates[1]*self.rescale+480)
            self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
        else:
            self.board.round_available_roads(self.game.players[self.current_player])
            if self.game.players[self.current_player].resources['brick']>0 and self.game.players[self.current_player].resources['lumber']>0:
                if len(self.game.players[self.current_player].available_roads)!=0:
                    for road in self.game.players[self.current_player].available_roads:
                        self.button_road[road].place(in_=self.map, x=road.coordinates[0]*self.rescale+570, y=road.coordinates[1]*self.rescale+480)
                    self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                else:
                    self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                    self.enable_button(self.end_action_button)
            else:
                self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
                self.enable_button(self.end_action_button)
        
        self.var.set(0)
        self.end_action_button.wait_variable(self.var)


    def show_buttons_up_settlements(self):
        self.current_player=self.game.current_player
        if self.game.players[self.current_player].resources['ore']>2 and self.game.players[self.current_player].resources['grain']>1:
            for settlement in self.game.players[self.current_player].settlements:
                    if settlement.multiplier==1:
                        self.button_city[settlement].place(in_=self.map, x=settlement.coordinates[0]*self.rescale+570, y=settlement.coordinates[1]*self.rescale+480)
            self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button, self.end_action_button)
        else:
            self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
            self.enable_button(self.end_action_button)
        self.var.set(0)
        self.end_action_button.wait_variable(self.var)
    






    def disable_button(self, *args):
        for button in args:
            button.state(['disabled'])

    def enable_button(self, *args):
        for button in args:
            button.state(['!disabled'])    
    
    def end_action(self):
        self.var.set(1)
        self.disable_button(self.end_action_button)
        if self.round==0:
            self.enable_button(self.end_turn_button)
        else:
            self.enable_button(self.end_turn_button, self.buy_settlement, self.buy_road, self.up_settlement)
        

    def end_turn(self):
        self.var_end_turn.set(1)
        self.disable_button(self.end_turn_button)



    def action_place_robber(self):
        self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button, self.end_action_button)
        self.enable_button(self.place_robber)
        self.var.set(0)
        self.end_action_button.wait_variable(self.var)



    def other_actions(self):
        self.round=1
        self.enable_button(self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button)
        self.var_end_turn.set(0)
        self.end_turn_button.wait_variable(self.var_end_turn)
        


    def update_player_label(self):
        self.current_player_label.config(text=f'CURRENT PLAYER : {self.game.current_player}', foreground=self.RGB_players[self.game.current_player])

    def update_player_resources(self):
        self.player_resources.config(text=f'{self.game.players[self.game.current_player].resources}')

    def update_dice_roll(self, dice):
        self.dice.config(text=f'dice roll: {dice}')


    def display_winner(self, winner):
        self.winner=Label(self.panel, text=f'THE WINNER IS {winner}', background = "wheat")
        self.winner.place(in_=self.panel, x=150, y=700)
        self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button, self.end_action_button)


    #creating the buttons for the panel (right part of the window)
    def setup_panel(self):
        self.place_robber=ttk.Button(self.panel, text='MOVE ROBBER',command=self.show_buttons_robber )
        self.place_robber.place(in_=self.panel, x=50, y=200)
        self.buy_road=ttk.Button(self.panel, text='BUY ROAD',command=self.show_buttons_roads)
        self.buy_road.place(in_=self.panel, x=50, y=50)
        self.buy_settlement=ttk.Button(self.panel, text='BUY SETTLEMENT',command=self.show_buttons_settlements )
        self.buy_settlement.place(in_=self.panel, x=50, y=100)
        self.up_settlement=ttk.Button(self.panel, text='UPGRADE SETTLEMENT',command=self.show_buttons_up_settlements )
        self.up_settlement.place(in_=self.panel, x=50, y=150)
        self.end_turn_button=ttk.Button(self.panel, text='END TURN',command=self.end_turn )
        self.end_turn_button.place(in_=self.panel, x=50, y=250)
        self.end_action_button=ttk.Button(self.panel, text='END ACTION',command=self.end_action )
        self.end_action_button.place(in_=self.panel, x=50, y=300)
        self.disable_button(self.place_robber, self.buy_settlement, self.buy_road, self.up_settlement, self.end_turn_button, self.end_action_button)
        self.current_player_label=ttk.Label(self.panel, text=f'CURRENT PLAYER : {self.game.current_player}', background = "wheat")
        self.current_player_label.place(in_=self.panel, x=50, y=350)

        self.player_label=ttk.Label(self.panel, text='current player resources:', background = "wheat")
        self.player_label.place(in_=self.panel, x=50, y=500)
        self.player_resources=ttk.Label(self.panel, text=f'', background = "wheat")
        self.player_resources.place(in_=self.panel, x=50, y=520)

        self.dice=ttk.Label(self.panel, text='dice roll:', background = "wheat")
        self.dice.place(in_=self.panel, x=300, y=50)


    def setup_map(self):
        for region in self.board.regions:
            self.place_image_region(region)
        
        for settlement in self.board.settlements:
            self.create_button_vertices(settlement, city=0)
            self.create_button_vertices(settlement, city=1)
        for road in self.board.roads:
            self.create_button_edges(road)



        self.robber_image=self.map.create_image(self.board.robber.region.coordinates[0]*self.rescale, self.board.robber.region.coordinates[1]*self.rescale, image = self.robber)
        


    def build_GUI(self):
        self.master.mainloop()



if __name__=='__main__':
    window=GUI()
    window.build_GUI()