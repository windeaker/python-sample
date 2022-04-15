class Testclass(object):
    def __init__(self):
        print("student call construct function")
        self.name=None
        self.id='2222'
        self.__private_properties=None

    def print_name(self):
        print(self.name)

    def print_id(self):
        print(self.id)

    def print_private_properties(self):
        print(self.__private_properties)

testclass=Testclass()
testclass.print_id()
print(testclass.name)
testclass.print_private_properties()



