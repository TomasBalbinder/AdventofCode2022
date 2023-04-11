
# first - opponent  
# A - rock
# B - paper
# C - sccisors

# second - me 
# X - rock
# Y - paper
# Z - sccisors

# The winner of the whole tournament is the player with the highest score.
# The score for a single round is the score for the shape you selected
#  1 rock
#  2 paper 
#  3 sccisors

# plus the score for the outcome of the round
# 0 if you lost
# 3 if the round was tied
# 6 if you won





def loading_input():
    with open('input_2.txt', 'r') as strategy_guide:
        reading = strategy_guide.read().strip()
        return reading
    
cheat_sheet = loading_input()

replacements = {
        'A': '1',
        'B': '2',
        'C': '3',
        'X': '1',
        'Y': '2',
        'Z': '3',
        }

for old, new in replacements.items():
    cheat_sheet = cheat_sheet.replace(old, new)

saving_data = cheat_sheet


numbers_list = [int(number) for number in saving_data.split()]

new_list = []
for i in range(0,len(numbers_list),2):
    new_listik = [numbers_list[i], numbers_list[i+1]]
    new_list.append(new_listik)


score = 0        
for i in new_list:
    if i[0] > i[1]:
        score = score + i[1]

    elif i[0] < i[1]:
        score = score + (i[1] + 6)

    elif i[0] == i[1]:
        score = score + (i[1] + 3)

print(score)
