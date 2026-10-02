# WORD FREQUENCY COUNTER
This algorithm counts characters distinct of spaces and break lines, and words with their frequency, in a text file.

## How to run this project
1) Open google colab in your browser. You have to acces with a google account.
2) Click on New Notebook
3) Copy and paste the script in words.py
4) Download texto.txt and then added to the files in google colab
5) Run the script

The screen should be like this:
<img width="1617" height="812" alt="image" src="https://github.com/user-attachments/assets/450dc628-175f-4520-a397-e0480f8b6b75" />

## Computational complexity:

If *n* is the number of characters, it takes *n* steps to count the characters and words and to use the `addWord` function.

For each word formed (the number of which does not exceed the number of characters), the `addWord` function is executed; this function iterates through the words already stored (at most *n*) and, at most, uses the `remove` and `append` or `insert` functions. Since `remove` and `insert` have O(*n*) complexity and `append` is O(*n*), we have O(*n*) complexity for each character. Consequently, the Computational complexity of the script is O(*n*²).
