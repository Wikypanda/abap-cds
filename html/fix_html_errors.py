import markdown
import os
import re

# Function to fix unclosed HTML tags
def fix_unclosed_tags(html_content):
    # List of self-closing tags
    self_closing_tags = ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']
    
    # Closing tags regex
    closing_tag_regex = re.compile(r'</?([a-zA-Z0-9]+)\b.*?>')
    
    for tag in self_closing_tags:
        html_content = re.sub(f'<{tag}[^>]*>', f'<{tag} />', html_content)
    
    # Find and close unclosed tags
    open_tags = []
    for match in closing_tag_regex.finditer(html_content):
        tag_name = match.group(1)
        if match.group(0).startswith('</'):
            if open_tags and open_tags[-1] == tag_name:
                open_tags.pop()
            else:
                continue
        else:
            open_tags.append(tag_name)
    
    for tag in reversed(open_tags):
        html_content += f'</{tag}>'
    return html_content

# Function to convert Markdown to HTML and fix errors
def convert_markdown_to_html(markdown_file, output_directory):
    # Read the Markdown content
    with open(markdown_file, 'r') as file:
        markdown_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)
    
    # Fix any unclosed tags
    html_content = fix_unclosed_tags(html_content)
    
    # Ensure proper HTML structure
    full_html = f'<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Converted HTML</title>\n</head>\n<body>\n{html_content}\n</body>\n</html>'
    
    # Write the output HTML file
    output_file = os.path.join(output_directory, 'output.html')
    with open(output_file, 'w') as file:
        file.write(full_html)
    
    print(f'Converted HTML saved to: {output_file}')

# Example usage
# convert_markdown_to_html('example.md', 'html')
