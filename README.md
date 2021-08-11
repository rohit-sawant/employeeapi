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

####While sending the request you have to make use of the attribute in the following list, any other attribute or spelling error would lead to inappropriate data. 
`["firstname","lastname","email","age","dob","mobile"]`

## Get a specific Thing

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


## Get a specific Thing using multi valued attribute
While sending the request you have to make use of the attribute in the following list, any other attribute or spelling error would lead to inappropriate data.
`["firstname","lastname","email","age","dob","mobile"]`

### Request

`https://employeeapigetgologistics.herokuapp.com/employee?firstname=Rohit&age=23`

### Response
    {
        "videos": [
            [
                "Rohit",
                "Sawant",
                "sawant.rohit510@gmai.com",
                "23",
                "Sun, 17 May 2020 00:00:00 GMT",
                "8291520420"
            ],
            [
                "Rohit",
                "Bhalu",
                "Bhalu.rohit123@gmai.com",
                "23",
                "Mon, 19 Jan 2020 00:00:00 GMT",
                "7894561230"
            ]
        ]
    }
## Getting all people between two ages

### Request
The minimum value should be entered first and maximum value entered later.
no more than two attribute should be added
`https://employeeapigetgologistics.herokuapp.com/employee?lastname=Sawant&age=10&age=20`
this code will generate all the record having age=>10 and age<=20


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

## Clubbing two same attribute except for age

### Request
Two same attribute cannot be merged in the request (Exception here is age - attribute)

`https://employeeapigetgologistics.herokuapp.com/employee?lastname=Sawant&lastname=Chavan`



### Response

    Not Found
    values not found

## Get a non-existent Thing or attribute

### Request
Searching for data which is not present.
`https://employeeapigetgologistics.herokuapp.com/employee?firstname=Manav`
                            or

Wrong attribute name:
`https://employeeapigetgologistics.herokuapp.com/employee?firstame=Manav`


### Response

    Not Found
    values not found

