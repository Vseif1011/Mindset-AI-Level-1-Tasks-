#1 
words = ['apple','banana','grape','kiwi']
last_char = sorted(words,key = lambda x:x[-1])
print(last_char)

#2 
from math import pi 

radius = float(input("Enter the radius of the circle: "))
circum  = 2 * pi * radius 
area = pi * radius**2
print(f"Circumference: {circum:.2f} - Area: {area:.2f}")

#3 
import random 

attempts = 0 
num = random.randint(1,50)
while True :
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == num:
        print(f"Correct!, It took you {attempts} attempts to guess the number")
        break 
    elif guess>num:
        print("Wrong, try a lower number")
    else:
        print("Wrong, try a higher number")

#4 
import random
from datetime import datetime, timedelta 

current_year = datetime.now().year
start_date=datetime(current_year,1,1)
end_date=datetime(current_year,12,31)

D = []
for _ in range(10):
    random_day=random.randint(0,(end_date-start_date).days)
    random_date=start_date+timedelta(days=random_day)
    D.append(random_date.day)
D=set(D)
print(D)