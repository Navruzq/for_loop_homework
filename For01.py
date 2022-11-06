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
    list1=[]
    for i in range(n):
        list1=list1+[i]
    return list1
print(main(5))


        