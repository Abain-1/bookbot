def get_word_count(book_text):
        
        split_text = book_text.split()

        count = len(split_text)

        print(f"{count} words found in the document")