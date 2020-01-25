score = input("Enter Score: ")
try:
    score = float(score)
    if score >1.0:
        print("Please enter a number between 0.0 and 1.0")
    elif score >= 0.9:
        print("A")
    elif score >=0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >=0.6:
        print("D")
    elif score < 0.6 and score >= 0.0:
        print("F")
except Exception as e:
    print("Enter a number.")
