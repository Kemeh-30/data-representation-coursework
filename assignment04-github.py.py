# Importing Module
import os
from git import Repo
# replacing old file with new file
def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace(old_text, new_text)
    
    with open(file_path, 'w') as file:
        file.write(content)
# commit changes
def commit_and_push_changes(repo_path, file_path, commit_message):
    repo = Repo(repo_path)
    
    # Stage the changes
    repo.index.add([file_path])

    # Commit the changes
    repo.index.commit(commit_message)

    # Push the changes to the remote repository
    origin = repo.remote(name='origin')
    origin.push()

if __name__ == "__main__":
    # Set your repository path, file path, and commit message
    repository_path = 'https://github.com/Kemeh-30/data-representation-coursework.git'
    file_to_modify = 'C:\Users\fifoa\OneDrive\Desktop\ATU\SECOND SEMESTER'
    old_name = 'Andrew'
    new_name = 'Adedoyinsola'
    commit_message = 'Replace instances of "Andrew" with my name'

    # Full path to the file
    full_file_path = os.path.join(repository_path, file_to_modify)

    # Replace text in the file
    replace_text_in_file(full_file_path, old_name, new_name)

    # Commit and push changes
    commit_and_push_changes(repository_path, file_to_modify, commit_message)
