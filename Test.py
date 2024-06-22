# Nhap du lieu tuy chon
noun = str(input("Noun: "))
verb = str(input("Verb: "))
adjective = str(input("Adjective: "))
verb2 = str(input("Verb: "))

# Khai bao lop ten madlibs
class madlibs():
    def first_method():
        madlib = f"Learning to {verb} is very {adjective}. {noun} can be difficult, so you need to {verb2} hard."
        print(madlib)
# Phuong thuc thu nhat tao mot chuoi matlib su dung f-string chen cac bien trong dau ngoac nhon {} va in ra        

    def second_method():
        madlib2 = (" Learning to " +   verb)
        print(madlib2)
# Phuong thuc thu hai tao mot chuoi don gian bang viec noi chuoi voi bien         
        
    def third_method():
        madlib3 =  "Learning to {} is very {}. {} can be difficult, so you need to {} hard.".format(verb,adjective,noun,verb2)
        print(madlib3)
# Phuong thuc thu ba su dung format() de chen cac bien vao chuoi        
        

call_class = madlibs()
madlibs.first_method()
madlibs.second_method()
madlibs.third_method()