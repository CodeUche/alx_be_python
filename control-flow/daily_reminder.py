# daily_reminder.py

def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Print message directly based on priority
    match priority:
        case "high":
            print(f"Reminder: '{task}' is a high priority task", end=" ")
        case "medium":
            print(f"Reminder: '{task}' is a medium priority task", end=" ")
        case "low":
            print(f"Note: '{task}' is a low priority task", end=" ")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")
            return

    # Modify message based on time-bound input
    if time_bound == "yes":
        print("ALX assignments requires immediate attention today!")
    else:
        if priority == "low":
            print("Consider completing the ethical hacking tasks when you have free time.")
        else:
            print("No immediate action needed here.")

if __name__ == "__main__":
    main()

