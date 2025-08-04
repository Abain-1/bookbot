from stats import get_word_count

def main():

    def get_book_text(path_to_file):
        with open(path_to_file) as f:
            file_contents = f.read()

        return(file_contents)


   

    #get_book_text("./books/frankenstein.txt")
        
    get_word_count(get_book_text("./books/frankenstein.txt"))



main()

