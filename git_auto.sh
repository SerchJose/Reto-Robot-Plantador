#!/bin/bash

# Add all files to the staging area
git add .

# Prompt the user to enter the commit message
read -p "Ingrese el mensaje de commit: " commitMessage

# Commit with the custom message
git commit -m "$commitMessage"

# Push to the remote repository
git push

# Pause to see the results
read -p "Presione enter para continuar..."
