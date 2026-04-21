# Automation script example

import os
import shutil
from datetime import datetime

def create_backup(source_dir, backup_dir):
    """Create a backup of a directory"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"

    backup_path = os.path.join(backup_dir, backup_name)

    try:
        shutil.copytree(source_dir, backup_path)
        print(f"Backup created successfully: {backup_path}")
        return True
    except Exception as e:
        print(f"Error creating backup: {e}")
        return False

def clean_old_backups(backup_dir, keep_count=5):
    """Keep only the most recent backups"""
    try:
        backups = [f for f in os.listdir(backup_dir) if f.startswith('backup_')]
        backups.sort(reverse=True)

        if len(backups) > keep_count:
            for old_backup in backups[keep_count:]:
                old_path = os.path.join(backup_dir, old_backup)
                shutil.rmtree(old_path)
                print(f"Removed old backup: {old_backup}")

    except Exception as e:
        print(f"Error cleaning backups: {e}")

def organize_files(directory):
    """Organize files by extension"""
    extensions = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
        'spreadsheets': ['.xls', '.xlsx', '.csv'],
        'presentations': ['.ppt', '.pptx'],
        'archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
    }

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = os.path.splitext(filename)[1].lower()

            for category, exts in extensions.items():
                if file_ext in exts:
                    category_dir = os.path.join(directory, category)
                    os.makedirs(category_dir, exist_ok=True)

                    src = os.path.join(directory, filename)
                    dst = os.path.join(category_dir, filename)

                    try:
                        shutil.move(src, dst)
                        print(f"Moved {filename} to {category}/")
                    except Exception as e:
                        print(f"Error moving {filename}: {e}")
                    break

# Example usage
if __name__ == "__main__":
    # Create backup
    source = "C:/Users/Documents"
    backup = "C:/Backups"
    create_backup(source, backup)

    # Clean old backups
    clean_old_backups(backup)

    # Organize files
    organize_files("C:/Downloads")