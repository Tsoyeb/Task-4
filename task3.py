# A program to determine the award a participant will recieve in a Triathlon 

# name of participant 
name = input('Please enter your name: ')

# Finish time for each triathalon event 
triathlon_event_s= int(input('Please enter your finish time in minutes for Swimming: '))
triathlon_event_c= int(input('Please enter your finish time in minutes for Cycling: '))
triathlon_event_r= int(input('Please enter your finish time in minutes for Running: '))

qualifying_time = 100
half_colours = 5
provincial_scroll = 10 

# total time of all events 
finish_time = triathlon_event_s + triathlon_event_c + triathlon_event_r 

# if finishing time is less then 10 mins of qualifying time of 100mins. The award will be provincal scroll.    
if finish_time <= qualifying_time:
    print(f'Congratulations, {name.capitalize().strip()}! you finished the triathlon in {finish_time} minutes you have been awarded Provincial Scroll!')

# if finishing time is less then 5 mins of qualifying time of 100mins. The award will be provincal half colours.  
elif finish_time <= qualifying_time + half_colours:
    print(f'Congratulations, {name.capitalize().strip()}! you finished the triathlon in {finish_time} minutes you have been awarded Provincial Half Colours!')  

# if finishing time is less then 100 mins of qualifying time. The award will be provincal Colours.  
elif finish_time <= qualifying_time + provincial_scroll:
    print(f'Congratulations, {name.capitalize().strip()}! you finished the triathlon in {finish_time} minutes you have been awarded Provincial Colours!')   

# if finishing time is more then 110 mins of qualifying time. There will be no award. 
else: 
    print(f'Unfortunately, you have not been awarded this time as you finished in {finish_time} minutes Better luck next time!')



    

