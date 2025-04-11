#add two lists using lists and lambda
n1 = [1, 2, 3]
n2 = [4, 5, 6]
result = map(lambda x, y: x + y, n1, n2)
print("addition of two lists is", list(result))


#square of a number using map function
nums = [1, 2, 3, 4, 5]
def square(n):
    return n * n

sqnum = list(map(square, nums))
print("square of a number is", sqnum)



#zip elements of two lists
s1 = {2, 3, 1}
s2 = {'b', 'c', 'a'}
s3 = zip(s1,s2)
print(list(s3))

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x,y in zip(list1,list2[::-1]):
    print(x,y)

#zip in dictionary
stocks = ["Samsung", "Apple", "Google"]
prices = [20000, 10000, 30000]

newdict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(newdict)


#exit function
for i in range(10):
    
    if i == 5:
        exit()
    print(i)