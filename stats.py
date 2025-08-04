def get_word_count(book_text):
        
        split_text = book_text.split()

        count = len(split_text)

        print(f"{count} words found in the document")

def get_char_count(book_text):

       letters = {}

       lower_case = book_text.lower()

       for i in lower_case:
            if i not in letters:
                letters[i] = 1
            else:
                  letters[i] += 1
        
       print(letters)

