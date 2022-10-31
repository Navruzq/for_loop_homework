import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    i=0
    a=list1=[]
    while i<n:
        list1=list1+[i]
        i+=1
    return list1
print(main(5))
        