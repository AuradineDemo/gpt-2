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