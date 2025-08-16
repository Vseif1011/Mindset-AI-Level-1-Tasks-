#1 
def is_prime():
    n = int(input("Enter a number to check if it is a prime number: "))

    if n < 2:
        print("Not Prime")
        return

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")

is_prime()

#--------------------------------------------
#2 
call_count = 0
max_calls = 100
fib_list = []
def fibonacci(n):
    global call_count
    call_count +=1
    if call_count == max_calls:
        raise RecursionError("Recursion limit reached")
        return
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def store_fibonacci():
    x=int(input("Enter a number: "))
    global fib_list
    fib_list = [fibonacci(i) for i in range(x)]
    print(fib_list)

store_fibonacci()

#--------------------------------------------
#3 
def filter_long_words(words,min_length):
    big_words = []
    for word in words:
        if len(word)>min_length:
            big_words.append(word)
    return big_words
Words = ['Company','Bank','Hospital','School']
Min_Length = 4
lst = filter_long_words(Words,Min_Length)
print(lst)


#--------------------------------------------
#4 

def Multiplication_table(x,y):
    for i in range(1,x+1):
        for j in range(1,y+1):
            if i*j %2 ==0:
                print(f"{i*j}\t",end="")
            else:
                print(f"-\t",end="")
        print()
        
Multiplication_table(5,5)