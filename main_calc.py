from termcolor import colored
from matplotlib import pyplot as plt

print(colored("Calculator made by Kiet P.", "red"))
print("The output of the calculator will indicate how many cycles\nit takes for the input value to reach back to 1")
print("If the value is even, it will be divided in half, if odd then 3n+1")

def main():
    input_num = int(input("Enter a number to run: "))
    value = input_num
    cycle_count = 0
    cycle_list = []
    value_list = []
    while value != 1:
        cycle_list.append(cycle_count)
        value_list.append(value)
        if (value % 2) == 0: #if num is even
            value = round(value / 2)
        else: #if value is odd
            value = round((value * 3) + 1)
        cycle_count += 1
    cycle_list.append(cycle_count + round(cycle_count / 10))
    value_list.append(value)
    print(colored(f"The value {input_num} takes {cycle_count} cycles to come back to 1", "green"))
    plt.plot(cycle_list, value_list)
    plt.xlabel("Cycle num")
    plt.ylabel("Value")
    plt.show()

main()
