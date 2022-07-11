import pandas as pd
class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})

    def add_book(self, book_name, rating):
        for i in range(len(self.book_list)):
            if self.book_list.iloc[i][0] == book_name:
                return False
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)

    def has_read(self, book_name):
        for i in range(len(self.book_list)):
            if self.book_list.iloc[i][0] == book_name:
                return True
    
    def num_books_read(self):
        self.num_books = len(self.book_list)
        return self.num_books

    def fav_books(self):
        lst = [self.book_list.iloc[i][0] for i in range(len(self.book_list)) if self.book_list.iloc[i][1]>3]
        return lst