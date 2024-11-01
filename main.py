def linearize(book):
    chet = book.replace(" ", "")

def wordCount(book):
    words = book.split()
    wordCount = 0
    for word in words:
        wordCount += 1
    return wordCount

def letterCount(book):
    lower_case_book = book.lower()
    linearized_book = lower_case_book.replace(" ", "")
    alphabetCount = {}
    for letter in range(len(linearized_book)):
        print(alphabetCount[letter])
        if (ord(linearized_book[letter]) >= 97 or ord(linearized_book[letter]) <= 122):
            alphabetCount[linearized_book[letter]] += 1
            print(alphabetCount[letter])
        

def main():
    with open("books/frankenstein.txt") as frank:
        file_contents = frank.read()
        print(wordCount(file_contents))
        letterCount(file_contents)


main()