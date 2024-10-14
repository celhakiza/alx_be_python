
class Book:
    # Constructor: Initializes the attributes
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Destructor: Prints message when the object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # String representation: User-friendly display
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # Official representation: For recreating the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"