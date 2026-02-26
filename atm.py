print("====Mini ATM System====")

balance = 1000 #starting balance 

while True:
    print("\n----MENU----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4)😊")

    if choice == "1":
        print(f"\n💰 current balance : Rs. {balance:.2f }")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount > 0:
            balance += amount
            print("✅Deposit successfull!")
        else:
            print("❌ Invalid Amount")    

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: Rs. "))
        if amount > balance:
            print("❌ Insufficient balance!")
        elif amount <= 0:
            print("❌ Invalid amount ")
        else:
            balance -= amount 
            print("✅Withdrawl sucessful !")
          

    elif choice == "4":
        print("\nThank You for using ATM. Goodbye 👋")
        break

    else:
        print("❌ Invalid choice. Please try again !!")

                  
 
