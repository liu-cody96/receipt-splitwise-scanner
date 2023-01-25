# receipt-splitwise-scanner
(WIP) Upload an image of your receipt and then enter who bought/is paying for which item and then this app will automatically and correctly split the bill :) 

# to run the app, you need to run the frontend and then the backend.
# to run the backend: 
1. cd into backend folder
2. build image --> "docker-compose up --build"
3. to close out, hit Ctrl + C, then type "docker-compose stop" 
4. to open image back up, "docker-compose up"

# to run backend tests:
1. "docker-compose up --build" if you haven't already. If you have, then do "docker-compose up"
2. now type this: "docker-compose exec website py.test receiptscanner/tests"

# to run the frontend: 
1. cd into frontend folder
2. build image --> "docker-compose up --build"
3. to close out, hit Ctrl + C, then type "docker-compose stop" 
4. to open image back up, "docker-compose up"
