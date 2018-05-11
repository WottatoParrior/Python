leaf=[]
leaf.append([1,8])                  #The tree creation but not in the most optimal way, it was a test to check some things
leaf.append([5])
leaf.append([6,4,7])
leaf.append([9])
leaf.append([3,2])
leaf.append([6,10,2])
maxVal=[]                           #The maximum values are storen in maxVal and the minimum at minVal
minVal=[]
count=0                             #A count we will use later on

def childset_max(counter,*arg):     #This function, depending on the length of the list, finds the biggest value contained in that list and appends them to maxVal and leaf,returning the list maxVal
    global maxVal
    if len(arg)==3:
        if arg[0] > arg[1]:
            if arg[0] > arg[2]:
                maxVal.insert(counter,arg[0])
                leaf[counter]=[maxVal[counter]]
            else:
                maxVal.insert(counter,arg[2])
                leaf[counter]=[maxVal[counter]]

        else:
            if arg[1] > arg[2]:
                maxVal.insert(counter,arg[1])
                leaf[counter] = [maxVal[counter]]
            else:
                maxVal.insert(counter,arg[2])
                leaf[counter] = [maxVal[counter]]
    elif len(arg)==2:
        if arg[0]>arg[1]:
            maxVal.insert(counter,arg[0])
            leaf[counter] = [maxVal[counter]]
        else:
            maxVal.insert(counter,arg[1])
            leaf[counter] = [maxVal[counter]]
    else:
        maxVal.insert(counter,arg[0])
        leaf[counter] = [maxVal[counter]]

    return maxVal

def childset_min(counter,*arg):             #Function works the same wasy as the childset_max, but this time finds the minimum ones
    global minVal
    if len(arg)==3:
        if arg[0] < arg[1]:
            if arg[0] < arg[2]:
                minVal.insert(counter,arg[0])
                leaf[counter]=[minVal[counter]]
            else:
                minVal.insert(counter,arg[2])
                leaf[counter]=[minVal[counter]]

        else:
            if arg[1] < arg[2]:
                minVal.insert(counter,arg[1])
                leaf[counter] = [minVal[counter]]
            else:
                minVal.insert(counter,arg[2])
                leaf[counter] = [minVal[counter]]
    elif len(arg)==2:
        if arg[0]<arg[1]:
            minVal.insert(counter,arg[0])
            leaf[counter] = [minVal[counter]]
        else:
            minVal.insert(counter,arg[1])
            leaf[counter] = [minVal[counter]]
    else:
        minVal.insert(counter,arg[0])
        leaf[counter] = [minVal[counter]]

    return minVal

def min_move():        #Instead of calling manually the childset_min, depending on the length of the leaf, we created this function to do this for us
    count=0
    while (count < min(6, len(leaf))):
        if len(leaf[count])==1:
            childset_min(count, leaf[count][0])
        elif len(leaf[count])==2:
            childset_min(count, leaf[count][0], leaf[count][1])
        elif len(leaf[count]) == 3:
            childset_min(count, leaf[count][0], leaf[count][1], leaf[count][2])
        elif len(leaf[count]) == 4:
            childset_min(count, leaf[count][0], leaf[count][1], leaf[count][2], leaf[count][3])
        elif len(leaf[count]) == 5:
            childset_min(count, leaf[count][0], leaf[count][1], leaf[count][2], leaf[count][3], leaf[count][4])
        elif len(leaf[count])==6:
            childset_min(count, leaf[count][0], leaf[count][1], leaf[count][2],leaf[count][3],leaf[count][4],leaf[count][5])
        count=count+1
    return minVal

def max_move():         #Same thing as min_move but for maximum Values
    count=0
    while (count < max(6, len(leaf))):
        if len(leaf[count])==1:
            childset_max(count, leaf[count][0])
        elif len(leaf[count])==2:
            childset_max(count, leaf[count][0], leaf[count][1])
        elif len(leaf[count]) == 3:
            childset_max(count, leaf[count][0], leaf[count][1], leaf[count][2])
        elif len(leaf[count]) == 4:
            childset_max(count, leaf[count][0], leaf[count][1], leaf[count][2], leaf[count][3])
        elif len(leaf[count]) == 5:
            childset_max(count, leaf[count][0], leaf[count][1], leaf[count][2], leaf[count][3], leaf[count][4])
        elif len(leaf[count])==6:
            childset_max(count, leaf[count][0], leaf[count][1], leaf[count][2],leaf[count][3],leaf[count][4],leaf[count][5])
        count=count+1
    return maxVal

def minmaxfind():       #Our main function that calls the other ones and finds the result

    global leaf
    max_move()
    leaf=[]             #We empty the list, so we can create a new tree with our new values
    leaf.insert(0,[maxVal[0],maxVal[1],maxVal[2]])
    leaf.insert(1,[maxVal[3],maxVal[4],maxVal[5]])
    min_move()                              #We alternate between max_move and min_move, while creating the new tree at each step
    leaf=[[minVal[0],minVal[1]]]
    childset_max(0,leaf[0][0],leaf[0][1])       #Max_move is not called here, since it came up with an unexpected error, so we had to call manually the childset_max function
    print('Result is',leaf)

minmaxfind()











