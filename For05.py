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
    for i in range(A,B+1):
       list1.append(i)
      
    return list1[::-1]
print(main(2,7))