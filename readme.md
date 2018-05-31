[![Coverage Status](https://coveralls.io/repos/github/bozicschucky/Maintenance-Tracker/badge.svg?branch=master)](https://coveralls.io/github/bozicschucky/Maintenance-Tracker?branch=master)
[![Build Status](https://travis-ci.org/bozicschucky/Maintenance-Tracker.svg?branch=ch-test-get-users-157940615)](https://travis-ci.org/bozicschucky/Maintenance-Tracker)

# Maintenance-Tracker-Api
Maintenance Tracker Api is an application that provides users with the ability to reach out to repairs department regarding repair or maintenance requests.
# Getting Started

You can clone the project
https://github.com/bozicschucky/Maintenance-Tracker/tree/ft-Api(v1)

#Usage 
- Open post man and navigate to the following endpoints
   - For authentication visit https://maintainencetrackerapi.herokuapp.com/auth to get a jwt token.
   - The password is 123456 and the username is admin which are supposed to be filled into the headers using post man.
   - Content-type selection should be application/json
   - After authentication visit the urls below to create requests
   - post https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id where id is any number passed in the url
   - get  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id to get a request of the user by id
   - put  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id  to either create request a request when it doesn't exit or update an existing request.
   - get https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests to get all requests created by a logged user
   - api/v1/user/requests

# Hosted on heroku
https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/

![Alt text](Week One/images/img (7).png?raw=true "Title")


# Features
 - Get all the requests for a logged in user
 - Get a request for a logged in user
 - Create a request.
 - Modify a request




# Developed using
 - Python 3.5
 - flask 1.0
 - flaskRestful
 - flaskJwt


# Authors
 - Sekito charles

# Licensing
MIT
