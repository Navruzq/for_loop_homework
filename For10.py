def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    i=0
    s=[]
    while i<len(list1):
        s+=[list1[i].title()]
        i+=1
    return s
print(main(['rustam','diyor']))