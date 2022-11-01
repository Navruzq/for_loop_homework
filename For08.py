def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    i=0
    s=0
    while i<=N:
        if i!=0:
          s+=1/i
        else:
            s=0
        i+=1
    return s
print(main(4))