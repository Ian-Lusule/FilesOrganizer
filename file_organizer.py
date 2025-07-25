```python
# file_organizer.py

import os
import shutil
import argparse
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def organize_files(directory, rules):
    """Organizes files in a directory based on file type, date modified, and user-defined rules.

    Args:
        directory: The directory to organize.
        rules: A dictionary defining organization rules.  Keys are file extensions (e.g., '.txt', '.jpg'),
               and values are target subdirectories.  A special key '*' can be used for all other file types.
    """

    if not os.path.isdir(directory):
        logging.error(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                _, ext = os.path.splitext(filename)
                ext = ext.lower()  # Handle case-insensitive extensions

                target_subdir = None
                if ext in rules:
                    target_subdir = rules[ext]
                elif '*' in rules:
                    target_subdir = rules['*']

                if target_subdir:
                    target_dir = os.path.join(directory, target_subdir)
                    os.makedirs(target_dir, exist_ok=True)  # Create target directory if it doesn't exist

                    # Add date-based subdirectories for better organization (optional)
                    modified_time = os.path.getmtime(filepath)
                    modified_date = datetime.datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d')
                    date_subdir = os.path.join(target_dir, modified_date)
                    os.makedirs(date_subdir, exist_ok=True)
                    target_path = os.path.join(date_subdir, filename)

                    shutil.move(filepath, target_path)
                    logging.info(f"Moved '{filename}' to '{target_path}'")

                else:
                    logging.warning(f"No rule found for file '{filename}'. Skipping.")

            except (shutil.Error, OSError) as e:
                logging.error(f"Error processing '{filename}': {e}")


def main():
    """Parses command-line arguments and runs the file organizer."""
    parser = argparse.ArgumentParser(description="Organize files in a directory.")
    parser.add_argument("directory", help="The directory to organize")
    parser.add_argument("-r", "--rules", nargs='+', required=True,
                        help="Organization rules in the format 'ext1=subdir1 ext2=subdir2 ...'.  Use '*' for others.")

    args = parser.parse_args()

    rules = {}
    for rule in args.rules:
        try:
            ext, subdir = rule.split('=')
            rules[ext.lower()] = subdir
        except ValueError:
            logging.error(f"Invalid rule format: '{rule}'. Use 'ext=subdir'.")
            return

    organize_files(args.directory, rules)
    logging.info("File organization complete.")


if __name__ == "__main__":
    main()

```

To run this:

1.  **Save:** Save the code above as `file_organizer.py`.
2.  **Run from the command line:**  Navigate to the directory containing `file_organizer.py` and run it with the directory to organize and rules as arguments. For example:

    ```bash
    python file_organizer.py /path/to/your/directory -r ".txt=documents" ".jpg=images" "*.pdf=documents" ".mp3=audio"
    ```

    Replace `/path/to/your/directory` with the actual path.  The `-r` flag specifies the rules.  Each rule is `extension=target_directory`.  `*` is a wildcard for all other file types.


This improved version includes:

*   **Error Handling:** Uses `try...except` blocks to catch `shutil.Error` and `OSError` during file operations.
*   **Logging:** Uses the `logging` module for better feedback and error reporting.
*   **Argument Parsing:** Uses `argparse` for a cleaner command-line interface.
*   **Date-Based Subdirectories:** Adds optional date-based subdirectories within the type-based directories for finer organization.
*   **Wildcard Support:** Allows using `*` to define a rule for all file types not explicitly specified.
*   **Case-Insensitive Extensions:** Handles file extensions case-insensitively.
*   **Clearer Documentation:** Improved docstrings and comments.


Remember to replace `/path/to/your/directory` with the actual path to the directory you want to organize.  Test thoroughly on a sample directory before running it on important data.
