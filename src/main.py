from email.mime import base
import os, sys, shutil
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs" # by default, GitHub Pages serves sites from the "docs" directory of branch main
dir_path_content = "./content"
template_path = "./template.html"

def main():
    base_path = "/"
    if sys.argv[0] != "src/main.py":
        print(sys.argv[0])
        base_path = sys.argv[0]
    
    print("Clearing files in public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Populating public directory with static files...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating pages...")
    generate_pages_recursive(base_path, dir_path_content, template_path, dir_path_public)

main()
