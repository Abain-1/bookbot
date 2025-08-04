def main():

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()

        return(file_contents)


    def get_word_count(book_text):
        
        split_text = book_text.split(" ")

        count = 0

        for words in split_text:

            count +=1

        print(f"{count} words found in document")

    #get_book_text("./books/frankenstein.txt")
        
    get_word_count(get_book_text("./books/frankenstein.txt"))



main()

