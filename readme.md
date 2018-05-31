
# Maintenance-Tracker-Api
Maintenance Tracker Api is an application that provides users with the ability to reach out to repairs department regarding repair or maintenance requests.
# Getting Started

You can clone the project
https://github.com/bozicschucky/Maintenance-Tracker/tree/feature/UI

#Usage 
- Open post man and navigate to the following endpoints
   - for authentication first visit the route /auth to get jw token to be used for login
   - The password is 123456 and the username is admin which are supposed to be filled into the headers using post man.
    
   - api/v1/user/request/<int:id> where <int:id> is any number passed in the url
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
