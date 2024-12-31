#!/bin/bash

# Set variables
DB_NAME="mydb"
DB_USER="myuser"
DB_HOST="localhost"       # Change if necessary (e.g., remote host IP)
DB_PORT="5432"            # Default PostgreSQL port
BACKUP_FILE="/c/Users/deepak.pandey-v/Downloads/FullBackUp-mydb-202412161118.sql"

# Check if the backup file exists
print("Starting the script...")

if [ ! -f "$BACKUP_FILE" ]; then
  echo "Error: Backup file '$BACKUP_FILE' not found."
  exit 1
fi

# Prompt for the password
read -s -p "Enter the password for user $DB_USER: " PGPASSWORD
echo
export PGPASSWORD
print("Starting the script...")


# Drop the existing database (optional, ensure you have a valid backup!)
echo "Dropping existing database '$DB_NAME'..."
if ! psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -c "DROP DATABASE IF EXISTS $DB_NAME;"; then
  echo "Error: Failed to drop the database '$DB_NAME'."
  unset PGPASSWORD
  exit 1
fi

print("Starting the script...")

# Create a new database
echo "Creating new database '$DB_NAME'..."
if ! psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -c "CREATE DATABASE $DB_NAME;"; then
  echo "Error: Failed to create the database '$DB_NAME'."
  unset PGPASSWORD
  exit 1
fi

# Restore the backup
echo "Restoring the database from '$BACKUP_FILE'..."
if ! psql -U "$DB_USER" -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -f "$BACKUP_FILE"; then
  echo "Error: Failed to restore the database from '$BACKUP_FILE'."
  unset PGPASSWORD
  exit 1
fi
print("Starting the script...")


# Unset the PGPASSWORD for security
unset PGPASSWORD

echo "Database restoration completed successfully!"
print("Starting the script...")
