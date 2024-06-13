import os
from datetime import datetime

def generate_index_html(dir_path):
    index_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Index of {path}</title>
        <link rel="stylesheet" type="text/css" href="{rel_path}style.css">
    </head>
    <body>
        <h1>Index of {path}</h1>
        [<a href="{parent_path}">Parent Directory</a>]
        <table>
            <tr>
                <th>Name</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """

    for root, dirs, files in os.walk(dir_path):
        rows = []
        for directory in dirs:
            rows.append(f'<tr><td><img src="https://cdn-icons-png.flaticon.com/512/716/716784.png" alt="Folder Icon" style="width:16px;height:16px;margin-right:8px;"><a href="{directory}/">{directory}/</a></td><td>-</td><td>{datetime.fromtimestamp(os.path.getmtime(os.path.join(root, directory))).strftime("%d.%m.%y, %H:%M:%S")}</td></tr>')
        for file in files:
            if not file.endswith('.html') and not file.endswith('.css'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%d.%m.%y, %H:%M:%S")
                rows.append(f'<tr><td><img src="https://cdn.icon-icons.com/icons2/2753/PNG/512/ext_file_generic_filetype_icon_176256.png" alt="File Icon" style="width:16px;height:16px;margin-right:8px;"><a href="{file}">{file}</a></td><td>{file_size} B</td><td>{file_mtime}</td></tr>')

        path = os.path.relpath(root, dir_path)
        depth = len(path.split(os.sep)) if path != '.' else 0
        rel_path = '../' * depth if depth > 0 else './'
        parent_path = '../' if depth > 0 else './'

        with open(os.path.join(root, 'index.html'), 'w') as f:
            f.write(index_content.format(path=path, rows='\n'.join(rows), rel_path=rel_path, parent_path=parent_path))

# Path to your Maven repository
generate_index_html('src')
