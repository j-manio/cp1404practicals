"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def display_subject_details(data):
    """Displays subject details."""
    for class_info in data:
        print(f"{class_info[0]} is taught by {class_info[1]:12} and has {class_info[2]:>3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        # print(subject_data)  # See if that worked
        # print("----------")
    input_file.close()
    return data


main()
