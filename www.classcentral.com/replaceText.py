import os

# Set the directory path containing the HTML and text files
directory = 'C:/Users/nicol/OneDrive/Desktop/ClassCentral/www.classcentral.com'

# Loop through all the files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        # Read the contents of the text file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            text = file.read()

        # Replace the content of the corresponding HTML file with the text
        html_filename = os.path.splitext(filename)[0] + '.html'
        with open(os.path.join(directory, html_filename), 'r+', encoding='utf-8') as file:
            html = file.read()
            file.seek(0)
            file.write(html.replace('<body>' + text + '</body>', '<body>' + 'REPLACED TEXT' + '</body>'))
            file.truncate()
