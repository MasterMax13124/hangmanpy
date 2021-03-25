import random

def findOccurrences(s, ch): #from https://stackoverflow.com/questions/13009675/find-all-the-occurrences-of-a-character-in-a-string
    return [i for i, letter in enumerate(s) if letter == ch]

if __name__ == "__main__":
    wordlist = ""
    with open ("wordlist.txt", "r") as myfile:
        wordlist=myfile.readlines()
    
    #picking a random word from the wordlist:
    index = random.randint(0,1000)
    word = wordlist[index][:-1] #!!WARNING!! this might have to be changed when using a different wordlist!
    #print("wordlength", len(word))

    #start of the game:
    hitpoints = 5
    gamerunning = True
    triedlist = ""

    #print(word) #just for debugging
    crypword = '*' * len(word)

    #first tip:
    hint = random.randint(0, len(word) -1)
    #print("hint 1", hint)
    occurlist = findOccurrences(word, word[hint])
    for i in occurlist:
        crypword = crypword[:i] + word[hint] + crypword[i+1:]
    hint = random.randint(0, len(word) -1)
    #print("hint 2", hint)
    occurlist = findOccurrences(word, word[hint])
    for i in occurlist:
        crypword = crypword[:i] + word[hint] + crypword[i+1:]

    print(crypword)
    

    while gamerunning:
        inputchar = input()[0]
        if word.find(inputchar) != -1:
            occurlist = findOccurrences(word, inputchar)
            for i in occurlist:
                crypword = crypword[:i] + inputchar + crypword[i+1:]
            print(crypword)

            if crypword.find('*') == -1:
                print("You win! The word was: " + word)
                gamerunning = False

        else:
            hitpoints -= 1
            triedlist += inputchar
            print(f"Wrong! {hitpoints} tries left, you tried:", triedlist)
            print(crypword)

            if hitpoints <= 0:
                gamerunning = False
                print("Sorry, you lose. The word was: ", word)
