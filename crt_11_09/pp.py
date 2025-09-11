
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
        