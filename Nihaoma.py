import random
from datetime import datetime, timedelta

def random_date(start_year=1990, end_year=2025):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)

print(random_date())
start_year = int(input("Enter the start year (e.g., 1990): "))
end_year = int(input("Enter the end year (e.g., 2025): "))
print(random_date(start_year, end_year))
while True:
    user_input = input("Enter a number to generate a random date or 'q' to quit: ")
    if user_input.lower() == 'q':
        break
    try:
        number = int(user_input)
        print(random_date(start_year, end_year))
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")