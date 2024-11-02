
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

def printLetterCount(letterDictionary):
    for letter in letterDictionary:
        print(f"The letter '{letter}' was found {letterDictionary[letter]} times.")

def main():
    with open("books/frankenstein.txt") as frank:
        print("------- Beginning book report for Frankenstein -------")
        file_contents = frank.read()
        print(f"There are {wordCount(file_contents)} words in this book.")
        printLetterCount(letterCount(file_contents))
        print("------- End of book report for Frankenstein -------")


main()