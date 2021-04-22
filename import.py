import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

uri = os.getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

engine = create_engine(uri)
db = scoped_session(sessionmaker(bind=engine))

def main():
    books = open('books.csv')
    reader = csv.reader(books)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
        {"isbn":isbn, "title":title, "author":author, "year":year})
    db.commit()
    print("Files added")

if __name__ == '__main__':
    main()
