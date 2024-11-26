#Problem 2
# Dictionary to store book titles as keys and their total borrowed days as values

def library_analysis(borrowed_list):
    borrowed_books = {}

    for entry in borrowed_list:
        title, days = entry.split('-')
        title = title.strip()
        days = int(days.strip())
        if title in borrowed_books:
            borrowed_books[title] += days
        else:
            borrowed_books[title] = days

    most_borrowed = max(borrowed_books, key=borrowed_books.get)
    least_borrowed = min(borrowed_books, key=borrowed_books.get)

    total_days = sum(borrowed_books.values())
    total_books = len(borrowed_books)
    average_days = total_days / total_books

    unique_titles = set(borrowed_books.keys())

    sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)
    
    print("Most borrowed book:", most_borrowed, "with", borrowed_books[most_borrowed], "days")
    print("Least borrowed book:", least_borrowed, "with", borrowed_books[least_borrowed], "days")
    print("Average borrowing time:", round(average_days, 2), "days")
    print("Unique book titles:", unique_titles)
    print("Books sorted by borrowed days:")
    for book, days in sorted_books:
        print(f"{book}: {days} days")

borrowed_books_list = [
    "Book A - 19",
    "Book B - 23",
    "Book C - 52",
    "Book A - 24",
    "Book B - 22",
    "Book D - 25"
]

library_analysis(borrowed_books_list)
