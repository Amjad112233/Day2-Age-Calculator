name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))


current_year = 2026

age = current_year - birth_year

print("Hello", name)
print("You are", age , "years old.")

if age<18:
    print("You are under 18.")
else:
    print("You are an adult")