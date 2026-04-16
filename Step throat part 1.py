def find_prob(a,b):

    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_bga = 0.085
        elif b == 2:
            prob_bga = 0.15
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of B given A: ", prob_bga)
        print("Probability of both the events occurring: ", prob_a_and_b)

    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_bga = 0.02
        elif b == 2:
            prob_bga = 0.98
        else:
            print("Invalid Choice")
        prob_a_and_b = prob_a * prob_bga
        print("Probability of B given A: ", prob_bga)
        print("Probability of both the events occurring: ", prob_a_and_b)
    
    else:
        print("Invalid Choice")

print("Let's calculate the probability. Please enter choices for the events.....")

print("Person has step throat: \n1. Yes \n2. No")
a = int(input("Enter your choice for event A: "))

print("Person has tested positive? : \n1. Yes \n2. No")
b = int(input("Enter your choice for event B: "))

print("Probabilities for event A and B are :-")
find_prob(a, b)