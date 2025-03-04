import os
import fnmatch

def generate_tree(startpath, prefix='', exclude_patterns=None):
    """Generates a tree-like diagram of the directory structure, excluding certain patterns."""
    if exclude_patterns is None:
        exclude_patterns = []

    contents = os.listdir(startpath)
    contents = [item for item in contents if not any(fnmatch.fnmatch(item, pattern) for pattern in exclude_patterns)]

    pointers = ['├── ' if i < len(contents) - 1 else '└── ' for i in range(len(contents))]
    paths = [os.path.join(startpath, content) for content in contents]

    tree_structure = ''
    for pointer, path, content in zip(pointers, paths, contents):
        tree_structure += prefix + pointer + content + '\n'
        if os.path.isdir(path):
            extension = '│   ' if pointer == '├── ' else '    '
            tree_structure += generate_tree(path, prefix + extension, exclude_patterns)
    return tree_structure

def save_tree_to_file(startpath, output_file, exclude_patterns=None):
    """Saves the directory tree structure to a .txt file, excluding certain patterns."""
    tree_structure = generate_tree(startpath, exclude_patterns=exclude_patterns)
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(tree_structure)

# Example usage
startpath = 'C:/Users/91959/Desktop/CODE/Alembic-Test'  # Replace with your project directory path
output_file = 'directory_tree.txt'
exclude_patterns = ['*.pyc', '__pycache__', '.git', 'venv']  # Add patterns to exclude
save_tree_to_file(startpath, output_file, exclude_patterns)

