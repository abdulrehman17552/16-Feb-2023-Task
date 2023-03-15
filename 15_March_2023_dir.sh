#!/bin/bash

# Prompt the user to enter the directory path to be monitored
read -p "Enter the directory path to be monitored: " directory_path

# Prompt the user to enter a regular expression pattern to match the file names to be monitored
read -p "Enter a regular expression pattern to match the file names to be monitored: " regex_pattern

# Validate the regex pattern
if ! [[ "$regex_pattern" =~ ^[[:alnum:]|[:space:]|\*|\-|\.|\(|\)|\[|\]|\{|\}|\\|\+|\?]+$ ]]; then
    echo "Invalid regex pattern"
    exit 1
fi

# Create a function that will be called whenever a file change is detected
function file_changed() {
    local filename="$1"
    echo "File $filename has been modified."
    
    # Use grep to search the file for a specific string
    if grep -q "specific string" "$filename"; then
        # Use awk to extract specific values from the line containing the string
        local extracted_value=$(awk '/specific string/ {print $2}' "$filename")
        
        # Use cp to create a backup of the file in a separate backup directory
        backup_dir="backup_$(date +%Y%m%d_%H%M%S)"
        if [ -d "$backup_dir" ]; then
            read -p "Backup directory already exists. Do you want to overwrite it? [y/n]: " overwrite
            if [ "$overwrite" = "n" ]; then
                backup_dir="backup_$(date +%Y%m%d_%H%M%S)_2"
            fi
        fi
        mkdir "$backup_dir"
        cp "$filename" "$backup_dir"
        
        # Use sed to modify the contents of the file by replacing the specific string with a new value
        sed -i "s/specific string/new value/g" "$filename"
        
        # If the modified file contains more than 10 lines, extract the first 5 and last 5 lines to a separate file
        if [ $(wc -l < "$filename") -gt 10 ]; then
            head -5 "$filename" > "${filename}_head.txt"
            tail -5 "$filename" > "${filename}_tail.txt"
        fi
        
        # Use tar to compress the backup directory and save it with a timestamp in the filename
        tar -czvf "${backup_dir}_$(date +%Y%m%d_%H%M%S).tar.gz" "$backup_dir"
        rm -rf "$backup_dir"
        
        echo "File $filename has been modified and backed up."
    fi
}

# Check if there are files in the specified directory or its subdirectories that match the specified regular expression pattern
if ! [ "$(find "$directory_path" -type f -name "$regex_pattern" | head -n 1)" ]; then
    echo "No files matching the specified regular expression pattern were found in $directory_path"
    exit 1
fi

# Use inotifywait to monitor the specified directory for changes to the files matching the specified regular expression pattern
inotifywait -m -r -e modify,delete,move,create --format '%w%f' "$directory_path" | while read filename; do
    # Check if the filename matches the regular expression pattern
    if [[ "$filename" =~ $regex_pattern ]]; then
        # Call the function defined in step 3 and pass the name of the changed file as an argument
        file_changed "$filename"
    fi
done
