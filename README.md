# Social-Media-Platform
Social media web-application using Django for ArIES open project.

## Features:
*1. User Authentication and Profiles:*
- create your profile, follow people and make friends

*2. Messaging and Chat:*
- enjoy realtime private chatting (using Websocket)

*3. News Feed and Content Sharing*
- share posts including photos, videos and links
- like, share, comment on your friend's posts

  
## Instructions
1. Create and navigate to a new Virutual Environment:
   ```bash
       python -m venv venv
       cd venv
       source bin/activate  
   ```
2. Clone the repository: `(venv) git clone <repository_url>`
3. Navigate into the project folder:
   ```bash
       (venv) cd Social-Media-Plaform
       (venv) cd myproject
   ```
4. Install dependencies: `(venv) pip install -r requirements1.txt`
5. Rename temp.env to .env
6. Make Migrations and create a superuser:
   ```bash
       (venv) pip manage.py makemigrations
       (venv) pip manage.py migrate
       (venv) pip manage.py runserver
   ```
7. Create a superuser: `(venv) pip manage.py createsuperuser `
8. Ready to run: `(venv) pip manage.py runserver`  

---
## Demo Video
Link for demo video: 
