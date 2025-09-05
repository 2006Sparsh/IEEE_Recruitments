cutoff = [["Pilani" , "CS" , 327] ,               #creating a list, called cutoff, with several other lists inside it
          ["Pilani" , "Chemical" , 247] ,
          ["Pilani" , "MSC ECO" , 271] ,
          ["Pilani" , "MSC BIO", 236] ,
          ["Hyderabad" , "CS" , 298] ,
          ["Hyderabad" , "Chemical" , 238] ,
          ["Hyderabad" , "MSC ECO" , 261] ,
          ["Hyderabad" , "MSC BIO" , 234] ,
          ["Goa" , "CS" , 301] ,
          ["Goa" , "Chemical" , 239] ,
          ["Goa" , "MSC ECO" , 263] ,
          ["Goa" , "MSC BIO" , 234] ]

dictionary = {}
for campus, branch, marks in cutoff:   #this command segregates each of them into campus, branch and marks
        if campus not in dictionary: #checks if the campus dictionary is alr created in the nested dictionary. We need to check this as
                                          #if we dont, after the first branch in a campus, for the 2nd branch python will simply overwrite the
                                          #previous entry . after 4 executions of the loop, we will end up with only MSC BIO (as its the last in
                                        #our branch order)
                                        #so what we can do is, we check if the campus dict alr exists. If yes, we skip the step and add the new 
                                        #branch. If no, we create the dict for that campus and then add one branch.
                               
            dictionary[campus] = {}   
        dictionary[campus][branch] = marks  
print(dictionary)

