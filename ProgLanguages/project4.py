''''
Jacob Esswein
Professor Galina
Completed 11/3/2019

This program has a 'Product' class and two child classes 'Book' and 'Movie'
that inherit 'Product''s constructor and in that, its private variables name,
price and discount percent.
'''

# Parent class 'Product'
class Product:
    name = ""
    price = 0
    discountPercent = 0

    #Contstructor
    def __init__(self, name, price, discountPercent):
        # All variables are private
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent
    
    # Calculate discount amount
    def getDiscountAmount(self):
        return self.__price * self.__discountPercent
    
    #Calculate discount price
    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()

    #Print description / details
    def printDescription(self):
        return "Name is: " + self.__name + " price is: " + str(self.__price) + " discount is: " + str(self.__discountPercent) + " discount amount is: " + str(self.getDiscountAmount()) + " discount price is " + str(self.getDiscountPrice())

# Polymorphed class 'Book' of 'Product' takes class 'Product' as a variable
class Book(Product):
    def __init__(self, author, name, price, discountPercent):
        self.__author = author
        # Polymorphed class's constructor 'calls' the 'Product' classes constructor
        Product.__init__(self, name, price, discountPercent)
    
    # Polymorphed printDescription
    def printDescription(self):
        return "Author is: " + self.__author + Product.printDescription(self)
        
class Movie(Product):
    def __init__(self, year, name, price, discountPercent):
        self.__year = year
        Product.__init__(self, name, price, discountPercent)
    
    def printDescription(self):
        return "Year is " + self.__year + Product.printDescription(self)

def main():
    #Create objects and give their values
    product = Product("product", 10, 0.9)
    book = Book("Jacob Esswein ", "Best Book", 10, 0.1)
    movie = Movie("1994 ", "Pulp Fiction", 22, 0.3)

    # Output their descriptions / details
    print(product.printDescription())
    print(book.printDescription())
    print(movie.printDescription())

main()
