import os
import markdown

# Function to convert Markdown to HTML
def convert_markdown_to_html(md_file_path, html_file_path):
    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Create html folder if not exists
    os.makedirs(os.path.dirname(html_file_path), exist_ok=True)

    # Write the HTML file
    with open(html_file_path, 'w', encoding='utf-8') as html_file:
        html_file.write('<!DOCTYPE html>\n')
        html_file.write('<html lang="en">\n')
        html_file.write('<head>\n')
        html_file.write('    <meta charset="UTF-8">\n')
        html_file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
        html_file.write('    <title>Converted Markdown</title>\n')
        html_file.write('</head>\n')
        html_file.write('<body>\n')
        html_file.write(html_content)
        html_file.write('\n</body>\n')
        html_file.write('</html>\n')

# Main function to process files in the markdown directory
if __name__ == '__main__':
    markdown_dir = './'  # Change this to your markdown directory path
    html_dir = 'html/'  # The output directory for html files

    # Iterate over all files in the markdown directory
    for filename in os.listdir(markdown_dir):
        if filename.endswith('.md'):
            md_file_path = os.path.join(markdown_dir, filename)
            html_file_path = os.path.join(html_dir, filename.replace('.md', '.html'))
            convert_markdown_to_html(md_file_path, html_file_path)

    print('Markdown files have been converted to HTML successfully.');