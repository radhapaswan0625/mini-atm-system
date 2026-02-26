print("====Mini ATM System====")

balance = 1000 #starting balance 

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4)😊")

    if choice == "1":
        print("your current balance is :", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit:"))
        balance += amount
        print("Deposit successfull!")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw:"))
        if amount <= balance: 
            balance -= amount 
            print("Withdrawl sucessful !")
        else:
            print("Insufficient balance 😁")  

    elif choice == "4":
        print("Thank You for using ATM. Goodbye 👋")
        break

    else:
        print("Invalid choice. Please try again !!")

                  
 
