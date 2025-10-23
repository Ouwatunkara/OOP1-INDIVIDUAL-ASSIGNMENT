
books = {}
members = []

GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "Fantasy")

def _is_valid_genre(genre):
    return genre in GENRES


def _get_member_by_id(member_id):
    for member in members:
        if member['member_id'] == member_id:
            return member
    return None


def _get_book_available_copies(isbn):
    if isbn in books:
        return books[isbn]['total_copies']
    return 0


def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return False

    if not _is_valid_genre(genre):
        return False

    if not isinstance(total_copies, int) or total_copies < 0:
        return False  # Basic data validation

    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return True


def add_member(member_id, name, email):
    if _get_member_by_id(member_id):
        # member_id must be unique
        return False

    new_member = {
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    }
    members.append(new_member)
    return True


def search_books(query, by="title"):
    matching_books = []

    if by not in ("title", "author"):
        by = "title"

    lower_query = query.lower()

    for book_isbn, book_details in books.items():
        if lower_query in book_details.get(by, "").lower():
            matching_books.append(book_details.copy())

    return matching_books


def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return False

    if genre is not None and not _is_valid_genre(genre):
        return False

    book = books[isbn]

    if title is not None:
        book["title"] = title
    if author is not None:
        book["author"] = author
    if genre is not None:
        book["genre"] = genre
    if total_copies is not None and isinstance(total_copies, int) and total_copies >= 0:
        book["total_copies"] = total_copies

    return True


def update_member(member_id, name=None, email=None):
    member = _get_member_by_id(member_id)
    if member is None:
        return False

    if name is not None:
        member["name"] = name
    if email is not None:
        member["email"] = email

    return True  # [cite: 54]


def delete_book(isbn):
    if isbn not in books:
        return False

    # Check if any member currently has this book borrowed
    for member in members:
        if isbn in member['borrowed_books']:
            return False

    del books[isbn]
    return True  # [cite: 56, 57]


def delete_member(member_id):
    global members

    member = _get_member_by_id(member_id)
    if member is None:
        return False

    if member['borrowed_books']:
        return False

    members = [m for m in members if m['member_id'] != member_id]
    return True  # [cite: 58, 59]

def borrow_book(isbn, member_id):
    member = _get_member_by_id(member_id)
    if member is None:
        return False

    if isbn not in books:
        return False

    book = books[isbn]

    if book['total_copies'] <= 0:
        return False

    if len(member['borrowed_books']) >= 3:
        return False

    # Perform the loan:
    book['total_copies'] -= 1
    member['borrowed_books'].append(isbn)

    return True  #


def return_book(isbn, member_id):
    member = _get_member_by_id(member_id)
    if member is None:
        return False

    if isbn not in books:
        return False
    if isbn not in member['borrowed_books']:
        return False
    # Perform the return:
    books[isbn]['total_copies'] += 1
    member['borrowed_books'].remove(isbn)

    return True

