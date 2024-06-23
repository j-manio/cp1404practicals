"""
Wimbledon
Estimate: 30 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():

    champion_to_count = {}
    records = load_data()
    for record in records:




def load_data():
    """Load data file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Remove header
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()