def printer(upcase, lowcase, puctmark, space):
    print("- " + str(upcase) + " upper letters")
    print("- " + str(lowcase) + " lower letters")
    print("- " + str(puctmark) + " punctuation marks")
    print("- " + str(space) + " spaces")


def text_analyzer(text):
    ' '.join(text)
    upcase = 0
    lowcase = 0
    punctmark = 0
    space = 0

    for it in str(text):
        if it.islower():
            lowcase += 1
        elif it.isupper():
            upcase += 1
        elif it == ',' or it == '.':
            punctmark += 1
        elif it.isspace():
            space += 1
    printer(upcase, lowcase, punctmark, space)

text_analyzer("Python 2.0, released 2000, introduced "
"features like List comprehensions and a garbage collection "
"system capable of collecting reference cycles.")