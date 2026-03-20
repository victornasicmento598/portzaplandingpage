
import re

file_path = 'index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if 'bg-canvas' in content:
    print('Canvas already exists.')
else:
    # Canvas element with z-index 1
    # We use single quotes for the string literal
    canvas_html = r'\1' + '\n    <canvas id=\u0022bg-canvas\u0022 style=\u0022position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none;\u0022></canvas>'
    
    # Use re.sub with regex
    new_content = re.sub(r'(<body[^>]*>)', canvas_html, content, count=1, flags=re.IGNORECASE)
    
    # Script
    script_html = '    <script src=\u0022bg-animation.js\u0022></script>\n</body>'
    new_content = new_content.replace('</body>', script_html)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('index.html updated successfully.')
