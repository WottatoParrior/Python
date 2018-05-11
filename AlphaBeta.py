
tree = [[[1, 8], [5], [6, 4, 7], [9], [3, 2], [6, 10, 2]]]   #This is the tree we are working with


a=-float('Inf')       #Initializing a & b as infinity and -infinity
b=float('Inf')
BetaVal=[]              #Also initializing a BetaVal list in which we will apend our beta values

def alphabeta(node, alpha, beta, StartingPlayer):
    global BetaVal
    if not isinstance(node, list):            #Checking if node is an edge node, by it not being a list
        v = node
        return v
    if StartingPlayer == 0:                 #If starting player ==0 , starting player is Max, if 1 starting player is Min

        v = -float('Inf')
        for child in node:
            v = max(v, alphabeta(child,alpha,beta,1))               #Alphabeta is running for each child of the node, then inserts that value at v
            alpha = max(alpha,v)                                    #and then checks the bigger value bewtween v and alpha, and inserts it into alpha, as then new biggest alpha
            if beta <= alpha:                                       #alternating each player by changing the value of StartingPlayer variable to 0 and 1 respectively
                break
        return v
    else:
        v = float('Inf')
        for child in node:
            v = min(v, alphabeta(child,alpha,beta,0))               #Same thing as above but now, we are not seeking the max but the min and inserting the value at beta
            BetaVal.append(beta)
            beta = min(beta,v)
            if beta <= alpha:
                break
        return v

alphabeta(tree,a,b,0)                                               #Calling the alphabeta with our tree, a, b, and starting player as 0(Max) as parameters
print (("The result is "),(BetaVal[len(BetaVal)-2]))                   #The code is running one more time than it should, so we appended them to a BetaVal list and we call the one before the last
                                                                       #so we get the result we want




