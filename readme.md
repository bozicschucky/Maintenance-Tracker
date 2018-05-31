[![Coverage Status](https://coveralls.io/repos/github/bozicschucky/Maintenance-Tracker/badge.svg?branch=master)](https://coveralls.io/github/bozicschucky/Maintenance-Tracker?branch=master)
[![Build Status](https://travis-ci.org/bozicschucky/Maintenance-Tracker.svg?branch=ch-test-get-users-157940615)](https://travis-ci.org/bozicschucky/Maintenance-Tracker)

# Maintenance-Tracker-Api
Maintenance Tracker Api is an application that provides users with the ability to reach out to repairs department regarding repair or maintenance requests.
# Getting Started

You can clone the project
https://github.com/bozicschucky/Maintenance-Tracker/tree/ft-Api(v1)

# Usage 
- Open post man and navigate to the following endpoints
   - For authentication visit https://maintainencetrackerapi.herokuapp.com/auth to get a jwt token.
   - In the body of the request provide the following details { "username":"admin","password":"123456"} to get a jwt token that you can use on the other endpoints.
   - Content-type selection should be application/json
   - After authentication visit the urls below to create requests
   - post https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id where id is any number passed in the url
   - get  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id to get a request of the user by id
   - put  https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/id  to either create request a request when it doesn't exit or update an existing request.
   - get https://maintainencetrackerapi.herokuapp.com/api/v1/user/requests to get all requests created by a logged user
   - api/v1/user/requests

# Screenshots
![img 7](https://user-images.githubusercontent.com/12638091/40767278-f0484504-6466-11e8-8645-c20d23b5b8d9.png)
![screenshot 8](https://user-images.githubusercontent.com/12638091/40767342-1f2f0808-6467-11e8-9884-26a3a2ad897d.png)
![screenshot 9](https://user-images.githubusercontent.com/12638091/40767350-24dcaab2-6467-11e8-9e06-bf60c086f769.png)
![screenshot 10](https://user-images.githubusercontent.com/12638091/40767370-31035818-6467-11e8-9246-8ce49b6c321c.png)
![screenshot 13](https://user-images.githubusercontent.com/12638091/40767394-3fe9d7e4-6467-11e8-9e40-0300aa6b9d4f.png)
![screenshot 16](https://user-images.githubusercontent.com/12638091/40767433-5d97cbc0-6467-11e8-8d7a-b8747cd046cb.png)
![screenshot 23](https://user-images.githubusercontent.com/12638091/40767480-7ea7f3c6-6467-11e8-8d8c-b4e3dd1d71f8.png)

# Hosted on heroku
https://maintainencetrackerapi.herokuapp.com/api/v1/user/request/ after authentication

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
