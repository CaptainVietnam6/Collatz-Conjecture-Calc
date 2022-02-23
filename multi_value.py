from asyncio import run
from termcolor import colored
from matplotlib import pyplot as plt

print(colored("Calculator made by Kiet P.", "red"))
print("The output of the calculator will indicate the number\nof cycles needed for a value to return to 1 for\na range of numbers")
print("If the value is even, it will be divided in half, if odd then 3n+1")

def main():
    run_cycles = int(input("Enter the upper range of value the calculator will run to: "))

    run_value = 1
    cycles_list = []
    run_list = []
    for i in range(run_cycles):
        value = run_value
        cycle_num = 0
        while value != 1:
            if (value % 2) == 0: #if num is even
                value = round(value / 2)
            else: #if value is odd
                value = round((value * 3) + 1)
            cycle_num += 1
        cycles_list.append(cycle_num)
        run_value += 1
        run_list.append(run_value)
    plt.plot(run_list, cycles_list)
    plt.xlabel("n value")
    plt.ylabel("Cycles to 1")
    plt.show()

main()
