class Parent():
    def altered(self):
        print("Parent altered()")


class Child(Parent):
    def altered(self):
        print("Chird, before Parent altered()")
        super(Child, self).altered()
        print("Chold, after Parent altered()")


dad = Parent()
son = Child()

dad.altered()
son.altered()
