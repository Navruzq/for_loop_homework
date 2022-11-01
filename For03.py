def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    
    list1=[]
    i=0
    while i<n:
        list1=(list1+[k])
        i+=1
    return list1
print(main(-1,4))   