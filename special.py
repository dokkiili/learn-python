class Supper:
    def method(self):
        print("Hello SUpper ")

    def delegate(self):
        self.action()


class Extend(Supper):
    def method(self):
        print("Extends == ")
        Supper.method(self)


class Provide(Supper):
    def action(self):
        print("Implemented In Privide")


if __name__ == "__main__":
    a = Supper()
    a.method()
    b = Extend()
    b.method()
    c = Provide()
    c.action()
    c.delegate()
