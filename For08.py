def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    s=0
    for i in range(N+1):
        if i!=0:
            s+=1/i
        else:
            s=0
    return s
print(main(5))