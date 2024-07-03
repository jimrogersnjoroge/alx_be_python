# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"'{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"'{task}' is a high priority task. Make sure to complete it soon!"
    case "medium":
        if time_bound == "yes":
            reminder = f"'{task}' is a medium priority task that needs to be done today!"
        else:
            reminder = f"'{task}' is a medium priority task. Try to complete it soon!"
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task, but it needs to be done today!"
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered. Please enter high, medium, or low."

# Provide a Customized Reminder
print(f"Reminder: {reminder}")
