class Outer:
    def __init__(self):
        self.name="Outer Class"

    class inner:
        def __init__(self):
            self.name="Inner Class"

        def display(self):
            print('Inner Class')

outer=Outer()
print(outer.name)
inner=Outer.inner()
inner.display()
print(inner.name)