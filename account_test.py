import bankaccount

def main():
    #Get the starting balance.
    startBal = float(input('Enter your starting balance: '))

    # Create a BankAccount object.
    savings = bankaccount.BankAccount(startBal)

    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    savings.deposit(pay)

    # Display the balance.
    print('Your account balance is $', \
    format(savings.getBalance(), ',.2f'),sep='')
main()
