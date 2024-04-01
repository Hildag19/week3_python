def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = price - (price * discount_percent / 100)
        return discounted_price
    else:
        return price

# Prompting the user to enter the original price and discount percentage
original_price = float(input("100 "))
discount_percentage = float(input("20% "))

# Calculating the final price using the calculate_discount function
final_price = calculate_discount(100, 20)

# Displaying the final price
if final_price == original_price:
    print("No discount applied. Final price:", final_price)
else:
    print("Final price after applying the discount:", final_price)
