def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    list1=[]
    i=0
    n=B-A
    while i<=n:
        list1=list1+[B-i]
        i+=1    
    return list1
print(main(5,9))