# file-organizer-python

## Description

`file-organizer-python` is a Python script designed to efficiently organize files within a specified directory. It categorizes files based on their type, modification date, and customizable user-defined rules.  The script prioritizes robust error handling and provides clear, informative feedback to the user throughout the organization process.

## Features

* **File Type Organization:** Automatically sorts files into folders based on their extensions (e.g., images, documents, videos, etc.).
* **Date-Based Organization:** Organizes files into folders based on their last modification date (e.g., year, month, year-month).
* **Customizable Rules:** Allows users to define their own rules for file organization using a simple configuration file (see Usage section).
* **Error Handling:** Gracefully handles exceptions such as permission errors, invalid file paths, and unexpected file types.
* **User Feedback:** Provides informative messages to the user during each stage of the organization process, including progress updates and error reports.
* **Dry Run Mode:** Allows users to preview the changes without actually moving files.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ian_Lusule/file-organizer-python.git
   ```

2. **Install dependencies:**  The script requires Python 3.7 or higher.  No external libraries are currently needed, but future versions might.  If so, they will be specified in a `requirements.txt` file.  You can install them using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configuration (Optional):** Create a configuration file named `config.yaml` (or specify a different file using the `-c` flag) in the same directory as the script.  This file allows you to define custom rules for file organization.  The format is YAML.  Example:

   ```yaml
   rules:
     - extension: ".txt"
       destination: "Documents"
     - extension: ".jpg"
       destination: "Images/2023" #Example of combining extension and date-based rules
   ```

2. **Run the script:**

   ```bash
   python file_organizer.py <directory_path> [-c <config_file>] [-d]
   ```

   * `<directory_path>`: The path to the directory you want to organize.
   * `-c <config_file>`: (Optional) Path to the configuration file (defaults to `config.yaml`).
   * `-d`: (Optional) Enables dry run mode.  The script will print the planned actions without actually moving files.


## Contributing Guidelines

Contributions are welcome!  Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure they are well-documented.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [LICENSE](LICENSE)

##  Error Handling and Logging

The script includes comprehensive error handling to catch potential issues such as:

* **Invalid directory paths:**  The script checks if the provided directory path is valid and accessible.
* **Permission errors:**  The script handles cases where it lacks the necessary permissions to access or modify files.
* **Unexpected file types:** The script gracefully handles files with unknown extensions, logging them for review.

Detailed log messages are printed to the console, providing information about the organization process and any encountered errors.  Future versions may include more sophisticated logging to a file.
