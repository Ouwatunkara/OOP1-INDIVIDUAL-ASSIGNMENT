import operations
import pprint  # For clean output of dictionaries/lists


def print_state(message):
    """Prints the current state of books and members with a header."""
    print("\n" + "=" * 50)
    print(f"SYSTEM STATE AFTER: {message}")
    print("=" * 50)
    print("--- BOOKS (ISBN: Details) ---")
    pprint.pprint(operations.books)
    print("\n--- MEMBERS (List of Dicts) ---")
    pprint.pprint(operations.members)
    print("=" * 50 + "\n")


def run_demo():
    """Runs the sequential demonstration scenario."""
    print("--- MINI LIBRARY MANAGEMENT SYSTEM DEMO ---")

    print(f"Valid Genres: {operations.GENRES}")

    print("\n--- Setup: Adding 5 Books ---")
    operations.add_book("978-0134041697", "Clean Code", "Robert C. Martin", "Non-Fiction", 3)
    operations.add_book("978-1491957223", "Fluent Python", "Luciano Ramalho", "Sci-Fi", 2)
    operations.add_book("978-0596520687", "The Mythical Man-Month", "Frederick Brooks", "Non-Fiction", 1)
    operations.add_book("978-0321765723", "Design Patterns", "Erich Gamma", "Sci-Fi", 4)
    operations.add_book("978-0743273565", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5)
    print_state("Initial 5 Books Added")

    print("\n--- Setup: Adding 3 Members ---")
    operations.add_member("M001", "Alice Smith", "alice@lib.com")
    operations.add_member("M002", "Bob Johnson", "bob@lib.com")
    operations.add_member("M003", "Charlie Day", "charlie@lib.com")
    print_state("Initial 3 Members Added")

    print("\n--- DEMO: Add New Book (Create) ---")
    success = operations.add_book("978-1593275990", "Python Crash Course", "Eric Matthes", "Non-Fiction", 1)
    print(f"Result of adding 'Python Crash Course': {success}")

    # 5. Search by Author (Read)
    print("\n--- DEMO: Search Books by Author (Read) ---")
    search_results = operations.search_books("Ramalho", by="author")
    print(f"Found {len(search_results)} book(s) by Ramalho:")
    pprint.pprint(search_results)

    print("\n--- DEMO: Update Member Email (Update) ---")
    success = operations.update_member("M002", email="bobby.j@lib.com")
    print(f"Result of updating M002 email: {success}")

    print("\n--- DEMO: Delete a Book (Delete) ---")
    # Delete 'The Mythical Man-Month' (ISBN: 978-0596520687) - should succeed as total_copies=1 (not borrowed)
    success = operations.delete_book("978-0596520687")
    print(f"Result of deleting 'The Mythical Man-Month': {success}")

    print_state("After CRUD Operations")

    print("\n--- DEMO: M001 borrows 'Clean Code' ---")
    success = operations.borrow_book("978-0134041697", "M001")
    print(f"Result: {success}")  # total_copies for Clean Code becomes 2

    print("\n--- DEMO: M003 attempts to borrow 'Fluent Python' (2 copies total) three times to test availability ---")
    operations.borrow_book("978-1491957223", "M003")  # Copy 1
    operations.borrow_book("978-1491957223", "M002")  # Copy 2

    unavailable_try = operations.borrow_book("978-1491957223", "M001")
    print(
        f"Result of M001's third attempt to borrow 'Fluent Python': {unavailable_try} (Expected False)")  # total_copies=0, should fail

    print("\n--- DEMO: M001 hits the 3-loan limit ---")
    operations.borrow_book("978-0321765723", "M001")  # Book 2
    operations.borrow_book("978-0743273565", "M001")  # Book 3

    limit_try = operations.borrow_book("978-1593275990", "M001")  # Book 4 (should fail)
    print(f"Result of M001 attempting to borrow 4th book: {limit_try} (Expected False)")

    print("\n--- DEMO: M001 returns 'Clean Code' ---")
    return_success = operations.return_book("978-0134041697", "M001")
    print(f"Result: {return_success}")  # total_copies for Clean Code becomes 3

    print("\n--- DEMO: Attempt to delete 'Fluent Python' (currently borrowed) ---")
    delete_borrowed_fail = operations.delete_book("978-1491957223")
    print(f"Result of deleting 'Fluent Python': {delete_borrowed_fail} (Expected False)")

    print_state("Final State After Borrow/Return Operations")


if __name__ == "__main__":
    run_demo()