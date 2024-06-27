"""
P: Write a program that takes a word and a list of possible anagrams and selects the correct sub-list that contains the anagrams of the word.

E:
detector = Anagram("listen")
    anagrams = detector.match(["enlists", "google", "inlets", "banana"])
    self.assertEqual(["inlets"], anagrams)
    
- Anagrams are case insensitive
- Multiple strings that match should be in the returned sublist
- Each anagram must have only 1 of each letter (ex. if there's two As in 1 word but only 1 in the other its not an anagram)
- Identical words are not anagrams

D: 
Input: String (original string), list of strings (possible anagrams)
Output: List of strings (validated anagrams)

A:
Create empty dictionary 
For word
    If letter not in dictionary, assign count of 1
    If letter in dictionary, increment count 
For each potential anagram:
    If letter not in dictionary, assign count of 1
    If letter in dictionary, increment count 

For comparison:
    Convert each dictionary to list of tuples. 
    Convert to a list and then sort. The list must then be equal to

"""
import pdb 

class Anagram:
    def __init__(self, string):
        self.string = string
        
    def match(self, list_of_possible_anagrams):
        return [possible_anagram for possible_anagram in list_of_possible_anagrams if self.is_anagram(possible_anagram)]
        
    def is_anagram(self, possible_anagram):
        if self.string.lower() == possible_anagram.lower():
            return False
        
        original_string_sorted_char_count_tuples, possible_anagram_sorted_char_count_tuples = sorted(list(self.letter_dict(self.string.lower()).items())), sorted(list(self.letter_dict(possible_anagram.lower()).items()))
        return original_string_sorted_char_count_tuples == possible_anagram_sorted_char_count_tuples
        
    @staticmethod
    def letter_dict(string):
        letter_dict = {}
        for letter in string:
            letter_dict[letter] = letter_dict.get(letter, 0) + 1 
        
        return letter_dict