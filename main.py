import math

#math

# Step 1: Get user input
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 2: Apply the Euclidean distance formula
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Step 3: Display the result with 2 decimal places
print(f"The distance between the two points is: {distance:.2f}")
# End the program



#Password_checker
def password_checker():
    while True:
        password = input("Enter your password: ")
        
        if len(password) < 8:
            print("passwordsword is too short, must be atleast 8 characters long. Try again")
        elif len(password) > 15:
            print("password is too long. Must not exceed 15 characters. Try again")
        else:
            print("Password accepted.")
            break
password_checker()


#Loan
credit_score = int(input("Enter credit score: "))
income = float(input("Enter annual income: "))
years_job = int(input("Enter years at current job: "))

if credit_score >= 700:
    if income >= 30000:
        if years_job >= 2:
            print("Result: Loan Approved")
        else:
            print("Result: Loan Denied")
    else:
        print("Result: Loan Denied")
else:
    print("Result: Loan Denied")
