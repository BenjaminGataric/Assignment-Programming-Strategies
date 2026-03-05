from typing import Final
#Constants (TASK 1 - put constants in a dictionary or tuple - WHO?)
COFFEE: Final = "Coffee"
TEA: Final = "Tea"
HOT_COCO: Final = "Hot Chocolate" #Lelandi
COFFEE_PRICE: Final = 3.00
TEA_PRICE: Final = 2.50
HOT_COCO_PRICE: Final = 3.75
SUGAR: Final = "Sugar"
CREAM: Final = "Cream"
SYRUP: Final = "Syrup"
SUGAR_PRICE: Final = .10
CREAM_PRICE: Final = .50
SYRUP_PRICE: Final = .75
DISCOUNT_THRESHOLD: Final = 5.00
DISCOUNT: Final = .10
TAX: Final = .05
#Welcome Message
border = f"="*37
order_count = 1
print(border)
print(f"\tWELCOME TO Python CAFE")
print(border)
print(f"\nOrder #{order_count}")
print(f"-" * 8)
print(border)
print(f"\tBeverage Menu:")
print(border)
print(f"1. {COFFEE}\t\t${COFFEE_PRICE:.2f}"
      f"\n2. {TEA}\t\t\t${TEA_PRICE:.2f}"
      f"\n3. {HOT_COCO}\t${HOT_COCO_PRICE:.2f}")
print(border)
#Beverage selction
user_selection = int(input("Your selection (1-3): "))
drink_order = {}
while user_selection == 1 or 2 or 3:
    if user_selection == 1:
        print("\nYou chose Coffee:")
        drink_order[COFFEE] = COFFEE_PRICE
        break
    elif user_selection == 2:
        print("\nYou chose Tea.")
        drink_order[TEA] = TEA_PRICE
        break
    elif user_selection == 3:
        print("\nYou chose Hot Chocolate.") #Lelandi
        drink_order[HOT_COCO] = HOT_COCO_PRICE
        break
    else:
        print("Please enter a number between 1 and 3.")
        user_selection = int(input("Your selection (1-3): "))
#Extra Selection

#checkmark when choosing extras - WHO?

print(f"\n{border}")
print(f'{"Add Extras":>23}')
print(border)
print(f"1. {SUGAR}\t{SUGAR_PRICE:.2f}"
      f"\n2. {CREAM}\t{CREAM_PRICE:.2f}"
      f"\n3. {SYRUP}\t{SYRUP_PRICE:.2f}"
      f"\n0. Finish order")
print(border)
#Extras Order
extra_order = {}
extra_selection = int(input("Select extra (0-3): "))
while extra_selection == 1 or 2 or 3 or 0:
    if extra_selection == 1:
        print(f"{SUGAR} added ({SUGAR_PRICE})")
        extra_order[SUGAR] = SUGAR_PRICE
        extra_selection = int(input("Select extra (0-3): "))
        if extra_selection == 1:
            print("Sugar is already added.")
    elif extra_selection == 2:
        print(f"{CREAM} added ({CREAM_PRICE})")
        extra_order[CREAM] = CREAM_PRICE
        extra_selection = int(input("Select extra (0-3): "))
    elif extra_selection == 3:
        print(f"{SYRUP} added ({SYRUP_PRICE})")
        extra_order[SYRUP] = SYRUP_PRICE
        extra_selection = int(input("Select extra (0-3): "))
    elif extra_selection == 0:
        break
    else:
        print("Please enter a number between 0 and 3.")
        extra_selection = int(input("Select extra (0-3): "))
#Calculations
subtotal = 0
for v in drink_order.values():
    subtotal += v
for v in extra_order.values():
    subtotal += v
if subtotal > DISCOUNT_THRESHOLD:
    discount_order = subtotal * DISCOUNT
else:
    discount_order = 0
discount_before_subtotal = subtotal - discount_order
total_tax = discount_before_subtotal * TAX
Grand_total = total_tax + discount_before_subtotal
#Order Summary
print(border)
print(f"\tORDER SUMMARY")
print(border)
for key, val in drink_order.items():
    print(f"Beverage: {key}\t${val:.2f}")
if extra_order != {}:
    print(f"Extras:")
    for key, val in extra_order.items():
        print(f"   • {key}\t\t${val:.2f}")
print(f"Subtotal: \t\t${subtotal:.2f}")
if discount_order > 0:
    print(f"Discount (10%)\t\t-${discount_order:.2f}"
        f"\nAfter Discount:\t\t${discount_before_subtotal:.2f}")
print(border)
another_order = input("Would you like to order another drink? (Y/N): ")
#Reciept Summary
if another_order.lower() == "n" or " ":
    print(border)
    print(f"\tRECEIPT SUMMARY") #Lelandi
    print(border)
    print(f"\nNumber of Drinks:\t{order_count}"
          f"\nSubtotal:\t\t{(discount_before_subtotal):.2f}"
          f"\nTax (5%):\t\t{total_tax:.2f}"
          f"\nGrand Total:\t\t{Grand_total:.2f}")
    print(border)
    print (f"\nThank you for visiting Python Cafe!"
           f"\nWe hope to see you again soon!")
#Part 2 - WHO?


'''Part 2: Multiple Orders and Final Receipt
Update your Part 1 program to include the following functionality:

1. Handling Multiple Orders:
o Allow the user to place multiple beverage orders
• After each order, ask: “Would you like to order another drink? (Y/N)” and allow
placing a new order if the user wants.
o Keep running totals for all orders
o Track number of drinks ordered

2. Displaying Final Receipt:
o Display final receipt when user finishes ordering
o Show total number of drinks
o Show subtotal, tax, and grand total
o Display thank you message

3. Validating the User’s Input:
o Validate all user inputs (beverage choice 1-3, extra choice 0-3)
• If the user input falls outside of the allowed values, display an appropriate
message, and have them try again.
o Handle empty input when asking for another order. Empty input will be considered as
the case of entering ‘n/N’
o Display appropriate error messages
o It is NOT necessary to verify that input values match the expected data type. In other
words, you can assume that the user will enter digits for an integer item such as
beverage and extra selection.

4. Constants:
o The program MUST use constants for:
▪ Beverage names and prices
▪ Extra names and prices
▪ Discount threshold ($5.00) and rate (10%)
▪ Tax rate (5%)

5. Formatting:
o Use formatted output with proper alignment
o Display prices with 2 decimal places
o Use separators and banners for visual organization
o Overall, the program's output must be formatted to exactly match the format, layout,
and content displayed in the sample test runs provided in the Test Plan section.

6. Using Compound Data:
o The program must use compound data types to streamline your solution
'''
