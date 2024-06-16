"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_data(data)


def display_subject_data(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:>3} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)
        # print(parts)  # See if that worked
        # print("----------")
    input_file.close()
    return data


main()
