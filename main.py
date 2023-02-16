import datetime

print("Age calculator!")

birth_year = int(input("Enter your birth year: "))
today = datetime.date.today()
current_year = today.year

age = current_year - birth_year

print("Your current age is ", age, " in ", current_year)

