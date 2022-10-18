# Catan


Python Project

Versions
Version 1 (easy)
The easy version of the project will include the Catan game with the following rules:
Objective: get 10 points
Settlement construction 
Road construction
Dynamic number of players (from 2-4)
Dice rolling
Fixed board
Fixed course of actions per turn
No visuals (map)
Version 2 (medium)
The medium version of the project will include the Catan game with the following rules:
Objective: get 10 points
Settlement construction 
Road construction
Dynamic number of players (from 2-4)
Dice rolling
Random board
Visuals (map)
Version 3 (hard)
The hard version of the project will include the Catan game with the following rules:
Objective: get 10 points
Settlement construction 
Road construction
Dynamic number of players (from 2-4)
Dice rolling
Random board
Visuals (map)
add ports
Add development cards
Trades
Ports 
Fair board
Limited number of settlements 




Classes



Player

    Attributes (version 3)
        Name 
        Resources (initialized as 0)
        Regions (initialized as 0)
        Points
        Settlements
        Cities
        Roads
        (Ports)

    Methods (version 3)
        Pass the round
        Roll dice
        Buy roads
        Buy settlements
        Upgrade settlements → to cities
        Move the robber
        (Trade with players)
        (Trade with bank)
        (Accept trade)
        (Refuse trade)
        (Buy development card)



Region

    Attributes (version 3)
        Resource 
        Position on the board
        Number 
        Owner(s) (dictionary with key: player name and value: 0/1 for town/city)
        Robber 
        Vertices (initialized as a dictionary [0-5])
        Edges (initialized as a dictionary [0-5])
        (Ports)

    Methods (version 3)
        Give resources to players



Road

    Attributes (version 3)
        Owner
        Regions it belongs to 


    Methods (version 3)
        Assign_owner
        Assign_region
        Get_owner
        Get_regions



Settlement (town/city)

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



    Board

    Attributes (version 3)
        Regions (list of regions)
        Methods (version 3)
        Assign robber
        Setup



Game

    Attributes (version 3)
        Players (list) 

    Methods (version 3)
        Declare winner
        Round (ask actions to each player)






