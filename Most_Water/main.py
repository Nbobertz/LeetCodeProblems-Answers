#(Softwrap this)You are given a range of positive integers where each integer represents the height of a vertical line on a chart. The goal of this problem is to have you write a function that will calculate which two integers in the array would hold the most amount of water. Return the area of the water.

#Forumula for area of a square: L*W = area

#Assumptions: 1: The lines on both the x and y axis have no value to them. They take up no space. 2: You can not use the walls of the graph to hold water. This would allow you to pull the axis which means the 0 and -1 position would automatticaly be the maximum. 3: Individual lines can not sever the area of the graph by cutting through your water containor. For example if index position 5 in your graph is the dead center of your water containor it does not seperate the water containor into two sections, esentially the largest area does not have to be between eachother.4: The water will spill out of the highest Y axis number. For exapmle a water contanior with the y axis of 5 and 7 will only fill up to 5 because one of the walls will overpour.

#Algorithim: Here you can do a pointer algorithm and push that into a function that will calculate the area between the two index positions. It is possible to have a brute force solution that tests the area for each pair of numbers but that might not be the optimal solution depending on Big O. From Brute force simply start scaling back your for loops and putting constants.

#here is the solution


#this is the basics for the intervewer to ask. It provides a prompt along with an imput that will create the int list.
print("Welcome to the 'most-water' leetcode question. This question is designe to find the maximum area in a x/y graph between two integers in a list. The question starts off with asking you to define the numbers in the arrsay and then will provide the two integers with the largest area between them")
given_array_str = input('give me a list of numbers seperated with a ,\n').split(',')
int_array = [int(x) for x in given_array_str]

#below is the function that contains all the logic to solve this problem. It takes the array, provides the equation to find the target area. At the end of the function it prints out the two integers which create the maximum water holder. This can be edited to make the program either consume less memory or have better O(n) scaling. It is the brute force solution. It iterates through each set to find the largest area. By far not the most efficent solution but the easiest to impliment.

def work_now():
    area = 0
    for l in range(len(int_array)):
        for r in range(l+1, len(int_array)):
            area1 = (r-l)* min(int_array[l], int_array[r])
            if area1 > area:
                area = area1

    print(area)
work_now()