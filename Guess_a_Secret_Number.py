import random

def main():
    secret = random.randint (1,100)

    while True:
        guess = int(raw_input("Guess the secret number between 1 and 100: "))

        if guess == secret:
            print "Congratulations! It's number %s" % secret
            break
        elif guess > secret:
            print "Try a lower number!"
        elif guess < secret:
            print "Try a higher number!"

if __name__ == "__main__":
    main()



guess = None

currentTry = 1

while guess != secret and currentTry <= maxTries:

    print "What's the secret number?"
    print "Current Try", currentTry

    entry = raw_input()
    guess = int(entry)


    if guess == secret:
        print "Jackpot, you did it!"
    else:
        currentTry += 1
        print "Nope, give it another try! ", secret

if guess != secret:
    print "Sorry, too many tries."