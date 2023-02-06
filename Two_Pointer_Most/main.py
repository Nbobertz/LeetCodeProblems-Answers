#This is the most water containor problem but solved usign the two pointer algorithm

#the whole point of this python file is to demonstrate how we can drasticly decrease the runtime by assigning more memory to, in this case, variables that hold the position of 'pointers' in an array.

#Once our while loop has progressed through the first loop, it will determine to either push the P1 closer or the P2 closer to the center. All the while it will calculate the max area and save it to a variable outside the while loop. Once the loop ends by both pointers meeting in the center it terminate and then report back the max area size

#this block of code acts as the interviewer
print("Welcome to the 'most-water' leetcode question. This question is designe to find the maximum area in a x/y graph between two integers in a list. The question starts off with asking you to define the numbers in the arrsay and then will provide the two integers with the largest area between them")
given_array_str = input('give me a list of numbers seperated with a ,\n').split(',')
int_array = [int(x) for x in given_array_str]

#below is the algorithm
def max_water_contain():
    p1 = int_array[0]
    p2 = int_array[-1]
    max_area = 0
    while int_array.index(p1) < int_array.index(p2):
        height = min(p1,p2)
        width = int_array.index(p2)-int_array.index(p1)
        print(width)
        area = height*width
        max_area = max(area,max_area)
        if p1 <= p2:
            p1 = int_array[p1+1]
        else:
            p2 = int_array[p2-1]
    return max_area

#this block prints out the max area
done=max_water_contain()
print(done)

