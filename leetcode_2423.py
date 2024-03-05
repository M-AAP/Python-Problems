def is_eq_freq(word): # a function which tells you if each letter in the word has the same frequency
    letter_freq_dict = {} # Create a dictionary which will store the frequency of each letter in the word
    for letter in word:
        if letter in letter_freq_dict:
            letter_freq_dict[letter] += 1
        else:
            letter_freq_dict[letter] = 1
    lowest = min(letter_freq_dict, key=letter_freq_dict.get)
    highest = max(letter_freq_dict, key=letter_freq_dict.get)

    return letter_freq_dict[lowest] == letter_freq_dict[highest] 
'''    
If the smallest and largest values of the dict are equal then all values must be the same
I.e. each letter has the same frequency
'''

class Solution(object):
    def equalFrequency(self, word):
        word_length = len(word)
        removed_list = [] # create a list of all the possible combinations of removing one letter from the word
        for i in range(word_length):
            removed = word.replace(word[i],"",1)
            removed_list.append(removed)

        is_eq_freq_list = map(is_eq_freq, removed_list) # a list containing whether each word has equal frequency or not

        if True in is_eq_freq_list: # if even one of those words has all letters of equal frequency then return True and False otherwise 
            return True
        else:
            return False
