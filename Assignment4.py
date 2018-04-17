#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience
    
    def get_name(self):
        return self.__name
    
    def get_experience(self):
        return self.__experience
    
    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))
#intializes player list and works with it 
class Game:
  players_list=[]
  def __init__(self, players_list):
    self.__players_list=players_list
  
  #sorts list by experience using sorted method
  def sort_players_based_on_experience(self):
    new_list=sorted(self.__players_list, key=lambda x:x.get_experience(), reverse=True)
    return new_list
  
  #shifts a player from given position to another
  def shift_player_to_new_position(self, old_index_position, new_index_position):
    player = self.__players_list.pop(old_index_position)
    self.__players_list.insert(new_index_position, player)
    
    return self.__players_list
    
  def display_player_details(self):
    for i in self.__players_list:
      print(str(i.get_name()) + ", " + str(i.get_experience()))
      
  
player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,   player9,player10,player11]


gameObj = Game(players_list)
sorted_list = gameObj.sort_players_based_on_experience()
gameObj.display_player_details()
exchanged_list =gameObj.shift_player_to_new_position(1,3)
print("----------------------")
gameObj.display_player_details()
