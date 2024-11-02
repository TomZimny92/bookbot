
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
    for i in range(len(linearized_book)):
        letter = linearized_book[i]
        if (ord(letter) >= 97 and ord(letter) <= 122):
            if (letter not in alphabetCount):
                alphabetCount[letter] = 1
            else:
                alphabetCount[letter] += 1
    return alphabetCount

def main():
    with open("books/frankenstein.txt") as frank:
        file_contents = frank.read()
        print(wordCount(file_contents))
        print(letterCount(file_contents))


main()