# Creating a new react app
create-react-app <app name> --template typescript


# Usage
npm start
Starts the development server.

npm run build
Bundles the app into static files for production.

npm test
Starts the test runner.

npm run eject
Removes this tool and copies build dependencies, configuration files
and scripts into the app directory. If you do this, you can’t go back!

# Current state
1. frontend routing works with npm start but fails when serving static files via fastapi. The root path only works when served via fastapi. likely the only path to success requires fastapi and client to be served separately. There has to be a way around this but it might take a while to find.
2. 
