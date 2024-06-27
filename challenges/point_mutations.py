import pdb
"""
P: Given two strings, determine Hamming distance.
Hamming distance is number of differences between chars at same point.
Use shorter string, blanks do not count towards Hamming Distance.

E: 
self.assertEqual(0, DNA("").hamming_distance(""))

(3, DNA("ACT").hamming_distance("GGA"))

strand = "GGACGGATTCTGACCTGGACTAATTTTGGGG"
distance = "AGGACGGATTCTGACCTGGACTAATTTTGGGG"
self.assertEqual(19, DNA(strand).hamming_distance(distance))

Ignore extra length
strand = "GACTACGGACAGGGTAGGGAAT"
distance = "GACATCGCACACC"
self.assertEqual(5, DNA(strand).hamming_distance(distance))

Original strand not modified 
dna = DNA("AGACAACAGCCAGCCGCCGGATT")
    self.assertEqual(1, dna.hamming_distance("AGGCAA"))
    self.assertEqual(4, dna.hamming_distance("AGACATCTTTCAGCCGCCGGATTAGGCAA"))
    self.assertEqual(1, dna.hamming_distance("AGG"))
    
D: 
Argument 1: String 
Argument 2: String
Output: Integer 

A:
Iterate through both strings at the same time
If the char is different, add True to an array 
Length of the array is the hamming distance
"""

class DNA:
    def __init__(self, strand_string):
        self._strand_string = strand_string
        
    @property 
    def strand_string(self):
        return self._strand_string
    
    def __len__(self):
        return len(self.strand_string)
    
    def hamming_distance(self, other):
        if not isinstance(other, str):
            return NotImplementedError
        
        other = DNA(other)
        
        if len(self) <= len(other):
            shorter_string, longer_string = self.strand_string, other.strand_string
        elif len(self) > len(other):
            shorter_string, longer_string = other.strand_string, self.strand_string 

        hamming_distance = len([ True for i in range(0, len(shorter_string)) if shorter_string[i] != longer_string[i] ])
        
        return hamming_distance
    
        
        