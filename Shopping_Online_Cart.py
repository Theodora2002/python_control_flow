# Dictionary declaration
cart = {
    "TV" : 
        {
            "price" : 200000,
            "description" : "black 75'"
        },
    "Office-chair":
        {
            "price" : 45000,
            "decription" : "gray 100cm"
        },
    "mattress":
        {
           "price" : 42000,
            "description" : "soft 6*6 high density"  
        },
    "speakers":
        {
           "price" : 50000,
            "description" : "JBL BASS BOOSTER"  
        }
}
priceSum = 0
for x in cart:    # For dictionary X in the cart dictionary,                             
    print(cart[x]["price"]) # print the items under the key "price" in the x dictionaries looped
    priceSum += cart[x]["price"]  #Getting the totals of prices printed from the loop   
print(f"Your total price is: {priceSum}")

# Discounts calculation for priceSum > 200,000
discount = 0
if priceSum >= 200000:
  print("Eligible for discount and free shipping")
  discount = (0.05 * 200000)
  print(f"Discount is {discount}")

# Total amount payable calculation.
payable = priceSum - discount
print(f"Total amount payable is {payable}")
