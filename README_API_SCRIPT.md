'''
Script:

- Able to take user input
- Import data from the RDW -API (contains registered cars)
- Convert it to a pandas DataFrame (table)
- Create a folder for the files to be exported
- Export the file in the right folder

API 

HTTP -requests:

- GET
- PUT
- POST
- DELETE

response:
- Code
    - 200, OK
    - 201, redirect
    - 403, unauthorized
    - 404, not found
    - 503, internal server error
    
- body/content

Open API's --> GET

-REQUESTS-

third-party library, "requests"

(venv)
> pip install requests 

send request
where to? --> Endpoint
-                   API documentation

'''
