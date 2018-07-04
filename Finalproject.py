def scalarvecmulti(scalar,vector):
    """
    The function scalarvecmulti(scalar,vector)
    1: the function checks to see if the elements in vector are int float or complex numbers
        if they are not the function prints out invalid input
    2: The function first goes through and makes sure that the scalar is an
       integer and that the vector is a list. If the scalar is not an integer or
       the vector is not a list the function prints out "Invalid Input"
    3: The function then sets a variable titled sclaranswer as an empty list.
       The function then goes through a for loop and goes through all the
       numbers in the entire length of the vector
    4: the function then sets a variable as scalaranswer1 and in the variable
       multiplies the scalar by all the elements in the vector.
       the function then appends the results in scalaranswer1 to scalaranswer
       and returns the updated list in scalaranswer. 
       
    """
    for i in range(len(vector)):
       inputstatus = True
    for i in range(len(vector)):
        if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            scalaranswer=[]
            for i in range(len(vector)):
                scalaranswer1=scalar*vector[i]
                scalaranswer.append(scalaranswer1)
        return scalaranswer

def dot(vector01,vector02):
    """
    This function does the following.
    1: The function checks to see if the elements in vector01 are int float or complex numbers
       if they are not the function prints invalid input
    2: The function first checks to see if the vectors are list if they
       are not list the function prints Invalid Input and retruns None.
    3: The function defines a variable as isvalid and states the
       length of vector01 is equal to vector02 if the variable is False
       the function prints out Invalid Input and returns None
    4: The function then sets a variable titled answer.
    5: The function then implements a for loop and goes through the numbers in
       the entire length of the vectors and multiplies each element of vector1
       to each element of vector 2 and returns the dot product in the variable
       answer. 
    """
    for i in range(len(vector01)):
       inputstatus = True
    for i in range(len(vector01)):
        if ((type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            isvalid=len(vector01)==len(vector02)
            if isvalid is False:
                print("Invalid Input")
                return None
            answer=0
            for i in range(len(vector01)):
                answer+= vector01[i]*vector02[i]
        return answer

def vecsubtract(vector01,vector02):
    """
    The function vecsubtract(vector01,vector02) does the following.
    1: The function checks to see if the elemetns in vector01 are int float or complex numbers
       if they are not the function prints out invalid input
    2: The function checks to see if vector01 or vector 02 is a list
       if its not a list the function prints out Invalid Input and returns
       None.
    3: The function sets a variable titled isvalid and states that
       the length of vector01 is equal to vector02. If the lenghts are not
       equal the function prints Invalid Input and returns None.
    4: The function sets a variable titled answer as an empty list.
    5: the function then goes through a for loop and goes through the numbers
       in the entire length of vector01, it then sets a variable titled
       addedanswer and in the variable addedanswer subtracts the elements in
       vector02 from the elements in vector01
       the results from addedanswer are then appended to the emptylist in the
       variable answer and returns the updated list in the variable answer. 
    """
    for i in range(len(vector01)):
        inputstatus = True
        for i in range(len(vector01)):
            if ((type(vector01[i]) != int) and (type(vector01[i]) != float) and (type(vector01[i]) != complex)):
                inputstatus = False
                print("Invalid Input")
            if inputstatus == True:
                if type(vector01) != list or type(vector02) != list:
                    print("Invalid Input")
                    return None
                isvalid=len(vector01)==len(vector02)
                if isvalid is False:
                    print("Invalid Input")
                    return None
                answer=[]
                for i in range(len(vector01)):
                    addedanswer = vector01[i]-vector02[i]
                    answer.append(addedanswer)
                return answer 

def twonorm(vector):
    """
    The function does the following.
    1: a variable titled imputstatus is set to the boolean True
    2: The function checks to see if the elemetns in the function
       are integers booleans and floating point numbers
    3: if the inputs are true a variable titled result is set
       to 0
    4: A for loop is implemented and a variable titled result is set
       in the variable the loop adds teh variable result and squares teh elements
       in the vector and teh outside function result takes the square root of the
       squares and returns the result. 
    """
    for i in range(len(vector)):
       inputstatus = True
    for i in range(len(vector)):
        if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            result = 0
            for i in range(len(vector)):
                result = result + (vector[i]**2)
            result = result**(1/2)
        return result 

def normalized(vector):
    """
    The function does the following.
    1: The function checks to see if the elements in vector are int float and complex numbers
       if they are not the function prints out invalid input
    1: A variable with an empty list is implemented.
    2: a for loop is implemented that divides the elements in the vector
       by teh two norm
    3: The resulting elements are then appended into the empty list and the
       new values are returned. 
    """
    result_normalized=[]
    for i in range(len(vector)):
        inputstatus = True
    for i in range(len(vector)):
        if (type(vector[i]) != int and type(vector[i]) != float and type(vector[i]) != complex):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            for i in range(len(vector)):
                normalization = vector[i]/twonorm(vector)
                result_normalized.append(normalization)
        return result_normalized

def QR(A):
    """
    The function AR(A) does the following
    1: a variable m is set to the len of A from the first index
    2: a variable n is set for the entire lenth of A
    3: a variable v is set to A
    4: a variable R is set that multiplies the elements of n by zero
    5: a varia Q is set that multiplies the elements of m by zero.
       that creates a zero matrix
    6: A for loop is implemented that does the following
        1: the twonorm defined earlier is calculated throughout A
        2: the normalized vector is computed using the normalized function defined earlier.
    7: A for loop is implemented.
       1: The dot product is aquired
       2: the vectors are multiplied by a scalar.
       3: The vectors are subtracted from each other.
    8 we return the results. 
    """ 
    m = len(A[0])
    n= len(A)
    v = A
    R = [[0]*n for i in range(n)]
    Q = [[0]*m for i in range(m)]
    for i in range(n):
        R[i][i]= twonorm(v[i])
        Q[i] = normalized(v[i])
        for j in range(i+1, n):
            R[j][i] = dot(Q[i],v[j])
            temp = scalarvecmulti(R[j][i],Q[i])
            v[j] = vecsubtract(v[j],temp)
    return [Q,R]
"""
A is the representation of the matrix given
the print fucntion prints out the QR factorization of A
"""
A = [[1,1,1,1,1,1,1,1,1,1],
    [.55,.60,.65,.70,.75,.80,.85,.90,.95,1],
    [.3025,.36,.4225,.49,.5625,.64,.7225,.81,.9025,1.00],
    [.166375,.216,.274625,.343,.421875,.512,.614125,.729,.857375,1.00]]

print(QR(A))


def transpose(matrix):
    """
    This function first checks to see if the elemetns in matrix are int float and comple
    if they are flase the function returns invalid input
    This function sets an empty list titled result
    the goes through the elements in the matrix
    and appends the the elements in the collums to the rows and returns
    the transpose
    """
    inputstatus = True
    for i in range(len(matrix)):
        if (type(matrix[i]) != int and type(matrix[i]) != float and type(matrix[i]) != complex):
            inputstatus = False
            print("Invalid Input")
        if inputstatus == True:
            if type(matrix) != list:
                print("Invalid Input")
                return None
        result = []
        for i in range(len(matrix[0])):
            collumn = []
            for j in range(len(matrix)):
                collumn.append(matrix[j][i])
            result.append(collumn)
        return result

def matvec(matrix,vector):
    """
    This matrix checks to see iof the elemetns in matrix are int float anc complex numbers if they are not the function prints out invalid input.
    if its true the function checks to see if the matrix is a list if its not a list the function prints out invalid input
    if it is a list the function multiplies the collumns and rows by a vector and returns the result. 
    """
    inputstatus = True
    for i in range(len(matrix)):
        if (type(matrix[i]) != int and type(matrix[i]) != float and type(matrix[i]) != complex):
            inputstatus = False
        if inputstatus == True:
            if type(matrix) != list:
                print("Invalid Input")
                return None
        result=[]
        for i in range(len(matrix)):
            total = 0
            for j in range(len(vector)):
                total += matrix[i][j]*vector[j]
            result.append(total)
        return result

"""
the variable x defines the variables given in the i collumn from the handout
The variable y defines the variables given in teh j collumn from the handout
"""
x = [.55,.60,.65,.70,.75,.80,.85,.90,.95,1]

y = [1.102,1.099,1.017,1.111,1.117,1.152,1.265,1.380,1.575,1.857]

# I was not able to compute Q*y
# I was not able to compute Rc=Q*y for c
# I was not able to define backsubstitution function

        
# Part two written part of the project.

"""
Question One: The diffrences made to the classical Gram-Schmidt to obtain Modified Gram- Schmidt is the order of which the operations are carried out
            In the Algorithm

            1: In the classsical Gram schmidt
            2: The norm of the vector is calculated
            3: The vector is divided by the norm
            4: the next vector is taken
            5: the vector is multiplied by the first normalized vector transpose
            6: The product of the first normalized vector and the norm are subtracted from the second vector
            7: The norm of vector 2 is taken
            8: The vector 2 is divided by the norm of vector 2.
            9: we then Get Q
            10: and R

            1: In the Modified Gram Schmidt
            2: The norm of the first vector is taken.
            3: teh first vector is divided by teh norm
            4: the normolized vector transpose is multiplied by vector two
            5: The result of the normolized vector transpose multiplied by vector two is subtracted from vector two.
            6: the norm of vector two is taken.
            7: vector two is divided by the norm
            8: from there we get Q
            9: from there we get R

            Although on paper both algorithms get the same result, in the computer due to roundoff error the results are diffrent and due to those
            diffrences, it results in the classical gram schmidt being unstable and the modified gram schmidt being stable. and since the modified
            gram schmidt is stable it is necessery to have

Question three: Briefley explain the concepts of conditioning and stability and why they are necessary.

            1: Conditioning measures the effects of small changes to our problem  and stability measures small changes that affect our solution.
            2: furthermore an example of conditioning is we can define a problem as a function  f:x--->y where f is the problem x is the data y is the solution.
            3: we can then say a problem is ill-conditioning if a small change leads to a big change in f(X)
            4: In addition there are diffrent types of stability. For example we say an algorithm is forward stable if in algorithm gives the right answer to nearly the right question.
            5: We say an algorithm is backwards stable if an algorithm gives exactly the right answer to nearly the right question. 
                
"""
     
    
    


    
































        


    
    








