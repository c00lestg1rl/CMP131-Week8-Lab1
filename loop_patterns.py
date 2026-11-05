# Samantha Vasquez 
# CMP 131: Week 8, Lab 1
# Program 1: Sales Bar Chart
# November 5, 2026

# Part 1: Display a Program Title
print(f'~~~ Sales Bar Chart ~~~')

# Part 2: Enter the store sales
ast= ""
store= int(input("Enter the amount of stores: "))

# Part 3: Covert and validate input 
for i in range(store): 
    sale= float(input( "Enter today's sales for store " + str(i + 1) + ":"))
    # xxx missing line
    sale= sale/100

# Part 4: Determine the number of astericks
    for j in range(sale):
        ast = ast + "*"
ast= ast + "/n"
print( )    


