class Aclass():
    def topstudent(student,name):
        print("the top student in a class is ",name)

    def minimon(self,name):
        print("the class minimon in a class is ",name)
    

class Bclass:
    def setname(student,name):
        student.platinum = name
    def topstudent(teacher):
        print("the top student in b class is ",teacher.platinum)
    def minimon(self):
        print("the class minimon in b class is ",self.platinum)
    def poorstudent(self,name):
        print("the poor student in b class is",name)
    

a = Aclass()
b = Bclass()

#a.setname("sun")
b.setname("moon")
a.topstudent("fafa")
a.minimon("star")
b.topstudent()
b.minimon()
b.poorstudent("sun")


