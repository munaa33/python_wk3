def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after discount
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        # Return the original price if discount is less than 20%
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the final price or the original price
final_price = calculate_discount(original_price, discount_percent)

print(f"The final price is: ${final_price:.2f}")
