#flashcards.py
#created: 1/12/2017
#Peter wuz here

from random import randint
import codecs
import sys
UTF8Reader = codecs.getreader('utf8')
sys.stdin = UTF8Reader(sys.stdin)

def main () :
    print ("Welcome to flashcards!")
    print ("Would you like to make cards or play cards?")
    mode = input(">")
    print ("What is your filename?")
    filename = input(">")
    keyname = filename + "k"

    if (mode == "make") :
        make(filename,keyname)

    elif (mode == "play") :
        play(filename,keyname)

    else :
        print ("Invalid mode. Try again.")


def make (filename,keyname) :
    print ("Time to make some cards! Congrats on learning new things!")
    rus_word = ''
    while (rus_word != "Goodbye.") :
        print ("Please enter Russian word.")
        rus_word = input('>')
        print ("Please define in English.")
        eng_word = input(">")
        print ("Is that correct? ",rus_word,eng_word)
        correct = input(">")
        
        if correct[0] == 'y':
            doc = open(filename,'a', encoding='utf8')
            key = open(keyname,'a', encoding='utf8')
            doc.write(rus_word)
            doc.write('\n')
            key.write(eng_word)
            key.write('\n')
            print ("Card created.\n")
            key.close() 
            doc.close()
        else:
            print("That one didn't make it.\n")

        
def play (filename,keyname) :
    doc = open(filename, encoding='utf8')
    key = open(keyname, encoding='utf8')
    doclines = doc.readlines()
    keylines = key.readlines()
    attempt = ""
    print ("English or Russian?")
    side = input(">")
    print ("Happy learning!")
    print ("s for show, n for next.")

    while attempt != "Goodbye." :
        rand = randint(0,len(doclines) - 1)
        rus_word = doclines[rand]
        eng_word = keylines[rand]
        
        if side.lower() == "russian" :
            print('слово: ',rus_word,)
        elif side.lower() == "english" :
            print("word: ",eng_word,)
            
        incorrect = True
            
        while incorrect:
            attempt = input('>')
                
            if (attempt == eng_word.strip() or attempt == rus_word.strip()
                    or attempt == "n") :
                print ("Gucci golden!\n")
                incorrect = False
            elif attempt == "s" :
                print (rus_word," ",eng_word,)
            else :
                print ("Nope. Try again.",)
    
    print("Have a lovely day ^.^")
    doc.close()
    key.close()
main()
