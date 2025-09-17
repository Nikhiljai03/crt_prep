# l = [5,3,1,6,7,8,4,2,17,3]
# sl = []
# for i in range(0,len(l)-2):
#     sum = 0
#     for j in range(i,i+3):
#         sum += l[j]
#     sl.append(sum)
# print(sl)

# l = [5,3,1,6,7,8,4,2,17,3]
# k = 3
# max_sum = 0
# current_sum = 0
# for i in range(0,k):
#     current_sum += l[i]
# max_sum = current_sum
# for i in range(k,len(l)):
#     current_sum = current_sum - l[i-k] + l[i]
#     if current_sum > max_sum:
#         max_sum = current_sum
# print(max_sum)

# s = "abacddcbkbb"
# k = 4
# u = []
# for i in range(len(s)-k+1):
#     w = s[i:i+k]
#     if len((set(w))) == k:
#         u.append(w)
# print(u)

