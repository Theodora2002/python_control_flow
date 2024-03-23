cart = {
    "TV" : 
        {
            "price" : 200000,
            "decription" : "black 75'"
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
for x in cart:
    # print(cart[x]["price"])
    priceSum += cart[x]["price"]
    
print(f"Your total price is: {priceSum}")
