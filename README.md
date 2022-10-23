# DATASCIENTEST PROJECT 3

## Description
This project is around the Marvel Universe Network.

![Alt text](https://static1.srcdn.com/wordpress/wp-content/uploads/2022/09/MCU-Avengers-on-Comic-Books-Background.jpg?q=50&fit=contain&w=1500&h=&dpr=1.5?raw=true "Optional Title")

## Prerequisites
- You need docker installed to run the project
- Better suited for Linux


## Containers
Here are 3 docker containers.
All are chained with the docker-compose.yml

## Running the project
- Create a directory on your system
- Download the docker-compose.yml file to the newly created folder
- Open a consol inside this folder
- Run the following command: docker-compose up
- Wait few seconds until you see the message "Database successfully populated"


## Access the API
- Open a web browser to: http://172.19.0.4:8000/docs
- Follow endpoints instructions 


## Access to the database
If you want to query the databae, follow below instructions:
- Open a web browser to: http://localhost:7474/browser/
- You are automatically logged to the graph database

Some Cypher knowledges may be necessary
