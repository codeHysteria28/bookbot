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

def sort_on(characters):
    return characters["count"]

def report(characters):
    sorted_report = []
    
    for char, count in characters.items():
        char_dict = {"char": char, "count": count}
        sorted_report.append(char_dict)

    sorted_report.sort(reverse=True, key=sort_on)

    for i in sorted_report:
        if(i["char"].isalpha()):
            print(f"{i["char"]}: {i["count"]}")
    

