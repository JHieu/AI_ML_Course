noun = str(input("Noun: "))
verb = str(input("Verb: "))
adjective = str(input("Adjective: "))
verb2 = str(input("Verb: "))

class madlibs():
    def first_method():
        madlib = f"Learning to {verb} is very {adjective}. {noun} can be difficult, so you need to {verb2} hard."
        print(madlib)

    def second_method():
        madlib2 = (" Learning to " +   verb)
        print(madlib2)
        
    def third_method():
        madlib3 =  "Learning to {} is very {}. {} can be difficult, so you need to {} hard.".format(verb,adjective,noun,verb2)
        print(madlib3)

call_class = madlibs()
madlibs.first_method()
madlibs.second_method()
madlibs.third_method()