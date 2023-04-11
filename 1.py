
def part_1():
    with open('input_1.txt', 'r') as calories:
        reading = calories.read().strip()
        
        split_space_elfs = reading.split('\n\n')
        
        split_done = [calories_split.split() for calories_split in split_space_elfs]

        new_list = []
        larger_number = 0
        
        for each_elf_calories_list in split_done:
            
            total = 0        
            for calorie in each_elf_calories_list:
                int_calorie = int(calorie) # from string to intiger, important !
                total = total + int_calorie
            
            new_list.append(total)
          
                
            if total > larger_number:
                larger_number = total
        return new_list
    

def part_2(total_calories):
    new_list_1 = list(total_calories)

    final_list = []
    for b in range(3):
        
        larger_number1 = 0   
        for all_calorie in new_list_1:
            if all_calorie > larger_number1:
                larger_number1 = all_calorie

        final_list.append(larger_number1)
        new_list_1.remove(larger_number1)

    sum = 0
    for calorie in final_list:
        sum = sum + calorie

    return sum

print(part_2(part_1()))
    


 






   
 
    