class Book:
    def __init__(self):
        # Step 1: সব property শুরুতে 0
        self.length = 0
        self.width = 0
        self.depth = 0

    # Step 2: Getter methods
    def getVolume(self):
        return self.length * self.width * self.depth

    def getWeight(self):
        return 2 * self.length + 3 * self.width + 4 * self.depth

    # Step 2: Setter method
    def setLengthWidthDepth(self, l, w, d):
        self.length = l
        self.width = w
        self.depth = d


# Step 3: দুটি Book object, সব property 0
book1 = Book()
book2 = Book()

# Step 4: মান আপডেট
book1.setLengthWidthDepth(2, 3, 4)
book2.setLengthWidthDepth(9, 8, 7)

# Step 5: Weight ও Volume দেখানো
print("Book 1 -> Weight:", book1.getWeight(), ", Volume:", book1.getVolume())
print("Book 2 -> Weight:", book2.getWeight(), ", Volume:", book2.getVolume())