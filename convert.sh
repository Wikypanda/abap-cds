#!/bin/bash

# Function to print colored messages
print_color() {
    COLOR=$1
    MESSAGE=$2
    case $COLOR in
        "green") echo -e "\e[32m$MESSAGE\e[0m";;   # Green
        "red") echo -e "\e[31m$MESSAGE\e[0m";;     # Red
        "yellow") echo -e "\e[33m$MESSAGE\e[0m";;  # Yellow
        *) echo "$MESSAGE";;                         # Default
    esac
}

# Current Date and Time (UTC)
current_date=$(date -u +"%Y-%m-%d %H:%M:%S")
print_color "green" "Current Date and Time (UTC - YYYY-MM-DD HH:MM:SS formatted): $current_date"

# Current User Login
current_user=$(whoami)
print_color "green" "Current User's Login: $current_user"

# Convert HTML function
convert_html() {
    if [ -z "$1" ]; then
        print_color "red" "No file provided for conversion."
        exit 1
    fi

    local input_file=$1
    local output_file="${input_file%.txt}.html"

    # Check if the file exists
    if [[ ! -f $input_file ]]; then
        print_color "red" "Error: $input_file does not exist."
        exit 1
    fi

    # Convert to HTML (this is a placeholder for actual conversion)
    echo "<html><body><pre>$(cat $input_file)</pre></body></html>" > "$output_file"
    
    if [[ $? -eq 0 ]]; then
        print_color "green" "Conversion successful: $output_file"
    else
        print_color "red" "Error during conversion."
        exit 1
    fi
}

# Example usage of the convert_html function
convert_html "$1"