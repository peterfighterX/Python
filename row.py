Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> firstRow = 1
>>> lastRow = 31
>>> currentRow = firstRow
>>> while (currentRow <= lastRow)
SyntaxError: expected ':'
>>> while(currentRow <= lastRow):
...     print("Row number...")
...     currentRow+=1
