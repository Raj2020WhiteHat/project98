def find_numbers(start, end, divisor):
    for i in range(start, end+1):
        if i % divisor == 0:
            print(i)

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
divisor = int(input("Enter the divisor: "))

find_numbers(start, end, divisor)
