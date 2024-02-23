def main():
    print("Hello World!")

    for i in range(10):
        print(i)

        def fibonacci_sum(start, end):
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