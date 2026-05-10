# collect the name of item from the terminal from the user
# collect the price of the item from the terminal from the user
# collect promotional-code from the terminal from the user
# calculate for when discount code applied is "SAVE10" to apply 10% discount
# calculate for when discount code applied is "HALFOFF" to apply 50% discount
# write a logic that accounts for when no discount code is applied

item_name = input("enter item name: ")
item_price = float(input("enter item price: "))
promo_code = input("enter promo code: ").upper()

def ten_off_discount(price):
    discount = price * 0.10
    return discount
    
def fifty_off_discount(price):
    discount = price * 0.50
    return discount
    
if promo_code == "SAVE10":
    discount = item_price - ten_off_discount(item_price)
    print(f"10% discount applied, you'll pay: {discount:.2f}")
elif promo_code == "HALFOFF":
    discount = item_price - fifty_off_discount(item_price)
    print(f"50% discount applied, you'll pay: {discount:.2f}")
else: print("no discount applied")
