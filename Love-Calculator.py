firstP = input("What is your name ? \t").upper()
secondP = input("What is their name ? \t").upper()

numberOfTrue = firstP.count("T") + firstP.count("R") + firstP.count("U") + firstP.count("E") \
               + secondP.count("T") + secondP.count("R") + secondP.count("U") + secondP.count("E")

numberOfLove = firstP.count("L") + firstP.count("O") + firstP.count("V") + firstP.count("E") \
               + secondP.count("L") + secondP.count("O") + secondP.count("V") + secondP.count("E")
score = int(str(numberOfTrue) + str(numberOfLove))

if score < 10 or score > 90:
    print("Your score is {}, you go together like coke and mentos."
          .format(score))
elif 40 < score < 50:
    print("Your score is {}, you are alright together."
          .format(score))
else :
    print("Your score is {}."
          .format(score))

