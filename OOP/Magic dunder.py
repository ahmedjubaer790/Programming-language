# Problem 7: Magic (Dunder) Methods

# Book class এর __init__(self, title, author, pages) থাকবে।
# __str__ return করবে: 'Title' by Author
# __repr__ return করবে: Book('Title', 'Author', pages)
# __eq__ দুটি book তখনই সমান ধরবে যখন title ও author দুটোই মিলবে।
# __len__ return করবে pages।

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    
    def __str__(self):
        return (f"{self.title} by {self.author}")

    def __repr__(self):
        return (f"Book({self.title},{self.author},{self.pages})")

    def __eq__(self,other):
        if not isinstance(other,Book):
            raise NotImplementedError ("Object are not same")
        return self.title==other.title and self.author==other.author
    def __len__(self):
        return self.pages


b1=Book("Python","Jubaer",300)
b2=Book("Python","Jubaer",500)

print(b1)
print(repr(b1))
print(b1==b2)
print(len(b1))
        