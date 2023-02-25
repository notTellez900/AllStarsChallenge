import os
from bs4 import BeautifulSoup

# Set the directory path containing the HTML files
directory = 'C:/Users/nicol/OneDrive/Desktop/ClassCentral/www.classcentral.com'

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        # Read the contents of the HTML file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            html = file.read()

        # Parse the HTML content and extract the text
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()

        # Save the extracted text into a new text file
        text_filename = os.path.splitext(filename)[0] + '.txt'
        with open(os.path.join(directory, text_filename), 'w', encoding='utf-8') as file:
            file.write(text)
