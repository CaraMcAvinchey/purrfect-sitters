# Purrfect Sitters - Cat Sitting Service 
(image)

* You can view the deployed website [here](#).

## Author
Cara McAvinchey 

## Contents

## User Experience

### Strategy
#### Project Goals
* The aim of the project is to provide easily digestible information about popular house plants for beginners and to allow for conversation and sharing of experiences in taking care of them.

### Scope
#### Feature Planning

### Structure
#### User Stories
(table) 
#### Database Schema

(screenshot)

- [X] C - Site users can create/register their own profile to interact with the plant posts.
- [X] R - Site users can open and read the plant blog posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a plant detail post.
- [X] D - Site users can eliminate their like if desired on a plant detail post.

(screenshot)

- [X] C - Site users can create their own comments using a form on each blog post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

(screenshot)

- [X] C - Site users can create their own comments using a form on each blog post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

### Skeleton
#### Wireframes

##### Landing Page 
(screenshot)
- XX
- XX

##### Services Page
(screenshot)
- XX
- XX

##### Account Page
(screenshot)
- XX
- XX

##### Cat Profile Page
(screenshot)
- XX
- XX

##### Bookings Page
(screenshot)
- XX
- XX

### Surface
#### Colors
(colour palette)
 
- The natural color palette links to the theme of plants and plant care. 
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.
- The green header and footer ensures clear contrast and delineation between sections.
- Due to the lighthouse score for accessibility, the background color for the header and footer was adjusted:

#### Typography
(font pairing)

- The font combination was chosen using guidance article from Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The logo and headings use Amatic SC with a fallback of cursive and the body text uses Roboto Condensed with a fallback of san-serif.
- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

#### Images/Icons
(choices of imagery)

- The icons were chosen to provide clear understanding of each plant and its care requirements.
- Each summary card has the same information structure with all icons standard throughout the site.

#### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

#### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## Features

### Navigation
- The users will have a choice of home, login/logout & register when visiting the site. 
- There is a subtle hover state on each of the navigation items for better user experience.
- For mobile devices, the navigation toggles to a hamburger menu.

### Register 
- The user will be able to easily sign up as a user using the below form.
- If users are already registered, there is a link to easily navigate to login instead

### Login/Logout 
- The users can easily sign in using the below form with an option to 'remember me' if desired.
- If a user hasn't registered, there is a link to easily navigate to sign up instead.

### Footer
- The footer links directly to the social media pages of the plant care blog.
- There is a subtle hover state on each icon for better user experience.

### Error 400/404/403/500
- There are error pages in place in case a user is taken to a restricted area or the page doesn't exist.
- The return home button will take the user back to the plant list page.

### Services Page
- XX

### Cat Profile Page
- XX

### Bookings Page
- XX

### Future Features
- It will become less efficient for the user to scroll through many posts in the list view so a search bar will allow users to find specific plants they want to read more about.
- It would increase user experience to add a method to 'save' blog posts so users can keep their favourite plants in one place.
- To increase user interactivity from readers, users could rate blog posts on how helpful the information was and give feedback.
- Pending comments can be added so users are aware they are awaiting approval. 

## TECHNOLOGIES USED
### Languages
- HTML, CSS, JavaScript, Python

### Database
- sqlite3, ElephantSQL

### Frameworks
- Django
- Bootstrap

### Libraries & Packages
- Font Awesome
- Django allauth
- Django Crispy Forms
- Summernote
- gunicorn
- Pillow
- psycopg2
- djangostorages
- boto3

### Programs
- GitPod
- GitHub
- Favicon.io
- Balsamiq
- Diagrams.net
- Tiny PNG
- AWS S3
- Heroku
- Stripe

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

## Deployment 

### ElephantSQL
1. Login to ElephantSQL, access the dashboard and create a new instance (input a name, choose tiny turtle, select a region).
2. Return to the dashcoard, copy the URL.

### Heroku
1. Create a new app in Heroku, choose a unique name and region.
2. Go to settings and add a new config var of ``` DATABASE_URL ```python with the value of the URL from ElephantSQL.
3. Add host name of the Heroku app name to ALLOWED HOSTS in settings.py:

```python
ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
```

### GitHub/GitPod
1. Create a new repository on GitHub, open a new workspace with GitPod.
2. Install django ```pip3 install 'django<4```python to install Django 3.2 the LTS (Long Term Support) version.
3. Create a new project and run the server to see if the app has installed.
4. Run migrations, create a super-user with a username, email and password. 
5. Install ```  pip3 install dj_database_url==0.5.0 psycopg2 ``` and freeze requirements ``` pip freeze > requirements.txt```
6. Add ``` import os``` and ```import dj_database_url``` to settings.py
7. Connect the new database, paste in the ElephantSQL URL (do not commit at this stage):
 
```python
 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #     }
 # }
 
 DATABASES = {
     'default': dj_database_url.parse('your-database-url-here')
 }
```
8. Ensure connection to the external database, run ```python3 manage.py showmigrations``` then run ```python3 manage.py migrate```
 ![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ae646775-8f48-41aa-9f5b-d16e807332f9)
9. Create a new superuser for the new database, same as above.
10. Create an if else statement to setup development and external databases:

 ```python
 if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
      }
    }
 ```
11. Install ```pip3 install gunicorn``` and run ``` pip freeze > requirements.txt```
12. Create a Procfile in the root directory and include ```web: gunicorn project_name.wsgi:applications```
13. Generate a SECRET_KEY, add it to Heroku config vars.
14. Create env.py file (ensure it is included in .gitignore file) and add the SECRET_KEY & DATABASE_URL to environment variables:
![Screenshot 2023-05-14 at 00 09 44](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/a7eb73f5-da1a-4cd2-8691-5c03a4de197b)
15. Edit settings.py to the below:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
```
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ceb9f1d4-35e8-47cd-ba04-6cd07bd8fe37)
19. Add, commit and push to GitHub.
20. Go to Heroku, add ```DISABLE_COLLECT_STATIC = 1``` to Heroku config vars.
23. Connect the project to the GitHub repository using personal account login.
24. Go to settings in Heroku and perform a manual deployment.
25. Go to Heroku settings, enable automatic deployments.
27. Setup AWS S3 bucket (these settings might change since time of writing these instructions).
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/7412eec2-b6c2-42ac-aba7-81b80b3b5774)

## CREDITS
- The Code Institute 'Boutique Ado' walkthrough project assisted and guided in the setup and basic structure of this project.
- Seaside Sewing by Kera Kudmore was a great source of inspiration and best practice regarding testing and README structure.
- Escape Room by XXX helped to understand the code logic, as the site is structured as a service instead of product.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The articles on the blog were written myself and any additional helpful articles were linked to for the user to access for more information.

### Media
- The fonts were sourced using [Google Fonts](https://fonts.google.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
