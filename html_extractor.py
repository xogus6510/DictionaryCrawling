from bs4 import BeautifulSoup
import re

html = """
<html>
    <head>
        <title>Example HTML Document</title>
    </head>
    <body>
        <p>This is an example HTML document.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

text = " ".join(word for word in soup.stripped_strings)

# Eliminate duplicates and convert to a list of words
words = list(set(text.split()))


def custom_sort(word):
    if re.match(r'[\uac00-\ud7a3]+', word):
        return 0
    elif re.match(r'[a-zA-Z]+', word):
        return 1
    elif re.match(r'\d+', word):
        return 2
    else:
        return 3


# Sort words based on custom_sort
words.sort(key=custom_sort)

# Print words line by line
for word in words:
    print(word)
