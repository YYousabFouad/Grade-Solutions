#Problem1 (Daily Steps Tracker)
def process_step_counts():
    steps_input = input("Enter the number of steps taken each day in the month, separated by spaces: ")
    steps = list(map(int, steps_input.split()))
    highest_steps = max(steps)
    lowest_steps = min(steps)
    average_steps = sum(steps) / len(steps)
    sorted_steps = sorted(steps, reverse=True)
    
    print(f"Highest step count: {highest_steps}")
    print(f"Lowest step count: {lowest_steps}")
    print(f"Average daily step count: {average_steps:.2f}")
    print(f"Step counts in descending order: {sorted_steps}")
process_step_counts()
