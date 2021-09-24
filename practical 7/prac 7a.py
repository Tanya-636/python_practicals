class student:
    def init(self,name, sex,course,result):
        self.name=name
        self.sex=sex
        self.course=course
        self.result=result
    def display(self, name, sex, course, result):
        self.name=name
        self.sex=sex
        self.course=course
        self.result=result
        print ('Name:', name)
        print ('Sex:',sex)
        print ('course:',course)
        print ('result:', result)
