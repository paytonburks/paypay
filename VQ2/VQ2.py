# a list is a sequence of items
# ID lists like a single row or column
# declare a list using [,]


#            -4 -3 -2 -1
list_ints = [0, 1, 10, 20]
#index starts at 0, last element n-1; n = num elements
#negative elements too

print(list_ints[-4])

#types can be mixed in the list

list_numbers = [0, 0.0, 1.0, -2]
print(list_numbers)
print(type(list_numbers))

#use len() to find out how manyu elements are in the list

print(len(list_numbers))
list_numbers.append("another element")
print(len(list_numbers))

print(list_numbers[len(list_numbers) - 1])

#we can declare an empty list woo! or lists of lists

#loop time

candies = ["twix", "reeses"]

for candy in candies:
    print(candy)

i=0
while i < len(candies): 
    print (i, candies[i])
    i+= 1

#common list operators
#list concatenation... adding 2 lists together

print(candies)
candies += ["m&ms", "starbursts"]
print(candies)

bag_o_candies = 5 * ["twix", "snickers"]
print(bag_o_candies)

#list slicing
print(candies[1:2]) # : is the slice operator; start index is inclusive, end index is exclusive

#if you ever need a copy, you can use the slice





