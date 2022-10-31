def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list1=[]
    i=0
    while A<=B:
        list1+=[A]
        A+=1
    return list1
print(main(2,7))