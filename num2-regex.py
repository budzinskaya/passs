import re

def process_paths(paths):
    pattern = re.compile(r'(?m)' +
                         r'^([\\/]?(?:[^\\/:*?\"<>|\r\n]+[\\/])*)' +
                         r'(\.?(?:[^\\/:*?\"<>|\r\n\.]|\.(?=.*\.))+)' +
                         r'(?!\.bat(?:$|\n))(?!\.txt(?:$|\n))' +
                         r'(\.[^\\/:*?\"<>|\r\n\.]+)?$')
    return re.findall(pattern, paths)

paths = '''
file.txt
file.txts
\\dir\\file.bat
\\dir\\file.bats
/dir/dir/file.py
dir\\file.py
dir\\file.before.py
.file
/dir/.file
file.py
/file.py
/file.py/file.py
dir1/file 1.7z
'''

expected_results = [
    ('', 'file', '.txts'),
    ('\\dir\\', 'file', '.bats'),
    ('/dir/dir/', 'file', '.py'),
    ('dir\\', 'file', '.py'),
    ('dir\\', 'file.before', '.py'),
    ('', '.file', ''),
    ('/dir/', '.file', ''),
    ('', 'file', '.py'),
    ('/', 'file', '.py'),
    ('/file.py/', 'file', '.py'),
    ('dir1/', 'file 1', '.7z'),
]

actual_results = process_paths(paths)

assert(actual_results == expected_results)
