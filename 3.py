
def loading_input():
    with open('input_3.txt', 'r') as bags:
        reading = bags.readlines()
        return reading
    
texts = loading_input()

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0

for text in texts:
    change_text = text.strip()
    
    size = (len(change_text))
    splitted = size // 2
    first_contain = change_text[:splitted]
    second_contain = change_text[splitted:]

    for letter in first_contain:
        if letter in second_contain:
            char_value = alphabet.index(letter) + 1
            total = total + char_value
            break
print(total)
