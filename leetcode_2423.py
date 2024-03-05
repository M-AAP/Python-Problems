def is_eq_freq(word):
    letter_dict = {}
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    lowest = min(letter_dict, key=letter_dict.get)
    highest = max(letter_dict, key=letter_dict.get)

    return letter_dict[lowest] == letter_dict[highest]

def equalFrequency(self, word):
    word_length = len(word)
    removed_list = []
    for i in range(len(word)):
        removed = word.replace(word[i],"",1)
        removed_list.append(removed)

    is_eq_freq_list = map(is_eq_freq, removed_list)

    if True in is_eq_freq_list:
        return True
    else:
        return False
    
            
        
