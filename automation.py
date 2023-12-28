def total_daily_sales():
    
    while True:
        
        try:
            sales_shift_1 = input("Enter morning shift sales seperated by commas: ")
            sales_shift_2 = input("Enter evening shift sales separated by commas: ")
            
            sales_shift_1 = [float(x) for x in sales_shift_1.split(',')]
            sales_shift_2 = [float(x) for x in sales_shift_2.split(',')]
            
            break
        except ValueError:
            print('Please enter a valid number')
    
    total_sales = sales_shift_1 + sales_shift_2
    print(f'Total sale is ${sum(total_sales):.2f}')
    return total_sales

def salary():
    hourly_rates = 5
    hours_worked = 8
    salary_value = hourly_rates * hours_worked
    print(f' Salary for 8 hour shift is ${salary_value:.2f}')
    
    
def profit(total_sales):
    total_costs = [50, 25, 80, 65, 20, 45]    
    difference = sum(total_sales) - sum(total_costs)
    
    if difference > 0:
        print(f'Your profit is ${difference:.2f}')
    elif difference == 0:
        print('You did not make profit or loss')
    else:
        print(f'Your loss is ${difference:.2f}')

        
def tip_per_shift(sales_shift_1, sales_shift_2):
    shift_choice = input("Enter '1' for morning shift or '2' for evening shift: ")
    if shift_choice == '1':
        tip = sum(sales_shift_1) * 0.02
        print(f'Tip for morning shift: ${tip:.2f}')
    elif shift_choice == '2':
        tip = sum(sales_shift_2) * 0.02
        print(f'Tip for evening shift: ${tip:.2f}')
    else:
        print('Invalid choice. Please enter either "1" or "2".')
    
    
def total_tips(total_sales):
    total_tip = sum(total_sales) * 0.02
    print(f'total tip is {total_tip:.2f}')

    
### Automation Program
    
def automation():
    total_sales = []
    sales_shift_1 = []
    sales_shift_2 = []
    
    while True:  
        print("\nAutomation")
        print("1. Calculate total sales")
        print("2. Calculate Salary")
        print("3. Calculate Profit or Loss")
        print("4. Calculate Tip for a shift")
        print("5. Calculate total Tips for a the day")
        print("6. Exit Program")
        
        

        choice = input("Enter your choice from (1-6): ")
        if choice == '1':
            total_sales = total_daily_sales()
            sales_shift_1 = total_sales[:len(total_sales)//2]
            sales_shift_2 = total_sales[len(total_sales)//2:]
        elif choice == '2':
            salary()
        elif choice == '3':
            if not total_sales:
                print("Please calculate total sales (option 1) before calculating profit.")
            else:
                profit(total_sales)
        elif choice == '4':
            if not sales_shift_1 or not sales_shift_2:
                print("Please calculate total sales (option 1) before calculating tip for a shift.")
            else:
                tip_per_shift(sales_shift_1, sales_shift_2)
        elif choice == '5':
            if not total_sales:
                print("Please calculate total sales (option 1) before calculating total tips.")
            else:
                total_tips(total_sales)
        elif choice == '6':
            print('Exiting program.')
            break
        
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')