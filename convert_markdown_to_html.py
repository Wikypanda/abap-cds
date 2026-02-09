import os
import markdown
from bs4 import BeautifulSoup

# Create output directory if it doesn't exist
output_dir = 'html'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to fix common HTML errors
def fix_html(html):
    # Use BeautifulSoup to handle any unclosed tags and correct structure
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()

# Function to convert markdown files to html
def convert_markdown_to_html():
    html_files = []
    # Iterate over all markdown files in the current directory
    for filename in os.listdir('.'):  
        if filename.endswith('.md'):
            with open(filename, 'r', encoding='utf-8') as md:
                text = md.read()
                # Convert markdown to html
                html = markdown.markdown(text)
                # Fix common HTML errors
                html = fix_html(html)
                # Generate proper HTML5 structure
                complete_html = f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n    <meta charset='UTF-8'>\n    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n    <link rel='stylesheet' href='styles.css'>\n    <title>{filename[:-3]}</title>\n</head>\n<body>\n{html}\n</body>\n</html>"
                html_files.append((filename[:-3], complete_html))
                # Save to html directory
                with open(os.path.join(output_dir, f'{filename[:-3]}.html'), 'w', encoding='utf-8') as html_file:
                    html_file.write(complete_html)
                    print(f'Converted {filename} to HTML.')

    return html_files

# Function to create an index file
def create_index_file(html_files):
    index_content = '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Index of HTML Files</title>\n    <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n<h1>Index of HTML Files</h1>\n<ul>\n'
    for title, _ in html_files:
        index_content += f'    <li><a href="{title}.html">{title}</a></li>\n'
    index_content += '</ul>\n</body>\n</html>'

    # Save index file
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)
        print('Created index.html')

# Main execution
if __name__ == '__main__':
    html_files = convert_markdown_to_html()
    create_index_file(html_files)
