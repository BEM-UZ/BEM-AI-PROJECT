from Levenshtein import distance, ratio

def correct_word(word, word_list):
    """
    Given a word and a list of valid words, finds the closest matching word
    based on the Levenshtein distance and returns it. If no close match is found,
    returns the original word.
    """
    max_distance = 2  # Maximum distance to consider a close match
    closest_word = None
    closest_distance = max_distance + 1
    for valid_word in word_list:
        d = distance(word, valid_word)
        if d <= max_distance and d < closest_distance:
            closest_word = valid_word
            closest_distance = d
    if closest_word:
        return closest_word
    else:
        return word
    
print(correct_word("businnes studies",['business','rank']))