import random

def get_random_color():
    """
    Returns a randomly chosen color.

    Returns:
        str: A randomly chosen color.
    """
    colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
    random_color = random.choice(colors)
    
    return random_color


def get_random_alphabet():
    """
    Returns the hexadecimal value of a randomly chosen alphabet.

    Returns:
        str: The hexadecimal value of a randomly chosen alphabet.
    """
    # Select a random alphabet from the string of alphabets
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    random_alphabet = random.choice(alphabets)
    
    # Convert the randomly chosen alphabet to hexadecimal
    hex_value = hex(ord(random_alphabet))
    
    return hex_value

def main():
    print("Hello World!")

    for i in range(10):
        print(i)

        def fibonacci_sum(start, end):
            """
            Calculates the sum of Fibonacci numbers within a given range.

            Args:
                start (int): The starting number of the range.
                end (int): The ending number of the range.

            Returns:
                int: The sum of Fibonacci numbers within the given range.
            """
            # Calculate the sum of Fibonacci numbers within the given range
            fib_sum = 0
            fib_prev = 0
            fib_curr = 1

            while fib_curr <= end:
                if fib_curr >= start:
                    fib_sum += fib_curr
                fib_prev, fib_curr = fib_curr, fib_prev + fib_curr

            return fib_sum
        
    


if __name__ == '__main__':
    main()