TotalGrocery = []
i = 1
j = 1
while True:
    try:
        MyGrocery = input("").upper()
        if f"{j} {MyGrocery}" in TotalGrocery:
            j += 1
            TotalGrocery.remove(f"{j-1} {MyGrocery}")
            TotalGrocery.append(f"{j} {MyGrocery}")
            TotalGrocery.sort()
        else:  
            j = 1          
            TotalGrocery.append(f"{i} {MyGrocery}")
            TotalGrocery.sort()     
    except EOFError:
            for Grocery in TotalGrocery:
                 print(Grocery)            
            break    
    # 