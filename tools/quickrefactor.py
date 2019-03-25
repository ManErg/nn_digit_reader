"""
Change instances of text for every file in a directory to a different text

The intended use is to expedite reorganizing files i.e. '../text.txt' -> 'text'
"""
import os
import sys
    

def switchText(original, newText, fileName):
    """Change all instances of original text to new text in a given file"""
    result = ""
    #Read file into string
    with open(fileName) as f:
        oldFile = f.read()
    #Copy char for char; check for instances of original text and replace if true
    for char in oldFile:
        result += char
        if original in result[-len(original):]:
            result = result[: len(result) - len(original)] #Truncate instance
            result += newText #Append new text
    #Write out to same file name
    with open(fileName, 'w') as newFile:
        newFile.write(result)
    return


if __name__ == '__main__':
    for fileName in os.listdir(os.getcwd() ):
        switchText(sys.argv[1], sys.argv[2], fileName)
