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
    for i in range(n):
        list1=list1+[k]
    return list1
print(main(-1,4))    