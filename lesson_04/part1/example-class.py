class Example:
    def __init__(self, name, version="1"):
        self.name = name
        self.version = version

    def show(self):
        # print(self.name + " " + self.version)
        print("{} {}".format(self.name, self.version))


example1 = Example("Example 1")
example1.show()
example2 = Example("Example 2")
example2.show()
