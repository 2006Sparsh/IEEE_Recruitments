para = input("Enter a paragraph :")


words = para.split() #split() turns the string of words into a list of strings, each word being one seperate string
#We cannot procede without splitting it into a seperate string for every seperate word, because then one non-palindrome will reject the entire para
 
#checking for 100 words max
if len(words) > 100:
    print("Pls enter a para of less than 100 words")
else:
    palindromes = []
    for word in words:     #defines a variable word, which if its in the words of para, is checked before going into this loop
        if word.lower() == word.lower()[::-1]:  #word.lower() reduces all letters to lowercase
            palindromes.append(word)            #word.lower()[::-1] reverse the string(word) coz it makes it start from index -1, i.e. last letter

    if len(palindromes) == 0:
            print("0 palindromes in given para")
    else:
            print("The" , len(palindromes) , "palindromes in the paragraph are: " , palindromes)

            




    



