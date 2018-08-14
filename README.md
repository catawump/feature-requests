# Feature Requests for IWS Engineering Test Project

// How to Run

- Clone the repository to your local machine
- Install virtualenv and flask if needed
- Navigate to the directory and activate the virtual environment
- flask run
- Open a browser and navigate to localhost:5000

// Feature Overview

- Login/logout and registration
- Internal pages require login to view/edit
- Ability for users to submit feature requests on behalf of clients
- Users can view full request details or delete requests from the dashboard
- Requests are ranked based on client priority across clients
- If a duplicate priority value is selected, new item takes priority and all other requests for that client reorder accordingly
- Front end has been lightly styled for a more visually appealing experience

// Technology Used

- Server framework: Flask
- Server scripting: Python 2.7
- ORM: Sql-Alchemy
- CSS: Bootstrap
- Extensions: WTForms/Flask-WTF, Flask-Migrate/Alembic, Werkzeug, Flask-Login
