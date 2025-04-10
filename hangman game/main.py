import random
def hang():
    print("welcome to the hangman game\nguess the word 1 letter at a time")

    words = ["iphone","macbook","laptop","screen","charger","lights"]
    elcetronics = random.choice(words)
    #print(elcetronics)
    dots = []
    for i in elcetronics:
        dots.append("-")
   
    print("word:" ," ".join(dots))
    let = input("enter a letter: ").lower()
    
hang()
