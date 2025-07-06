# Deployment:

The Unique Dining project was developed using version control via Git and hosted on GitHub. This allowed for organized source code management, collaboration, and easy deployment to platforms like Heroku.

Table of Contents

## 1. GitHub Repository Creation and the app

Create a New Repository on GitHub
    - Navigate to GitHu
    - Click on New Repository
    - Enter a repository name (e.g., heavenly-dining)
    - Add a description (optional)
    - Choose Public or Private
    - Click Create Repository

Set Up Git Locally and Push to GitHub
    - echo "# heavenlydining" >> README.md
    - git init
    - git add README.md
    - git commit -m "first commit"
    - git branch -M main
    - git remote add origin https://github.com/sowmya1283/heavenlydining.git
    - git push -u origin main


## 2. User stories in GitHub Projects

    - Create a GitHub Project
    - Add Columns to Represent Workflow (you can edit the workflow to include issues)
    - Create Issues for Each User Story
    - Add Issues to the Project Board
    - Move Cards Through the Board
    - Use Labels and Assignees

## 3. Heroku App Creation and Deployment
   - Create the app on Heroku and update the Config Vars section of the Settings tab with DISABLE_COLLECTSTATIC and value to 1
   - Install webserver gunicorn and include it to the project requirements.txt (This lists all the required Python packages)
        pip3 install gunicorn~=20.1
        pip3 freeze --local > requirements.txt
   - Create Procfile and neccessary steps. This tells Heroku how to run your app
   - Update settings.py: Set DEBUG to False and added , '.herokuapp.com' to the ALLOWED_HOSTS
   - Push the code to github and Deploy: Go to Deploy tab in Heroku, search for your github repo, connect to it and then Deploy branch
   - To view the app is deployed click on view app.
   
## 4. Create the database
 Instance of a cloud-based PostgreSQL database is created using Code Institute student email provided.
## 5. Deployment of Static Files


