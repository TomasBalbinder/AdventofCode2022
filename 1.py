

with open('input.txt', 'r') as calories:
    reading = calories.read().strip()
    
    split_space_elfs = reading.split('\n\n')
     
    split_done = [calories_split.split() for calories_split in split_space_elfs]

    larger_number = 0
    for each_elf_calories_list in split_done:
   
        total = 0        
        for calorie in each_elf_calories_list:
            int_calorie = int(calorie) # from string to intiger, important !
            total = total + int_calorie 
             
        if total > larger_number:
            larger_number = total
    print(larger_number)




   
 
    