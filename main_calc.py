from termcolor import colored

print(colored("Calculator made by Kiet P.", "red"))
print("The output of the calculator will indicate how many cycles\nit takes for the input value to reach back to 1")
print("If the value is even, it will be divided in half, if odd then 3n+1")
input_num = int(input("Enter a number to run: "))

value = input_num
count = 0
while value != 1:
    if (value % 2) == 0: #if num is even
        value /= 2
    else: #if value is odd
        value = (value * 3) + 1
    count += 1
print(colored(f"The value {input_num} takes {count} cycles to come back to 1", "green"))
