# Advanced Search Engine

## About the project

AdvancedSearchEngine is a project for my Bachelor thesis that uses AI and ML tools. It demonstrates how an advanced search engine works and how it is such an important part of every app with a large amount of data. 

It consists of:
- autocompletion  - offering the potential next words for user's input even if it's misspelled
- spell correction - correcting misspelling and understanding what user wanted to write
- search history - displaying user's history and enabling him to use it while searching data
- audio search - seaching data using own voice 
- semantic search - enabling user to search data with multiple words, synonyms, abbreviations, misspelled words or incorrect word order

The goals of this project:
- to easily understand what user really wants to search and to provide him the most accurate results 
- to simplify and speed up searching by suggesting next words, showing search history, correcting spelling, using voice etc
- to satisfy all users (some users will use search box, some will use voice, it's up to their preference)
- to create the search-engine-pattern that could be used in different apps
- to improve the User Experience

This project is made with FastAPI for the backend application and ReactJs+Vite for the frondend application. 
The database is created and managed in Sql Server Management Studio. 

## Prerequisites

- Visual Studio Code installed
- Python Installed (version: 3.11.8)
- Sql Server Management Studio
- Node.js installed (version: v22.14.0)
- set values in Environment Variables to API_KEY (set your value), DATABASE_SERVER (set your value), DATABASE_NAME ("AdvancedSearchEngine"), DATABASE_USERNAME (set your value) and DATABASE_PASSWORD (set your value). Then restart the computer

## Backend Web App and Database

- Clone the repository: https://github.com/merimas01/Advanced-Search-Engine.git 
- Open terminal in the *my_fastapi_app* directory 
![fastapiapp](https://github.com/user-attachments/assets/ee8e6487-400c-4e61-810d-2fcf800dda35)
- Run a following command to install dependencies: *pip install -r dependencies.txt*
- Connect to a SQL Server with your credentials
- Execute an ***advanced_search_engine_database.sql*** script to create a database
- Run a ***data_seed.py*** script to generate test data 
- Run a following command to start the application:  *python -m uvicorn app.main:app --reload*
- Wait until startup completes
- Open Swagger at http://127.0.0.1:8000/docs

## Frontend Web App

- Open terminal in the *my-app* directory
![reactapp](https://github.com/user-attachments/assets/c9d92cb6-416b-4e18-8c01-0cf89e386a98)
- Run following commands:
  - npm install
  - npm run dev
- Open the application at: http://localhost:5173


