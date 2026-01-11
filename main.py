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
