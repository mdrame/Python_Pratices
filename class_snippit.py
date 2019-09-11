class person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def namee(self):
        #namee = "Mohammed"
        print(f"My name is {self.name}")


mohammed = person("Mohammed", 24)

print(mohammed.namee())
