def count_words(text):
    text_split = text.split()
    word_count = len(text_split)

    return word_count

def count_characters(text):
    characters = {}
    for c in text:
        c_lower = c.lower()
        if c_lower not in characters:
            characters[c_lower] = 1
        else:
            characters[c_lower] += 1
        
    
    return characters