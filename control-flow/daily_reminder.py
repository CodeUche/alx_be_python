# daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            message = f"Reminder: '{task}' is a high priority task"
        case "medium":
            message = f"Reminder: '{task}' is a medium priority task"
        case "low":
            message = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        if priority == "low":
            message += ". Consider completing it when you have free time."
        else:
            message += "."

    print("\n" + message)

if __name__ == "__main__":
    main()

