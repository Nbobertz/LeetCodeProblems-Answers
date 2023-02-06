This program demonstrates how we can solve the 'most water' leet code problem by simply using the two pointer algorithm. Here instead of looping through each possible answers like an animal we will assign the -1 index and 0 index as pointers and then move them inside the array closer together. By the time the pointers meet they will have calculated all possible answers for the max area of water.

The reason why people should know about the two pointer algorithm is because it halves the runtime of a program but results in increased memory.

Simply open the main file and run. Input the following array for testing

1,8,6,2,5,4,8,3,7

The answer should be 49