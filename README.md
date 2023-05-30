# Purrfect Sitters - Cat Sitting Service 
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/d696328a-dc32-434a-9083-ba7c8d9e99ab)

Purrfect Sitters is an online cat sitting service which offers trusted and affordable care for your beloved feline friends. Book a cat sitter to visit your home whilst you are away and choose between various time packages. Register a profile, add your cats information to our site and complete a simple booking and online payment to get started.

You can view the deployed website [here](https://purrfect-sitters-service.herokuapp.com/).

## Author
Cara McAvinchey 

## Contents

- [Purrfect Sitters - Cat Sitting Service](#purrfect-sitters---cat-sitting-service)
  * [User Experience](#user-experience)
    + [Strategy](#strategy)
      - [Project Goals](#project-goals)
    + [Structure](#structure)
      - [User Stories](#user-stories)
      - [Database Schema](#database-schema)
        * [Booking](#booking)
        * [Cat](#cat)
        * [Service](#service)
        * [Checkout](#checkout)
    + [Skeleton](#skeleton)
      - [Wireframes](#wireframes)
        * [Landing Page](#landing-page)
        * [Services Page](#services-page)
        * [Account Page](#account-page)
        * [Cat Profile Page](#cat-profile-page)
        * [Bookings Page](#bookings-page)
    + [Surface](#surface)
      - [Brand](#brand)
      - [Colors](#colors)
      - [Typography](#typography)
      - [Images/Icons](#images-icons)
      - [Animations](#animations)
      - [Responsiveness](#responsiveness)
  * [Features](#features)
    + [Navigation](#navigation)
    + [Register](#register)
    + [Login/Logout](#login-logout)
    + [Footer](#footer)
    + [Error 400/404/403/500](#error-400-404-403-500)
    + [Services Page](#services-page-1)
    + [Cat Profile Page](#cat-profile-page-1)
    + [Cat Detail Pages](#cat-detail-pages)
    + [Bookings Page](#bookings-page-1)
    + [Future Features](#future-features)
  * [Web Marketing Strategies](#web-marketing-strategies)
    + [SEO](#seo)
    + [Content Marketing](#content-marketing)
      - [Email Marketing](#email-marketing)
      - [Social Media Marketing](#social-media-marketing)
    + [Paid Advertising](#paid-advertising)
  * [Technologies](#technologies)
    + [Languages](#languages)
    + [Database](#database)
    + [Frameworks](#frameworks)
    + [Libraries & Packages](#libraries---packages)
    + [Programs](#programs)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [ElephantSQL](#elephantsql)
    + [Heroku](#heroku)
    + [GitHub/GitPod](#github-gitpod)
  * [Credits](#credits)
    + [Media](#media)
  * [Acknowledgements](#acknowledgements)

## User Experience

### Strategy
#### Project Goals
* Build an easy to use and information website that allows cat owners to book cat sitting services online.
* Ensure users are able to build and edit a cat profile.
* Create a user friendly booking and payment mechanism.

### Structure
#### User Stories
- The 27 user stories were generated using an agile approach in a *"As a [role], I can [action], so that [benefit]"* format with acceptance criteria in declarative gherkin syntax.
- They were prioritised according to low, medium and high priority during the planning phase, focusing on the basic requirements as high priority.
- These were documented as issues in GitHub and added to GitHub projects in a kanban board found [here](https://github.com/users/CaraMcAvinchey/projects/5) 
- This was utilised throughout the development process to build the project in increments.
- Record of progress or issues where documented in each user story as development progressed.
- The order of implementation was as follows:
    - Landing page, navigation and footer with contact and social links.
    - Service page with package information and FAQs.
    - Registration, login and logout features. 
    - My profile page, to view/add/edit/delete cats.
    - Booking page
    - Checkout page

|  | **VIEWING AND NAVIGATION** | PRIORITY |
|---|---|---|
| 1 | As a user, I can view the landing page so that I can find key information about the company and it's services. | HIGH |
| 2 | As a user, I can view the packages offered by Purrfect Sitters, so that I can learn more about the service in detail. | HIGH |
| 3 | As a new user, I can easily find the contact information of Purrfect Sitters, so that I can reach out to them for more information. | HIGH |
| 4 | As a user, I can easily connect with the social media accounts of Purrfect Sitters, so that I can learn more about the activities of the brand. | MEDIUM |
| 5 | As a user, I can sign up to receive a newsletter from Purrfect Pets, so that I can get updates about the company and its services. | MEDIUM |
| 6 | As a new or authenticated user, I can be notified once completing an important action on the website, so I know what I was last doing. | MEDIUM |
| 7 | As an authenticated user, I can write an optional rating/review, so that I can provide feedback to Purrfect Sitters about my experience. | LOW |
|  | **REGISTRATION AND ACCOUNTS** |  |
| 8 | As a new user, I can safely register for an account with an email and password, so that I can book cat-sitting services with Purrfect Sitters. | HIGH |
| 9 | As an authenticated user, I can view my profile information when logged in, so that I can ensure it is complete and up-to-date. | MEDIUM |
| 10 | As a user, I can safely login and logout of my account so that I can keep my information private. | HIGH |
| 11 | As an authenticated user, I can create a profile with information about each of my cats, so that I can get personalised service from the cat sitter. | HIGH |
| 12 | As an authenticated user, I can edit/update information about each cat in my profile, so that I can receive accurate services for my cats. | HIGH |
| 13 | As an authenticated user, I can delete a cat from my profile, so that I can remove a cat that is no longer in need of cat-sitting services. | HIGH |
| 14 | As an authenticated user, I can receive a notification confirming if I've added, edited or deleted a cat profile so that I can keep track of my cat profiles. | MEDIUM |
| 15 | As the site owner, I can access the admin panel as a superuser, so that I can view and manage user profiles when required. | HIGH |
| 16 | As a new user, I can register my profile using my social media accounts so that I can verify my credentials faster. | LOW |
|  | **BOOKING AND CHECKOUT** |  |
| 17 | As an authenticated user, I can easily make a booking using a form, so that I can schedule cat-sitting services with Purrfect Sitters. | HIGH |
| 18 | As an authenticated user, I can easily enter my payment information, so that I can check out quickly and with no hassles. | HIGH |
| 19 | As a site owner, I want to collect payment for sittings so I do not have to deal with checks or cash collections for my services. | HIGH |
| 20 | As a site user, I want to pay for my bookings in a secure manner online so I don’t have my personal information stolen. | HIGH |
| 21 | As a site owner, I can charge a customer an extra fee if they have more than three cats, so that I can be prepared for the additional care required during a visit. | HIGH |
| 22 | As an authenticated user, I can view my previous bookings, so that I can see how often I've used the service in the past and which service level I chose. | MEDIUM |
| 23 | As an authenticated user, I can update my existing booking, so that I can make changes to my cat-sitting services if needed. | MEDIUM |
| 24 | As an authenticated user, I can delete a booking, so that I can cancel my cat-sitting services if needed. | MEDIUM |
| 25 | As an authenticated user, I can receive an email confirming if I've edited or deleted my booking so that I can keep track of my cat-sitting services. | MEDIUM |
| 26 | As an authenticated user, I can receive an email after a successful payment, so that I can keep the confirmation of what I've booked for my records. | MEDIUM |
| 27 | As a site user, I want to pay for my bookings in a secure manner online so I don’t have my personal information stolen. | HIGH |

#### Database Schema

<img width="489" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/afbea4c5-1f02-44d7-a0bc-160975ffa296">

* A relational database was designed and the data is represented above in an ERD with four custom models.
* The checkout model was based off Boutique Ado walkthrough project with some adjustments.
* The number of cats per profile is connected to the owner.
* The Cat model is built to have full CRUD functionalities.
* The Booking model will be implemented with full CRUD in the next interation due to time contraints and therefore will be a future feature.
* The Service model will add the ability to add, update, delete and edit package information from the frontend in a future implementation.

##### Booking
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/126bbcbf-3db3-4ac2-98ae-e8bf19163749)


- [X] C - Customers can create a booking through the site when logged in via a form.
- [ ] R - Future feature, users will receive an email with a summary of their booking. This is top priority for the next sprint.
- [ ] U - Future feature, users can contact Purrfect Pets to update their booking for now.
- [ ] D - Future feature, users can contact Purrfect Pets to delete their booking for now.

##### Cat
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/4f775f4f-9df9-49d4-885a-2f86fcf74922)

- [X] C - Customers can sign up and register a profile thanks to Django allauth system. 
- [X] R - Customers can see a list of their cats added to their profile and click for further information.
- [X] U - Customers can update their cat detail cards if needed.
- [X] D - Customers can delete a cat if they no longer need future cat sitting services for that pet.

##### Service
<img width="277" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/35e58951-bdc2-4b9a-ad54-e9ecd32b3cac">

- [ ] C - This is a static model, future feature will allow creation of packages via a managmement panel.
- [X] R - Customers can view the packages on offer via the service page.
- [ ] U - Creation of a management panel on the frontend in a future iteration can allow for this.
- [ ] D - Deletion of packages is managed via the admin panel for now.

##### Checkout
<img width="277" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/35e58951-bdc2-4b9a-ad54-e9ecd32b3cac">

- [X] C - Customers can create a new payment once they've made a booking. 
- [ ] R - Customers will be able to view a booking summary and payment information in a future implementation.
- [ ] U - The user is unable to edit their checkout once processed.
- [ ] D - The user will be able to delete their booking and request a refund in a later interation.

### Skeleton
#### Wireframes

##### Landing Page 
- The landing page was designed to have a clear and easy to navigate layout, with a drop down for login/logout and profile information access.
- The customer can immediately see what the page is about with the page name and description.
- There is a clear call to action button to book.

<img width="916" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/31803c0c-3319-417d-96ed-75e5be05f128">

##### Services Page
- The page is to summarises the services offered including name, time and price with a call to action button.
- There is an FAQ section for new or returning users to refer to if needed. Designed using Bootstrap accordian feature.

<img width="566" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/b8dc6b4f-dc68-4052-95ac-d0222487f34a">

##### Account Page
- The django allauth system provided all the login/logout and registration functionalities for the page
- The templates were styled in some areas to account for the brand look and feel.

<img width="832" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/83d9ddab-8c6b-45da-a9e7-5638764526a1">
<img width="415" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/9c6f36f0-39d7-4965-92b8-58a61203a972">

##### Cat Profile Page
- The users can view a list of their cats in easy to read cards using Bootstrap to achieve this.
- If they do not have cats, a message will be displayed accordingly.
- Functionalities to edit and delete cat profiles from the front-end to increase user experience.

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

- The logo was custom designed myself using Canva.
- The cat icon in the center was found using creative commons search.

#### Colors
![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/7c482dfc-a4c1-4b45-b73d-b070970c96a6)
 
- The dark grey colour #2a2727 was chosen and paired with white to ensure high contrast whilst keeping with a black cat theme.
- The header and footer have a clear delineation from the body content. 

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
- The website was designed mobile-first using Bootstrap grid and flexbox to ensure responsiveness throughout the website.
- Limited media queries required with some adjustments for extra large screens.

## Features

### Navigation
- The users will have a choice of home, login/logout & register when visiting the site. 
- For mobile devices, the navigation toggles to a hamburger menu.
- The user name is displayed when logged in and a drop down is displayed for my profile and logout buttons.
- The navigation is personalised to the logged-in user by displaying their username. 

### Register 
- The user will be able to easily sign up for an account which includes an email confirmation feature for added security. 
- If users are already registered, there is a link to easily navigate to login instead.

### Login/Logout 
- The users can easily sign in using the below form with an option to 'remember me' if desired.
- For any user accessing a page which requires an account, they will be directed to the sign up page.

### Footer
- The footer links directly to the social media pages of the plant care blog using ```rel="noopener noreferrer"``` attributes.
- There is a subtle hover state on each icon for better user experience.
- All users are able to access the contact information of the service via the footer.
- There is a small description of the page which summarises the page intent.
- If users wish to sign up to a newsletter, they can do so easily by inputting their email address. 

### Error 400/404/403/500
- There are error pages in place in case a user is taken to a restricted area or the page doesn't exist.
- The customised pages give information about the error and next steps to take.

### Services Page
- Both new and registered users can see the current packages on offer with a name, price and description.
- This is updated via the admin panel, with future plans to create a management dashboard on the front-end.

### Cat Profile Page
- If a user has registered a profile, they can add a cat and complete information about their pet for the cat sitter using a form.
- For users who don't have any cats, a helpful message will guide them to add one.
- This profile is displayed alongside other cats on the user profile in a stacked card format using Bootstrap cards.
- Each action taken on a cat profile is notified using Bootstrap Toasts.

### Cat Detail Pages
- If a user has registered a profile and have loaded cats onto their profile, they can click on the card to see additional information.
- The user is able to read the additional information they added about their cat and can edit/update the information via a form.
- This form allows for the original photo of the cat to be kept.
- If the user would like to delete their cat, they can do so via this page with a warning to prompt them before hand.

### Bookings Page
- The user has multiple access points to the booking form including via the navigation, landing page and my profile page when viewing cats.
- If not logged in, they'll be directed to the login page.
- The form has checks in place for double booking dates, dates booked in the past and for phone number formatting.
- Thanks to crispy forms, input validation is present for required fields and toasts will update the user if the booking went through.

### Future Features
- This is a project with a lot of potential and due to the time constraints of the current implementation, I am very excited to be able to roll-out the below future features in the next sprint:

|  | FEATURE | PRIORITY |
|---|---|---|
| 1 | Creating webhooks for a more robust payment system. Due to ongoing errors this was not able to be implemented. | HIGH |
| 2 | Being able to add full CRUD to bookings will ensure a smoother user experience and an easier management for the site owner. | HIGH |
| 3 | Allowing reviews of the service can increase interaction with customer to brand and can be helpful in converting new customers who visit the site. | MEDIUM |
| 4 | Creation of optional registration/sign-in using social media accounts would improve user experience and increase trust of the brand | MEDIUM |
| 5 | Instead of deleting a cat, a softer feature can allow for users to 'check' a cat for booking in the event a pet is deceased. | LOW |
| 6 | Building an management dashboard for the owner on the front-end to easily manage bookings and payments | MEDIUM |

## Web Marketing Strategies
- The following strategies for Purrfect Sitters have been considered and a combination of strategies can be implemented as the company grows.
- For an online service, word of mouth will be the strongest tool alongside online support as described below.

### SEO
- The content of the website was written using a combination of short-tail and long-tail keywords without the use of keyword stuffing as a bad practice.
- The website was designed to extend additional meta descriptions and keywords as the site grows.
- For now, the home and services page are SEO optimised which can be reworked if Google Adwords are implemented at a later stage.
- There is a robots.txt and site-map.xml for search engine crawlers and proper indexing.   

### Content Marketing
- The nature of the business allows for fun, engaging and a variety of content types. 
- There is a lot of opportunity to grow a community of cat lovers via social media and the newsletter. 
- This business will benefit the most from word-of-mouth and testimonials which will be a key content pillar for social.

#### Email Marketing

![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/acf516c5-22f7-4c49-8f2e-7782cb1c541d)

- The newsletter can allow more detail and article type content to be delivered to those who opt-in. 
- This can be begin as a monthly update and can increase to weekly once a larger audence is established.
- The social media pages can be used as a guide to what conent is interesting to followers. 
- Testing of approaches can be easily done to see which content generates referrals and sales. 
- If there are competitions, offers or information accounements this channel can assist in information sharing with customers.

#### Social Media Marketing
- The Facebook Business page for Purrfect Sitters will be setup as an initial entry into the social media marketing space. 
- It would be benefical to setup an Instagram page which can link with Facebook and allow for more engagement with the target market.
- The content would be a combination of light-hearted cat humour, educational anecdotes about cats, and brand information.
- This can allow for links to the website content, directing web traffic to the Purrfect Sitters website. 
- It can also drive traffic to the newsletter to share more long form content. 
- Brand campaigns can be developed e.g. interviewing customers and getting testimonials in written or video format. 
- Paid Instagram and Facebook ads can be used as a driver to the webiste.

<img width="392" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/99878dcc-fe87-4394-b36d-451797bc081f">

### Paid Advertising
- For the size of this business, it would be beneficial to look at how social media advertising can drive traffic to the website with engaging content that is relatable to the customer. 

## Technologies
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
- Canva
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

## Credits
- The Code Institute 'Boutique Ado' walkthrough project assisted and guided in the setup and basic structure of this project.
- Seaside Sewing by Kera Kudmore was a great source of inspiration and best practice regarding testing and README structure.
- Escape Room by Freddie Boys helped to understand the code logic for a service based website and was a great reference point.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The website content was written myself.

### Media
- The fonts were sourced using [Google Fonts](https://fonts.google.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).
- The ERD was created with [draw.io](https://www.drawio.com/).

## Acknowledgements
- Thank you to my mentor Malia for continuous helpful feedback and support throughout the project.
- I greatly appreciate the tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
