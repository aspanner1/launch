class Game:
    count = 0  # Class attribute to count instances

    def __init__(self, player_name):
        type(self).count += 1  # Increment count for each instance creation
        self._player_name = player_name
        
    def play(self):
        return f'Start the {self.__class__.__name__} game!'  # Include class name in the play message
    
    @property 
    def player_name(self):
        return self._player_name  # Accessor for player_name
    
    def __str__(self):
        return self.__class__.__name__  # String representation of the class name

class Bingo(Game):
    pass  # Inherits everything from Game

class Scrabble(Game):
    def __init__(self, player_1, player_2):
        super().__init__(player_1)  # Initialize Game with player_1 as the player_name
        self._player_2 = player_2  # Additional attribute for Scrabble
    
    @property 
    def player_1(self):
        return self.player_name  # Use inherited player_name for player_1
    
    @property 
    def player_2(self):
        return self._player_2  # Accessor for player_2

# Resetting the count for testing
Game.count = 0

# Creating instances and testing outputs
bingo = Bingo('Bill')
print("Game count after Bingo:", Game.count)  # Should print 1
print(bingo.play())                           # Should print "Start the Bingo game!"
print("Player Name:", bingo.player_name)      # Should print "Bill"

scrabble = Scrabble('Jill', 'Sill')
print("Game count after Scrabble:", Game.count)  # Should print 2
print(scrabble.play())                           # Should print "Start the Scrabble game!"
print("Player 1:", scrabble.player_1)            # Should print "Jill"
print("Player 2:", scrabble.player_2)            # Should print "Sill"
