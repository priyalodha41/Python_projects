# x=121
# str=str(x);
# list2=list(str);
# print(list2)
# list2.reverse();
# x2="".join(list2);
# # print(int(x2))
# print(x)
# print(x==x2)
# # if(list2==list2.reverse()):
# #     print("true");
# # else:
# #     print("false");

# def fun(n):
#     if n==0:
#         return 0
#     # the value will be stored in the recursive call stack and will be printed in reverse order 1234
#     # otherwise it should be printing 4 3 2 1
#     fun(n-1); 
#     print(n,end=" ");
    
# fun(4);
# nums=[122,3,5,6,7,8,9,10]

# start=[0]*len(nums)

# print(start)

st=[]
s="erase*****"

for ch in s:
    if ch=="*":
        st.pop()
    else:
        st.append(ch)

print("".join(st))