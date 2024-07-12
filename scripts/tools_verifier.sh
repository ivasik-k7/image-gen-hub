#!/usr/bin/env bash

current_user=$(whoami)
echo "Running verifier script..."
echo "Current user is: $current_user"

ls -l /home/developer/.config/pypoetry/config.toml
ls -ld /home/developer/.config/pypoetry
ls -ld /home/developer/.config
ls -ld /home/developer

commands=("poetry" "python" "pip")
missing_command=false

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
