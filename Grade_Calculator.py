score =int (input("What is your Score?"))

grade = ""

def scores(score):
    while(score > 100 or score < 0 ):
        print("Invalid score")
        score = int(input("What is your Score?"))
        
    if score >= 90:
        grade = ("A")
    elif score >= 80:
        grade = ("B")
    elif score >= 70:
        grade = ("C")
    elif score >= 60:
        grade = ("D")
    elif score < 60 and score > 0:
        grade = ("F")
    return grade

print(scores(score))

    