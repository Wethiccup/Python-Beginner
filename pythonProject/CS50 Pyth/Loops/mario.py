def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)
    
#     print_row(4)

def print_row(width):
    print("#" * width)
    
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")
        
main()