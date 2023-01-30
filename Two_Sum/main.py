#this program demonstrates the popular leetcode question two-sum.
#Essentially, what we are doing here is taking a given array of integers, establishing a target integer, and then returning the position within the array for two integegers that add up to the target array.

#there are 4 steps to solving any leetcode problem. First, you have to ask and establish edge cases such as are the numbers only positive or can they be negative, can there be multiple solutions in the answer, or can any of the integers be repeated in the array? Second, after you have established the edge cases then you have to write up the ideal solution. Here you demonstrate that you understand the asked questions and ask further quetisons. Third, you find a solution logically without code. Here is where the interviewer can see your thought process in action. Fourth, after you have established the logic then it is time to code up the problem.

#For this here are the peramiters of the question that establish the edge case. There can be no negatives, multiple solutions per array, the numbers do not repeat, and there will never be negatives. If there is no solution in the array we will return the string 'null'

#The secret to doing the two-sum array problem is understanding the algorithm of Two Pointer technique. There are multiple ways that you can do this. Here is the basic pattern for the algorithm.


#the below code takes an input of numbers and turns it into the target array. First we ask the console user what they would like in the array and then we convert this using Pythonic list comprehension into an array of integers
array_1 = input("What numbers would you like to have in the array? Seperate the numbers with a comma (,)\n").split(',')
array_int = [int(x) for x in array_1]

#now we establish the target that the two-sum problem will add up to in our array.
target_str = input("What is the target number that you want me to find an addition pair for in the array?")
target = int(target_str)

#below is the brute force way of doing the two pointer technique. This is not efficent with Big O but is the most robust solution.
null = 0
for n in array_int:
    n_needed_forsolution = target - n
    if n_needed_forsolution in array_int:
        print(array_int.index(n),array_int.index(n_needed_forsolution))
        exit()
    else:
        null = 1
if null == 1:
    print('null (pair of numbers to add together to equal target not found in array)')
else:
    exit()

