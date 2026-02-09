import markdown
import os

def convert_markdown_to_html(markdown_file):
    # Read the markdown content from the file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Convert markdown to HTML
    html = markdown.markdown(text)
    
    # Construct the output filename
    html_file = os.path.splitext(markdown_file)[0] + '.html'
    
    # Write the HTML content to a new file
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html)
    
    print(f'Converted {markdown_file} to {html_file}')

# Example usage: convert_markdown_to_html('example.md')