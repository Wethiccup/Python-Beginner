def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")
        
main()


# ? while True: # * deliberate infinite loop
# ?     n = int(input("What's n? "))
# ?     if n > 0:
# ?         break
    
# ? for _ in range(n):
# ?     print("meow")
    
# ? print("meow\n" * 3, end="")

# ? for _ in range(3): # * Replaced [0, 1, 2] with range(3) pythonic to make the variable _
# ?    print("meow")

# ? i = 0
# ? while i < 3:
# ?   print("meow")
# ?   i += 1

