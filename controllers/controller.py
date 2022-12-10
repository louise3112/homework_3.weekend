from flask import render_template, request, redirect
from app import app
from models.book_list import *


@app.route('/library')
def index():
    return render_template('index.html', title = "CodeClan Library", books_html = all_books)

@app.route('/library', methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    add_book(title, author, genre)
    return redirect('/library')

@app.route('/library/<list_index>')
def book_page(list_index):
    page_title = all_books[int(list_index)].title
    return render_template('book.html', title = page_title, book_info = all_books[int(list_index)])

@app.route('/library/delete/<list_index>', methods=['POST'])
def delete(list_index):
    delete_book(all_books, int(list_index))
    return redirect('/library')

@app.route('/library/check-out/<list_index>', methods=['POST'])
def check_out(list_index):
    update_book_status(all_books, int(list_index), True)
    return redirect('/library')

@app.route('/library/check-in/<list_index>', methods=['POST'])
def check_in(list_index):
    update_book_status(all_books, int(list_index), False)
    return redirect('/library')
