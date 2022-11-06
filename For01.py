import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    a=[]
    
    for i in range(n):
       a.append(i)
    return a
print(main(5)) 
 
        