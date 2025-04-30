# Advanced Search Engine

## About the project

AdvancedSearchEngine is a project for my Bachelor thesis. 

## Prerequisites

- Visual Studio Code installed
- Python Installed (version: 3.13.3)
- Sql Server Management Studio

## Setting up 

- Clone the repository: https://github.com/merimas01/Advanced-Search-Engine.git 
- Open terminal in the *my_fastapi_app* directory 
![vsc](https://github.com/user-attachments/assets/80cc5073-9b32-4f6a-ada6-b702a095b16a)
- Run a following command to install dependencies: *pip install -r dependencies.txt*
- Connect to a SQL Server with your credentials
- Execute an ***advanced_search_engine_database.sql*** script to create a database
- Modify the credentials (username, password) inside the ***db/database.py*** file 
- Run a ***data_seed.py*** script to generate test data 
- Run a following command to start the application:  *python -m uvicorn app.main:app --reload*
- Wait until startup completes
- Open Swagger at http://127.0.0.1:8000/docs

## Web application

- Open terminal in the *my-app* directory

- Run following commands:
- - npm install
- - npm run dev
- Open the application at: http://localhost:5173

## Notes

