def convert_str_int(num_list):
    new=[]
    for i in num_list:
        new.append(int(i))
    return set(new)

num=input().split(',') 
n=int(input()) 
int_list=convert_str_int(num)
int_list=list(sorted(int_list))
index=0
for i in int_list:
    for j in int_list[index+1:]:
        if (i+j==n):
            pair=(i,j)
            print(tuple(sorted(pair)))
            index+=1 
            
###### 
def convert_str_to_int(val):
    new=[]
    for i in val:
        new.append(int(i))
    return new

def get_unique_pairs(int_list,n):
    unique_pairs_set=set()
    for i in range(len(int_list)):
        num1=int_list[i]
        num2=n-num1 
        rem_list=int_list[i+1:]
        if num2 in rem_list:
            pair=(num1,num2)
            pair=tuple(sorted(pair))
            unique_pairs_set.add(pair)
    return unique_pairs_set 

num=input().split(',')
n=int(input()) 
int_list=convert_str_to_int(num)
unique_pairs=get_unique_pairs(int_list,n)
unique_pairs=list(sorted(unique_pairs))
for pair in unique_pairs:
    print(pair)

           
            
 