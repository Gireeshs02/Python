import os

def visualize_directory_tree(start_path, prefix=''):
    if not os.path.exists(start_path):
        print(f"Error: The path '{start_path}' does not exist.")
        return
    base_name = os.path.basename(start_path)
    print(f"{prefix}├── {base_name}")

    if os.path.isdir(start_path):
        try:
            items = sorted(os.listdir(start_path))
        except PermissionError:
            print(f"{prefix}│   └── [Permission Denied]")
            return
        
        for i, item in enumerate(items):
            path = os.path.join(start_path, item)
            is_last = (i == len(items) - 1)

            current_prefix = "│   " if not is_last else "    "

            if os.path.isdir(path):
                visualize_directory_tree(path, prefix + current_prefix)
            else:
                print(f"{prefix}{current_prefix}└── {item}")

if __name__ == "__main__":
    target_path = "."
    visualize_directory_tree(target_path)