def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
        
    Returns:
        float: The final price after discount if discount_percent >= 20,
              otherwise the original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price

# Get user input
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate and display the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    if final_price < original_price:
        print(f"A {discount_percentage}% discount was applied.")
        print(f"Final price after discount: ${final_price:.2f}")
    else:
        print("No discount was applied because the discount percentage is less than 20%.")
        print(f"Original price: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")