def profitable_gamble(prob,prize,pay):
    if prob * prize > pay:
        print("True")
    else:
        print("False")

profitable_gamble(0.2, 50, 9)
profitable_gamble(0.9, 1, 2)
profitable_gamble(0.9, 3, 2)
