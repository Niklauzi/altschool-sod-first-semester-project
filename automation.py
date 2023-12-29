#AUTOMATION PROGRAM

'''
A local retail business, dealing with a variety of products, aims to streamline and automate its accounting procedures. The business operates two shifts per day with one worker on each shift. The primary goal is to create a Python project that assists in automating essential accounting tasks, including calculating total sales, worker salaries, profit, tips, and total tips for the day.

1. Calculate Total Sales for the Day: from sales data for morning and evening shifts, produce total sales for the day.

2. Calculate Worker's Salary: given hourly rate and hours worked by a worker. retrieve the worker's salary.

3. Calculate Profit: given a list of numbers representing total sales and total cost of items sold, find the profit.(or loss if negative)

4. Calculate Tips for a Shift: from sales data for a specific shift, workers get tipped for the shift (2% of shift sales).

5. Calculate Total Tips for the Day: with sales data for morning and evening shifts, return total tips for the day (sum of tips from both shifts).

'''

# Get_input function

'''
This function takes a string `input_value` as a parameter, prompts the user for input using the value, and attempts to convert the entered values (comma-separated) into a list of floats. (N/B: I felt it would be easier to just get all the sales in each shifts as a list, so it can be further analyze easily.)
It uses a try and except block to catch `ValueError` if the conversion fails, it prints an error message and prompts the user to enter valid numbers.
It then returns the list of float values.

'''

def get_input(input_value):
    while True:
        try:
            sales_input = input(input_value)
            return [float(x) for x in sales_input.split(',')]
        except ValueError:
            print('Invalid input. Please enter valid numbers separated by commas.')
            
# total_daily_sales function

'''
This function Prints a message prompting the user to enter sales for morning and evening shifts.
Calls `get_input()` twice to get the sales for each shift.
Calculates the total sales for the day and prints the result.
Print the sum of the total sales list and Returns the combined list of sales.

'''

def total_daily_sales():
    print("Enter sales for morning and evening shifts:")
    
    sales_shift_1 = get_input("Morning shift sales: ")
    sales_shift_2 = get_input("Evening shift sales: ")
    
    total_sales = sales_shift_1 + sales_shift_2
    print(f'Total sale is ${sum(total_sales)}')
    return total_sales

# salary function

'''
Defines fixed hourly rates and hours worked.
Calculates and prints the salary for an 8-hour shift.
NB: I didn't think i need to make the hourly rate and the hours worked Global because i would only be calling the function once, and also because i felt they should be fixed, it can be further modified to capture more flexible input when necessary

'''
def salary():
    hourly_rates = 5
    hours_worked = 8
    salary_value = hourly_rates * hours_worked
    print(f' Salary for 8 hour shift is ${salary_value:.2f}')
    
# profit function

'''
This function takes the total sales as a parameter and calculates the profit or loss by subtracting total costs from total sales.
Prints the result, indicating whether it's a profit, loss, or break-even.

'''
def profit(total_sales):
    total_costs = [50, 25, 80, 65, 20, 45]    
    difference = sum(total_sales) - sum(total_costs)
    
    if difference > 0:
        print(f'Your profit is ${difference:.2f}')
    elif difference == 0:
        print('You did not make profit or loss')
    else:
        print(f'Your loss is ${difference:.2f}')

# tip function

'''
Takes the sales for morning and evening shifts as parameters.
Prompts the user to enter a choice for the morning or evening shift.
Calculates and prints the tip for the selected shift based on 2% of the total sales for that shift.

'''
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
    
# total tips function

'''
Takes the total sales as a parameter and calculates the total tips for the day, which is 2% of the total sales. you can also get same figure by adding each individual tip
Prints the result.

'''

def total_tips(total_sales):
    total_tip = sum(total_sales) * 0.02
    print(f'total tip is ${total_tip:.2f}')






#Automation Program
'''  
Automation Program serves as the main control function for the program, running an interactive menu system.
The user can choose to calculate total sales, salary, profit or loss, tip for a shift, total tips, or exit the program.
Certain calculations are dependent on others (e.g., profit depends on total sales).
The program continues running until the user chooses to exit.

'''

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
            print('Exiting program!!!.')
            break
        
        else:
            print('Invalid choice. Please enter a number between 1 and 6.')


# Challenges
'''
1. Collecting the sales input in each shift as a list
2. Trying to not repeat myself
3. Accessing the sale_shift variable without assigning it outside of the total_daily_sales function or using the GLobal keyword inside the function was a bit stressful, as i ran into scoping issues. but i fixed it by returning the values and passing it into the required functions for further computation (e.g, profit function requires the list of the total_sales, same technique was implemented in the tip_per_shift function).
4. I had UnboundLocalError when trying call the tip_per_shift from the automation program without getting the total_sales first, normaling it would promt the user to 'Please calculate total sales (option 1) before calculating total tips.', i fixed this by initializing total_sales, sales_shift_1, and sales_shift_2.
'''