# Purrfect Sitters - Cat Sitting Service 
(image)

* You can view the deployed website [here](#).

## Author
Cara McAvinchey 

## Contents

## User Experience

### Strategy
#### Project Goals
* A service which allows cat owners to book trusted and affordable cat sitting services online with experienced cat sitters, offering personalised care packages giving enjoy peace of mind whilst travelling.

### Scope
#### Feature Planning

### Structure
#### User Stories
(table) 
#### Database Schema

![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/4c20560c-b364-4a58-9fe9-4edd9926a4e7)

* A relational database was designed and the data is represented above in an ERD with four custom models.
* The checkout model was based off Boutque Ado walkthrough project with some adjustments.
* The number of cats per profile is connected to the owner.
* The Cat model is built to have full CRUD functionalities.
* The Booking model will be implemented with full CRUD in the next interation due to time contraints and therefore will be a future feature.
* The Service model will add the ability to add, update, delete and edit package information from the client-side in a future implementation.

##### Booking
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/c0160aa1-0bb2-4019-8dd1-076cc115dfe2)

- [X] C - Customers can create a booking through the site when logged in.
- [] R - Future feature, users will receive an email with a summary of their booking.
- [] U - Future feature, users can contact Purrfect Pets to update their booking for now.
- [] D - Future feature, users can contact Purrfect Pets to delete their booking for now.

##### Cat
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/4f775f4f-9df9-49d4-885a-2f86fcf74922)

- [X] C - Customers can sign up and register a profile thanks to Django allauth system. 
- [X] R - Customers can see a list of their cats added to their profile and click for further information.
- [X] U - Customers can update their cat detail cards if needed.
- [X] D - Customers can delete a cat if they no longer need future cat sitting services for that pet.

### Skeleton
#### Wireframes

##### Landing Page 
- The landing page was designed to have a clear and easy to navigate layout, with a drop down for login/logout and profile information access.
- The customer can immediately see what the page is about with the page name and description.
- There is a clear call to action button to book.

<img width="916" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/31803c0c-3319-417d-96ed-75e5be05f128">

##### Services Page
- The page is to summarises the services offered including name, time and price.
- There is an FAQ section for new or returning users to refer to if needed.

<img width="566" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/b8dc6b4f-dc68-4052-95ac-d0222487f34a">

##### Account Page
- The django allauth system provided all the login/logout and registration functionalities for the page
- The templates were styled in some areas to account for the brand look and feel.

<img width="832" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/83d9ddab-8c6b-45da-a9e7-5638764526a1">
<img width="415" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/9c6f36f0-39d7-4965-92b8-58a61203a972">

##### Cat Profile Page
- The users will be able to view a list of their cats in easy to read cards using Bootstrap to achieve this.
- If they do not have cats, a message will be displayed accordingly.
- Functionalities will be added to edit and delete cat profiles.

<img width="631" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/461013da-25d9-42da-a6b2-d2ca1f6203c3">
<img width="362" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/4c2cb889-b839-4350-bb3d-506960722d91">
<img width="749" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/61774a13-a535-4563-b6f7-da675f15259f">

##### Bookings Page
- The bookings page allows the user to choose the Purrfect Package they prefer, the date of service required and special instructions.
- Plans for viewing past bookings, editing and deleting bookings have been planned for. 

<img width="651" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/6b87bed7-7005-4ee5-8efe-c33b6c3fe37c">
<img width="687" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/86e85c72-b767-430a-b34b-4d35053c5258">

### Surface

#### Brand
<img width="200" height="200" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/38b9714d-8f41-405b-ba32-6b2daa85689d">

- The logo was custom designed myself.
- The cat icon in the center was found using creative commons search.

#### Colors
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/7c482dfc-a4c1-4b45-b73d-b070970c96a6)
 
- The dark grey colour #2a2727 was chosen and paired with white.
- The header and footer have a clear contrast and delineation from the body content. 

#### Typography
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ad835b75-bd49-4d34-9964-220260adf92e)

- The font combination was chosen using guidance blog article from Haris Bacic [here]([https://artisanthemes.io/great-google-font-combinations-ready-use/](https://onextrapixel.com/10-great-font-combinations-from-google-web-fonts/)).
- The logo and headings use ABeeZee and the body text uses Patrick Hand both with a fallback of san-serif.
- It allows for a more light-hearted aspect to the service and links well to pet care.
- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

#### Images/Icons
- The paw icon and cat images were chosen to add some personality to the page in the context of the service provided.
- Each summary card has the same information structure with all icons standard throughout the site.

#### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underline when hovered for clear distinction from the body text.

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
- The ERD was created with [draw.io](https://www.drawio.com/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor Malia for continuous helpful feedback and support throughout the project.
- I greatly appreciate the tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
