secret = 7
guess = raw_input("Insert the number you think is secret:")

if secret == guess:
    print "Great you insert correct number"
elif secret != guess:
    print "Sorry wrong number"