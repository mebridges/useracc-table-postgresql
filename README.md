# PostgreSQL User Table Setup

This repository documents the creation of a user account table (`useracc`) in PostgreSQL, designed to store user profile and login information.

## 🔧 Purpose

The `useracc` table is intended for managing user accounts within an internal system. It tracks basic user information and credentials (to be securely handled in production).

## 🗂️ Table Structure

| Column    | Data Type | Description                            |
|-----------|------------|----------------------------------------|
| id        | serial     | Auto-incrementing primary key          |
| userid    | text       | Unique identifier for each user        |
| name      | text       | First name of the user                 |
| surname   | text       | Last name of the user                  |
| birthday  | date       | User's date of birth                   |
| gender    | text       | User's gender                          |
| email     | text       | User's email address (must be unique)  |
| pwd       | text       | Password (stored as plaintext for now; should be hashed later) |

## 🚀 Setup Instructions

1. Clone this repository or download the SQL file.
2. Open **pgAdmin** or connect to your PostgreSQL server using a terminal.
3. Run the SQL file to create the table:

   **Using pgAdmin:**
   - Open your database
   - Open the Query Tool
   - Load and run `create_useracc_table.sql`

   **Using command line:**
   ```bash
   psql -U your_username -d your_database -f createUSERACCtable.sql
