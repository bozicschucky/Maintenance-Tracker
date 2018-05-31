
# Maintenance-Tracker-Api
Maintenance Tracker Api is an application that provides users with the ability to reach out to repairs department regarding repair or maintenance requests.
# Getting Started

You can clone the project
https://github.com/bozicschucky/Maintenance-Tracker/tree/feature/UI

#Usage 
- Open post man and navigate to the following endpoints
   - For authentication visit https://maintainencetrackerapi.herokuapp.com/auth to get a jwt token.
   - The password is 123456 and the username is admin which are supposed to be filled into the headers using post man.
   - Content-type selection should be application/json
   - After authentication visit the urls below to create requests
   - post https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/<int:id> where <int:id> is any number passed in the url
   - get  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/<int:id>  to get a request of the user by id
   - put  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/<int:id>  to either create request a request when it doesn't exit or update an existing request.
   - get https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests to get all requests created by a logged user
   - api/v1/user/requests

# Hosted on heroku



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
