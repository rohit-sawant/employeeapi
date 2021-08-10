# REST API 

This is an Employee API which fetches data according to the respective attributes:
* First name
* Last name
* Email
* Age
* Date Of Birth
* Mobile No

The entire application is contained within the `app.py` file.

`Procfile` is a minimal configuration for heroku.


## Install

    pip install -r requirements.txt

## Run the app

    python app.py


# REST API

The REST API to the example app is described below.

## Get all the values

### Request

`https://employeeapigetgologistics.herokuapp.com/`


### Response

    {"employee":[
    ["Rohit","Sawant","sawant.rohit510@gmai.com","19","Sun, 17 May 2020 00:00:00 GMT","8291520420"],
    ["Swati","Sawant","sawant.swati510@gmai.com","20","Thu, 05 Oct 2000 00:00:00 GMT","8976938972"],
    ["Sandeep","Sawant","sawant.sandeep@gmai.com","23","Wed, 17 May 2000 00:00:00 GMT","9699517660"]]}


## Get a specific Thing
While sending the request you have to make use of the attribute in the following list, any other attribute or spelling error would lead to inappropriate data.
`["firstname","lastname","email","age","dob","mobile"]`

### Request

`https://employeeapigetgologistics.herokuapp.com/employee?firstname=Rohit`

### Response
    {
        "videos": [
            [
                "Rohit",
                "Sawant",
                "sawant.rohit510@gmai.com",
                "19",
                "Sun, 17 May 2020 00:00:00 GMT",
                "8291520420"
            ]
        ]
    }


## Get a non-existent Thing or attribute

### Request

`https://employeeapigetgologistics.herokuapp.com/employee?firstname=Manav`
                            or
`https://employeeapigetgologistics.herokuapp.com/employee?firstName=Manav`


### Response

    Not Found
    values not found

## Merging two or more attributes

### Request

`https://employeeapigetgologistics.herokuapp.com/employee?lastname=Sawant&age=10&age=20`

### Response

    {
        "videos": [
            [
                "Rohit",
                "Sawant",
                "sawant.rohit510@gmai.com",
                "19",
                "Sun, 17 May 2020 00:00:00 GMT",
                "8291520420"
            ],
            [
                "Swati",
                "Sawant",
                "sawant.swati510@gmai.com",
                "20",
                "Thu, 05 Oct 2000 00:00:00 GMT",
                "8976938972"
            ]
        ]
    }

