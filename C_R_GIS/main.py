#here is the target array, if the applicant answers the question properly the answer is 8
array1 = [0,1,0,2,1,0,3,1,0,1,2,0]

#start of logic function
def trap():
    stack = []
    water = 0
    i = 0
    while i < len(array1):
        if len(stack) == 0 or array1[stack[-1]] >= array1[i]:
            stack.append(i)
            i += 1
        else:
            x = stack[-1]
            stack.pop()
            if len(stack) != 0:
                temp = min(array1[stack[-1]], array1[i])
                dist = i - stack[-1] - 1
                water += dist * (temp - array1[x])
    return water





#this prints off the max water area
done = trap()
print(f"done the answer is {done} units of rainwater")
