import numpy as np
mat = np.random.randint(1,101, size=(5,5))  #np.random module makes matrix with random values. We can further specify the datatype, like
                                            #np.random.rand gives random float values, np.random.randint gives random integer values
"""below a guard to avoid printing the entire code, when I will import the matrix mat in the next question's program
How it works is that, each python file is a module. And python by default assigns a variable __name__ to every variable.
When a python program is run directly, __name__ is assigned the vaue(string) __main__. However, when imported in another file, __name__  is assigned
its filename as the string. """
if __name__ == "__main__": 
    print("Here is the 5x5 matrix with random integers:")
    print(mat)
    max = mat.max()
    min = mat.min()
    mean = mat.mean()
    print("Max entry: ", max)
    print("Min entry: ", min)
    print("Mean value of all 25 entries: " , mean)

    #normalisation
    print("Normalisation now")                   #Normalisation means changing the data so as to fit all values in a particular range
    normat = [ (mat - min)/(max-min)]    #formula for min-max norm = (x - x(min)) / (x(max) - x(min))
    print(normat)

    #flattening
    print("Flattening now")
    flatmat = mat.flatten()           #.flatten() is for conversion to 1d array only. For others, we can use .reshape(row,column); that too if  
                                      # we use -1 in any of row or column, numpy figures out on its own.
    print(flatmat)

    #sorting
    print("Sorting the 1d array now")
    flatmat.sort()  #if we had used np.sort(flatmat), it would;ve given us a new sorted array. flatmate.sort() sorts flatmat itself
    print(flatmat)

