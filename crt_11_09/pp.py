# Convert a number n from base g to base d

# n = int(input())
# g = int(input())
# d = int(input())

# p = 0
# s = 0
# while(n > 0):
#     r = n % 10
#     s += r * (g**p)
#     p +=1
#     n //= 10
# print(s)
# p1 = 0
# s1 = 0
# while(s > 0):
#     rem = s % d
#     s1 += rem * (10 ** p1)
#     p1 += 1
#     s //= d
# print(s1)

# n=123
# ans=0
# while(n>10):
#     d=n%100
#     ans+=d
#     n//=10
# print(ans)

# a=1
# while(n>0):
#     r=n%10
#     a*=r
#     n//=10
# print(a)

# Convert a number to any base  
# n = int(input())
# g = int(input())
# d = int(input())
# t = n
# w = 0
# while(t > 0):
#     r = t % 10
#     if(r >= g):
#         w = 1
#         print("Invalid")
#         break
#     t = t // 10
# if(w == 0):
#     if(g == 10 or d == 10):
#         p = 0
#         s = 0
#         while(n > 0):
#             r = n % 10
#             s += r * (g**p)
#             p += 1
#             n //= 10
#         print(s)
#     else:
#         p = 0
#         s = 0
#         while(n > 0):
#             r = n % 10
#             s += r * (g**p)
#             p +=1
#             n //= 10
#         print(s)
#         p1 = 0
#         s1 = 0
#         while(s > 0):
#             rem = s % d
#             s1 += rem * (10 ** p1)
#             p1 += 1
#             s //= d
#         print(s1)
        
# n = int(input())
# sum = 0
# while(n > 10):
#     r = n % 100
#     rev = 0
#     while(r > 0):
#         r1 = r % 10
#         rev = rev * 10 + r1
#         r //= 10
#     sum += rev
#     n = n // 10
# print(sum)
