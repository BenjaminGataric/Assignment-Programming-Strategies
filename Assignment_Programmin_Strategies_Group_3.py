'''
Program Name: Cafe Ordering System
Description: Collect user inputs for multiple beverage orders and display single order and complete order calculations 
Authors: Ben Gataric, Vincent Ruiyang Li, Lelandi Calil De Asis, Devon Huynh
Date: March 6th, 2026

'''




from typing import Final
#Constants
COFFEE: Final = "Coffee"
TEA: Final = "Tea"
HOT_COCO: Final = "Hot Chocolate"
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
border = f"="*37
order_count = 0
#Complete Customer Order
final_customer_order = {}
#Welcome Message
print(border)
print(f"\tWELCOME TO Python CAFE")
print(border)
while order_count >= 0:
    order_count += 1
    print(f"\nOrder #{order_count}")
    print(f"-" * 8)

#Beverage Menu
    print(f"\n{border}")
    print(f"\tBeverage Menu:")
    print(border)
    print(f"1. {COFFEE}\t\t${COFFEE_PRICE:.2f}"
          f"\n2. {TEA}\t\t\t${TEA_PRICE:.2f}"
          f"\n3. {HOT_COCO}\t${HOT_COCO_PRICE:.2f}")
    print(border)

#Beverage selction
    user_selection = input("Your selection (1-3): ")
    drink_order = {}
    while user_selection == "1" or "2" or "3":
        if user_selection == "1":
            print("\nYou chose Coffee:")
            drink_order[COFFEE] = COFFEE_PRICE
            break
        elif user_selection == "2":
            print("\nYou chose Tea.")
            drink_order[TEA] = TEA_PRICE
            break
        elif user_selection == "3":
            print("\nYou chose Hot Chocolate.")
            drink_order[HOT_COCO] = HOT_COCO_PRICE
            break
        else:
            print("Please enter a number between 1 and 3.")
            user_selection = input("Your selection (1-3): ")
    #Extra Selection
    extra_menu = {"1. Sugar": "$0.10", "2. Cream": "$0.50", "3. Syrup": "$0.75", "0. Finish Order":""}
    print(f"\n{border}")
    print(f'{"Add Extras":^37}')
    print(border)
    for key, val in extra_menu.items():
        print(f"{key}\t{val}")
    print(border)

    #Extras Order
    extra_order = {}
    extra_selection = input("Select extra (0-3): ")

    while extra_selection != "0":
        if extra_selection == "1":   
            if SUGAR in extra_order:
                print("Sugar is already added.")
            else:
                print(f"{SUGAR} added (+${SUGAR_PRICE:.2f}).")
                extra_menu["1. Sugar"] = "$0.10 ✓"
                extra_order[SUGAR] = SUGAR_PRICE
        elif extra_selection == "2":
            if CREAM in extra_order:
                print("Cream is already added.")
            else:
                print(f"{CREAM} added (+${CREAM_PRICE:.2f}).")
                extra_order[CREAM] = CREAM_PRICE
                extra_menu["2. Cream"] = "$0.50 ✓"
        elif extra_selection == "3":
            if SYRUP in extra_order:
                print("Syrup is already added.")
            else:
                print(f"{SYRUP} added (+${SYRUP_PRICE:.2f}).")
                extra_order[SYRUP] = SYRUP_PRICE
                extra_menu["3. Syrup"] = "$0.75 ✓"
        else:
            print("Please enter a number between 0 and 3.")
            extra_selection = input("Select extra (0-3): ")
            continue
        print(f"\n{border}")
        print(f'{"Add Extras":>23}')
        print(border)
        for key, val in extra_menu.items():
            print(f"{key}\t{val}")
        print(border)
        extra_selection = input("Select extra (0-3): ")
        

    #Oder Calculations
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
    final_customer_order[order_count] = discount_before_subtotal

    #Order Summary
    print(f"\n{border}")
    print(f"{"ORDER SUMMARY":^37}")
    print(border)
    for key, val in drink_order.items():
        print(f"Beverage: {key:<11}\t{f'${val:.2f}':>11}")
    if len(extra_order) > 0:
        print("Extras:")
        for key, val in extra_order.items():
            if extra_selection == "1" or "2" or "3":
                print(f"   • {key}\t\t{f'${val:.2f}':>11}")
    print(f"Subtotal: \t\t{f'${subtotal:.2f}':>11}")
    if discount_order > 0:
        print(f"{'Discount (10%)':<22} {f'-${discount_order:.2f}':>12}")
        print(f"After Discount:\t\t{f'${discount_before_subtotal:.2f}':>11}")
    print(border)
    another_order = input(f"\nWould you like to order another drink? (Y/N): ")
    #Recipt Calculations
    grand_total = 0
    for v in final_customer_order.values():
        grand_total += v
    grand_total_tax = grand_total * TAX
    grand_total_final = grand_total + grand_total_tax

    #Reciept Summary
    if another_order.lower() != "y":
        print(f"\n{border}")
        print(f'{f"RECEIPT SUMMARY":^37}') #Lelandi
        print(border)
        print(f"\nNumber of Drinks:\t{f'{order_count}':>7}"
              f"\nSubtotal:\t\t{f'${grand_total:.2f}':>11}"
              f"\nTax (5%):\t\t{f'${grand_total_tax:.2f}':>11}"
              f"\nGrand Total:\t\t{f'${grand_total_final:.2f}':>11}")
        print(border)
        print (f"\nThank you for visiting Python Cafe!"
           f"\nWe hope to see you again soon!")
        break