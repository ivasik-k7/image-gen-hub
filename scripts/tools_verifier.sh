#!/usr/bin/env bash

current_user=$(whoami)
echo "Running verifier script..."
echo "Current user is: $current_user"

ls -l /home/developer/.config/pypoetry/config.toml
ls -ld /home/developer/.config/pypoetry
ls -ld /home/developer/.config
ls -ld /home/developer

# Array of commands to check
commands=("poetry" "python" "pip")
missing_command=false

# Loop through each command and check if it exists
for cmd in "${commands[@]}"; do
    if ! command -v "$cmd" &>/dev/null; then
        echo "Command \"$cmd\" does not exist on the system."
        missing_command=true
    fi
done

# If any command is missing, exit with an error
if [ "$missing_command" = true ]; then
    echo "Exiting script due to missing commands."
    exit 1
fi

echo "All components have been set up!"

#!/bin/bash

# Function to check and adjust permissions
check_and_adjust_permissions() {
    # Check permissions for config.toml
    if [ -f "/home/developer/.config/pypoetry/config.toml" ]; then
        echo "Checking permissions for config.toml..."
        if [ -r "/home/developer/.config/pypoetry/config.toml" ] && [ -w "/home/developer/.config/pypoetry/config.toml" ]; then
            echo "Permissions are sufficient for config.toml"
        else
            echo "Adjusting permissions for config.toml..."
            sudo chmod u+rw /home/developer/.config/pypoetry/config.toml
            sudo chown developer:developers /home/developer/.config/pypoetry/config.toml
            echo "Permissions adjusted for config.toml"
        fi
    else
        echo "File /home/developer/.config/pypoetry/config.toml does not exist"
    fi

    # Check permissions for pypoetry directory
    echo "Checking permissions for pypoetry directory..."
    if [ -d "/home/developer/.config/pypoetry" ]; then
        if [ -r "/home/developer/.config/pypoetry" ] && [ -w "/home/developer/.config/pypoetry" ]; then
            echo "Permissions are sufficient for pypoetry directory"
        else
            echo "Adjusting permissions for pypoetry directory..."
            sudo chmod u+rwx /home/developer/.config/pypoetry
            sudo chown developer:developers /home/developer/.config/pypoetry
            echo "Permissions adjusted for pypoetry directory"
        fi
    else
        echo "Directory /home/developer/.config/pypoetry does not exist"
    fi

    # Check permissions for .config directory
    echo "Checking permissions for .config directory..."
    if [ -d "/home/developer/.config" ]; then
        if [ -r "/home/developer/.config" ] && [ -w "/home/developer/.config" ]; then
            echo "Permissions are sufficient for .config directory"
        else
            echo "Adjusting permissions for .config directory..."
            sudo chmod u+rwx /home/developer/.config
            sudo chown developer:developers /home/developer/.config
            echo "Permissions adjusted for .config directory"
        fi
    else
        echo "Directory /home/developer/.config does not exist"
    fi

    # Check permissions for developer home directory
    echo "Checking permissions for developer home directory..."
    if [ -d "/home/developer" ]; then
        if [ -r "/home/developer" ] && [ -w "/home/developer" ]; then
            echo "Permissions are sufficient for developer home directory"
        else
            echo "Adjusting permissions for developer home directory..."
            sudo chmod u+rwx /home/developer
            sudo chown developer:developers /home/developer
            echo "Permissions adjusted for developer home directory"
        fi
    else
        echo "Directory /home/developer does not exist"
    fi
}

# Execute the function to check and adjust permissions
check_and_adjust_permissions
