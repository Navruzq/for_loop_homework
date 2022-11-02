def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s=[]
    i=1
    while i<=10:
        s+=[price*i]
        i+=1
    return s
print(main(2.25))