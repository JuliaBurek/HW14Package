import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    reader = BookLover('Julia Burek', 'juliab@gmail.com', 'romance')
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        self.reader.add_book('We Were Liars', 4)
        actual1 = ('We Were Liars', 4)
        self.assertTrue(actual1, self.reader.book_list)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        actual2 = self.reader.add_book('We Were Liars', 4)
        self.assertFalse(actual2)
    
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        self.reader.add_book('Little Women', 5)
        actual3 = self.reader.has_read('Little Women')
        self.assertTrue(actual3)

    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        actual4 = self.reader.has_read('The Great Gatsby')
        self.assertFalse(actual4)

    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        self.reader.add_book('The Song of Achilles', 3)
        self.reader.add_book('Pride and Prejudice', 4)
        self.reader.add_book('Little Fires Everywhere', 2)
        actual5 = self.reader.num_books_read()
        expected = 5
        self.assertEqual(actual5, expected)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        # self.reader.add_book('The Song of Achilles', 3)
       # self.reader.add_book('Pride and Prejudice', 4)
        self.reader.add_book('Little Fires Everywhere', 2)
        self.reader.add_book('Moby Dick', 5)
        actual6 = self.reader.fav_books()
        expected = ['We Were Liars', 'Little Women', 'Pride and Prejudice', 'Moby Dick']
        self.assertEqual(actual6, expected)



if __name__ == '__main__':
    unittest.main(verbosity=3)