import os, pygame,sys
from collections import deque




def load_directory_files(root_dir):
    # Pygame init is required for image loading
    pygame.init()
    loaded_files = {}
    print(sys.path)
    queue = deque([root_dir])
    print(os.path.abspath(os.curdir))
    # File types
    image_exts = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}
    text_exts = {".txt"}
    font_exts = {".otf", ".ttf"}

    while queue:

        print('queue',queue)
        current = queue.popleft()
        # List directory contents
        print(current, 'current')
        '''if type(current)==dict:
            return loaded_files'''
        for entry in os.listdir(current):
            path = os.path.join(current, entry)

            # If it's a folder, enqueue it (BFS)
            if os.path.isdir(path):
                queue.append(path)
                continue

            # If it's a file, process it
            _, ext = os.path.splitext(entry)
            ext = ext.lower()

            # IMAGE FILES
            if ext in image_exts:
                try:
                    loaded_files[entry] = pygame.image.load(path)
                except Exception as e:
                    print(f"Error loading image {entry}: {e}")

            # TEXT FILES
            elif ext in text_exts:
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        loaded_files[entry] = f.read()
                except Exception as e:
                    print(f"Error reading text {entry}: {e}")

            # FONT FILES (saved as bytes unless you want pygame.font.Font)
            elif ext in font_exts:
                try:
                    with open(path, "rb") as f:
                        loaded_files[entry] = f.read()
                except Exception as e:
                    print(f"Error reading font {entry}: {e}")

    return loaded_files

'''print(load_directory_files(os.path.relpath('Data')))
Dict=load_directory_files(os.path.relpath('Data'))
print(Dict['GlacialIndifference-Regular.otf'])'''
