# Determining the award a person competing in a triathlon will receive

# asking the user to input time of various sporting activites 
swimming = float(input("record time for compeating in swiming: "))
running = float(input("record time for compeating in running: "))
cycling = float(input("record time for compaeting in cycling: "))
print(swimming)
print(running)
print(cycling)

# Added up all the times enterd and rounded off by 2 
Total_time = swimming + running + cycling 
print(round(Total_time,2))

Qualify_time = 100 

# used if,else,elif to determine the awards given to contestants 
if Total_time <= Qualify_time : 
    print( "Provincial Award")
elif Total_time <= Qualify_time + 5:
    print("Provincial half colours Award")
elif Total_time <= Qualify_time + 10:
    print("Provincial Scroll")
else:
    Total_time > Qualify_time + 10
    print("No award ")
    
    

