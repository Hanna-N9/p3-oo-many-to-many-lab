class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
       
    #This method should return a list of related contracts 
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    #This method should return a list of related books using the Contract class as an intermediary
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    #This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    #This method should return the total amount of royalties that the author has earned from all of their contracts
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])
        
        
        
  
        
class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    #This method should return a list of related contracts 
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    #This method should return a list of related authors using the Contract class as an intermediary
    def authors(self):
        return [contract.author for contract in self.contracts()]





class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        
# The author property should be an instance of the Author class, while the book property should be an instance of the Book class. The date property should be a string that represents the date when the contract was signed, while the royalties property should be a number that represents the percentage of royalties that the author will receive for the book.
# All setters should raise Exception upon failure.  

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Author must be an instance of the Author class.")
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception("Book must be an instance of the Book class.")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception("Date must be a string.")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception("Royalties must be a string.")
        
    #This method should return all contracts that have the same date as the date passed into the method.
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
       