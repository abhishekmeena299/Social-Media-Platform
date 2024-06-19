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

*4. Other Features*
- extra features include notifications for likes, comments, etc.
- ability to reply and like a comment as well its reply.
- list all posts of a user, all liked and saved posts.
  
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
6. Make Migrations :
   ```bash
       (venv) python manage.py makemigrations
       (venv) python manage.py migrate
   ```
7. Create a superuser: `(venv) python manage.py createsuperuser `
8. Ready to run: `(venv) python manage.py runserver`  

---
## Demo Video
Link for demo video: https://youtu.be/Jx-Bk5Qv6Ak
--
Special Thanks to Corey Schafer : https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p

Chatting and major front-end work inspired from : https://github.com/Ronik22/Django_Social_Network_App
