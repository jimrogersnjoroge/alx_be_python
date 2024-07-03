# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

reminder = f"Reminder: '{task}' "

# Task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(reminder + "is a high priority task that requires immediate attention today!")
        else:
            print(reminder + "is a high priority task. Make sure to complete it soon!")
    case "medium":
        if time_bound == "yes":
            print(reminder + "is a medium priority task that needs to be done today!")
        else:
            print(reminder + "is a medium priority task. Try to complete it soon!")
    case "low":
        if time_bound == "yes":
            print(reminder + "is a low priority task, but it needs to be done today!")
        else:
            print(reminder + "is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please enter high, medium, or low.")

# Provide a customized reminder
print()
