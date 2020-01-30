from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_book(bookname, author, pages, description, image):
	"""
	Add a student to the database, given
	their name, year, and whether they have
	finished the lab.
	"""
	book_object = Book(
		bookname=bookname,
		author=author,
		pages=pages,
		description= description,
		image=image)
	session.add(book_object)
	session.commit()

def query_by_name(bookname):
	"""
	Find the first student in the database,
	by their name
	"""
	book = session.query(Book).filter_by(
		bookname=bookname).first()
	return book

def query_all():
	"""
	Print all the students in the database.
	"""
	books = session.query(Book).all()
	for book in books:
		print(books)
		print('\n')
	return books

def delete_by_name(bookname):
	session.query(Book).filter_by(
		bookname=bookname).delete()
	session.commit()


def query_by_id(book_id):
    books = session.query(Book).filter_by(
        book_id=book_id).first()
    return books
