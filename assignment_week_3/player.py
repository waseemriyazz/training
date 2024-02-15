class Player:
    def __init__(self, name , marker) :
        self.name = name 
        self.marker = marker

def get_player_name():
    
    name = input("Enter your name : ")
    assert len(name) == 1
    
        