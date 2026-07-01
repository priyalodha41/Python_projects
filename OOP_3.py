# Library Management System

class Book:
    next_book_id=101
    def __init__(self,title,author):
        self.book_id=Book.next_book_id;
        Book.next_book_id+=1;
        self.title=title;
        self.author=author;
        self.available=True;
    
    def displayDetails(self):
        print(f"BOOK ID : {self.book_id}");
        print(f"Title : {self.title}");
        print(f"Author : {self.author}");
        if self.available == True:
            print(f"Available : Yes");
        else:
            print(f"Not Available : No");

class Member:
    next_member_id=101;
    def __init__(self,name):
        self.member_id=Member.next_member_id;
        Member.next_member_id+=1;
        self.name=name;
        self.borrowed_books=[];
    
    def displayDetails(self):
        print(f"Member ID : {self.member_id}");
        print(f"Name : {self.name}");
        print(f"Borrowed Books: {self.borrowed_books}");


class Library:
    
    def __init__(self):
        self.books=[];
        self.members=[];
    
    def add_book(self,book):
        self.books.append(book);
    
    def register_member(self,member):
        self.members.append(member);
        
    def display_all_books(self):
        for book in self.books:
            book.displayDetails();
    def display_all_members(self):
        for member in self.members:
            member.displayDetails();
            
    def search_book(self,title):
        for book in self.books:
            if(book.title==title):
                print("-------Book Found------");
                book.displayDetails();
                break;
        else:
            print("-----Book not found-----");
    
    def search_member(self,name):
        for member in self.members:
            if(member.name==name):
                print("-------Member Found------");
                member.displayDetails();
                break;
        else:
            print("-----Member not found-----");
            
    def borrow_book(self, member_id, book_id):

        member = None
        book = None

        # Find Member
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        else:
            print("Member not found")
            return

        # Find Book
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break
        else:
            print("Book not found")
            return

        if book.available and len(member.borrowed_books)<=3:
            book.available = False
            member.borrowed_books.append(book.title)
            print(f"{book.title} borrowed successfully.")
        else:
            print("Book is already borrowed.")
            
    def return_book(self,member_id,book_id):
        member = None
        book = None
        
        # Find Member
        for m in self.members:
            if m.member_id == member_id:
                member = m
                break
        else:
            print("Member not found")
            return

        # Find Book
        for b in self.books:
            if b.book_id == book_id:
                book = b
                break
        else:
            print("Book not found")
            return

        if book.available==False:
            book.available = True
            member.borrowed_books.remove(book.title)
            print(f"{book.title} returned successfully.")
        else:
            print("Book is available in the library");
           
b1=Book("Python","Corey")         
b2=Book("Harry Potter","J.K Rowling")
m1=Member("Priya Lodha");
l1=Library();
l1.add_book(b1);
l1.add_book(b2);
l1.register_member(m1);
# l1.display_all_members();
# l1.display_all_books();
# l1.search_book("Python");
# l1.search_member("Priya Lodha")
l1.borrow_book(101,101)
l1.return_book(101,101);
l1.display_all_members()