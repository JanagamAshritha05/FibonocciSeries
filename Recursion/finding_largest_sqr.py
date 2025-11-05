def get_largest_sqr(num):
    each_sqr = num[0]**2 
    if len(num)==1:
        return each_sqr 
    return max(each_sqr, get_largest_sqr(num[1:]))


num=[1, 2, 3, 4] 
res=get_largest_sqr(num) 
print(res) 


