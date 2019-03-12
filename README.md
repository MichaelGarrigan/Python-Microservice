# Python-Microservice

A service to connect to the twitch API, gather some data on popular streamers and games, and insert said data into a relational database.
This service is meant to run in a cron cycle of every 5 minutes around the clock.

My implementation will utilize AWS Lambda and CloudWatch.

### This service will utilize: 
*Python version 3.7
*Requests
*psycopg2 
*pytest
*json
