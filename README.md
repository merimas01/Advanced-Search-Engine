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
![fastapiapp](https://github.com/user-attachments/assets/ee8e6487-400c-4e61-810d-2fcf800dda35)
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
![reactapp](https://github.com/user-attachments/assets/c9d92cb6-416b-4e18-8c01-0cf89e386a98)
- Run following commands:
  - npm install
  - npm run dev
- Open the application at: http://localhost:5173


