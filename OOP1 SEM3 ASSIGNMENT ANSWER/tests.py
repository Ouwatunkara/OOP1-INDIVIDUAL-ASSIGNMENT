import operations
import sys
def reset_system_state():
    operations.books.clear()
    operations.members.clear()

reset_system_state()
print("--- Running Test Group 1: Book CRUD ---")

assert operations.add_book("111", "Python Mastery", "A. Coder", "Sci-Fi", 5) == True, \
    "Test 1.1 Failed: Failed to add a valid book."  # [cite: 85]

assert operations.add_book("111", "Duplicate Book", "B. Author", "Fiction", 1) == False, \
    "Test 1.2 Failed: Added book with duplicate ISBN."

assert operations.add_book("222", "Invalid Genre Book", "C. Writer", "Horror", 2) == False, \
    "Test 1.3 Failed: Added book with invalid genre."

results = operations.search_books("python", by="title")
assert len(results) == 1 and results[0]['author'] == "A. Coder", \
    "Test 1.4 Failed: Search by title failed."  # [cite: 85]

assert operations.update_book("111", genre="Fiction", total_copies=6) == True, \
    "Test 1.5 Failed: Failed to update book genre and copies."

assert operations.books.get("111", {}).get("genre") == "Fiction", \
    "Test 1.6 Failed: Book update verification failed."

print("Test Group 1 Passed.")

reset_system_state()
print("\n--- Running Test Group 2: Member CRUD ---")

# Add Member (Success)
assert operations.add_member("M001", "Alice", "alice@test.com") == True, \
    "Test 2.1 Failed: Failed to add a valid member."  # [cite: 85]

assert operations.add_member("M001", "Bob", "bob@test.com") == False, \
    "Test 2.2 Failed: Added member with duplicate ID."

assert operations.update_member("M001", email="new.alice@test.com") == True, \
    "Test 2.3 Failed: Failed to update member email."

member_found = operations._get_member_by_id("M001")
assert member_found is not None and member_found['email'] == "new.alice@test.com", \
    "Test 2.4 Failed: Member update verification failed."

assert operations.delete_member("M001") == True, \
    "Test 2.5 Failed: Failed to delete member with no borrowed books."

assert operations.delete_member("M002") == False, \
    "Test 2.6 Failed: Deleted non-existent member."

print("Test Group 2 Passed.")
reset_system_state()
print("\n--- Running Test Group 3: Borrow/Return & Edge Cases ---")

operations.add_book("333", "Book A", "D. Author", "Fiction", 2)
operations.add_book("444", "Book B", "E. Writer", "Non-Fiction", 0)  # Zero copies
operations.add_member("M002", "Charlie", "charlie@test.com")

assert operations.borrow_book("333", "M002") == True, \
    "Test 3.1 Failed: Failed to borrow available book."

assert operations.books['333']['total_copies'] == 1, \
    "Test 3.2 Failed: Book copies not decremented after borrow."
member_c = operations._get_member_by_id("M002")
assert "333" in member_c['borrowed_books'], \
    "Test 3.3 Failed: ISBN not added to member's list."

assert operations.borrow_book("444", "M002") == False, \
    "Test 3.4 Failed: Borrowed book with total_copies == 0."  # [cite: 86]

operations.add_book("555", "Book C", "F. Author", "Sci-Fi", 1)
operations.add_book("666", "Book D", "G. Writer", "Fiction", 1)
operations.add_book("777", "Book E", "H. Author", "Non-Fiction", 1)
operations.borrow_book("555", "M002")  # 2nd book
operations.borrow_book("666", "M002")  # 3rd book

assert operations.borrow_book("777", "M002") == False, \
    "Test 3.5 Failed: Exceeded 3-loan limit."  # [cite: 87]

assert operations.return_book("333", "M002") == True, \
    "Test 3.6 Failed: Failed to return a borrowed book."

assert operations.books['333']['total_copies'] == 2, \
    "Test 3.7 Failed: Book copies not incremented after return."
assert "333" not in member_c['borrowed_books'], \
    "Test 3.8 Failed: ISBN not removed from member's list."

assert operations.return_book("777", "M002") == False, \
    "Test 3.9 Failed: Returned a book the member never borrowed."

assert operations.delete_member("M002") == False, \
    "Test 3.10 Failed: Deleted member with borrowed books."

print("Test Group 3 Passed.")

operations.add_book("888", "Borrowed Book", "J. Author", "Fiction", 1)
operations.add_member("M003", "David", "david@test.com")
operations.borrow_book("888", "M003")
assert operations.delete_book("888") == False, \
    "Test 3.11 Failed: Deleted a book that is currently borrowed."

print("\nAll required unit tests completed successfully.")