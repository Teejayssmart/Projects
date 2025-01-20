score = input("Enter a score between 0.1 and 1.0: ")
try:
    scores = float(score)
except ValueError:
    print("Bad Score")
    quit()
else:


    if scores >= 0.0 and scores <= 1.0:
        if scores >= 0.9:
            print("A")
        elif scores >= 0.8:
            print("B")
        elif scores >= 0.7:
            print("C")
        elif scores >= 0.6:
            print("D")
        else:
            print("F")
    else:
        print("Bad score")

