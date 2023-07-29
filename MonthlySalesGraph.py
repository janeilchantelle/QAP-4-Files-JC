
# PYTHON PROGRAMMING QAP 4 - Program 2

# Written By: Janeil Carroll
# Date Written: July 26-28, 2023

# PROGRAM DESCRIPTION:
# A program used to that will allow the user to enter the total
# amount of sales for each month from January to December.

# Import Libraries

# Import required libraries

import matplotlib.pyplot as plt

# Function to convert sales value to formatted string with dollar sign and decimal
def format_sales(value): return "${:,.2f}".format(value)


# Inputs:

Jan = float(input("Enter the total sales for January: "))
Feb = float(input("Enter the total sales for February: "))
Mar = float(input("Enter the total sales for March: "))
Apr = float(input("Enter the total sales for April: "))
May = float(input("Enter the total sales for May: "))
Jun = float(input("Enter the total sales for June: "))
Jul = float(input("Enter the total sales for July: "))
Aug = float(input("Enter the total sales for August: "))
Sep = float(input("Enter the total sales for September: "))
Oct = float(input("Enter the total sales for October: "))
Nov = float(input("Enter the total sales for November: "))
Dec = float(input("Enter the total sales for December: "))

sales = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

formatted_sales = [format_sales(value) for value in sales]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

bar_color = "Pink"

plt.bar(months, sales, color=bar_color)

plt.xlabel('Month')
plt.ylabel('Sales Amount in CAD')
plt.title('Monthly Sales')
plt.show()
