def get_study_data():
    """Ask user to enter subjects and study time."""

    study_data = {}

    try:
        num_subjects = int(input("How many subjects did you study? "))

    except ValueError:
        print("Invalid number.")
        return study_data

    for i in range(num_subjects):

        subject = input(f"\nEnter name of subject {i + 1}: ")

        try:
            hours = int(input("Enter hours studied: "))
            minutes = int(input("Enter minutes studied: "))

            # Convert hours and minutes into total minutes
            total_minutes = (hours * 60) + minutes

        except ValueError:
            print("Invalid input. Setting time to 0.")
            total_minutes = 0

        if subject in study_data:
            study_data[subject] += total_minutes

        else:
            study_data[subject] = total_minutes

    return study_data


def convert_time(minutes, choice):
    """Convert time according to user choice."""

    choice = choice.lower()

    hours = minutes // 60
    remaining_minutes = minutes % 60

    # Hours only
    if choice == "h" or choice == "hours":
        if hours > 0:
            return f"{hours} hours"
        else:
            return "0 hours"

    # Minutes only
    elif choice == "m" or choice == "minutes":
        return f"{minutes} minutes"

    # Both hours and minutes
    elif choice == "b" or choice == "both":

        if hours > 0 and remaining_minutes > 0:
            return f"{hours} hours {remaining_minutes} minutes"

        elif hours > 0:
            return f"{hours} hours"

        elif remaining_minutes > 0:
            return f"{remaining_minutes} minutes"

        else:
            return "0 minutes"

    else:
        return f"{minutes} minutes"


def total_study_time(study_data):
    return sum(study_data.values())


def average_study_time(study_data):

    if len(study_data) == 0:
        return 0

    return total_study_time(study_data) // len(study_data)


def most_studied_subject(study_data):

    if not study_data:
        return None

    return max(study_data, key=study_data.get)


def least_studied_subject(study_data):

    if not study_data:
        return None

    return min(study_data, key=study_data.get)


def print_report(study_data):

    print("\n" + "=" * 45)
    print("       STUDY TIME ANALYSIS REPORT")
    print("=" * 45)

    if not study_data:
        print("No study data entered.")
        return

    choice = input(
        "\nDisplay time in Hours(H), Minutes(M) or Both(B): "
    )

    for subject, minutes in study_data.items():

        print(f"{subject:<20}: {convert_time(minutes, choice)}")

    print("-" * 45)

    print("Total study time     :",
          convert_time(total_study_time(study_data), choice))

    print("Average time/subject:",
          convert_time(average_study_time(study_data), choice))

    print("Most studied subject :",
          most_studied_subject(study_data))

    print("Least studied subject:",
          least_studied_subject(study_data))

    print("=" * 45)

def main():

    print("Welcome to Student Study Time Analyzer\n")

    data = get_study_data()

    print_report(data)


main()
