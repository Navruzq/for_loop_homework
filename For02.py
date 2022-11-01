def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    i=0
    a=''
    while i<n:
        if i==n-1:
            a+=str(i)
        else:
            a=a+str(i)+','
        i+=1
    return a

print(main(8))