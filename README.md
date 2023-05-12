# Purrfect Sitters - Cat Sitting Service 

## Author
Cara McAvinchey 

## Project Overview
*  XX
* You can view the deployed website [here](#).

(image)

## UX

### Project Goal
* The aim of the project is to provide easily digestible information about popular house plants for beginners and to allow for conversation and sharing of experiences in taking care of them.

### User Stories
(table) 

## DATA MODEL
<img width="484" alt="image" src="https://user-images.githubusercontent.com/97494262/209538748-6f3cdc41-16c5-43ab-94a8-2341239ffc78.png">

- [X] C - Site users can create/register their own profile to interact with the plant posts.
- [X] R - Site users can open and read the plant blog posts and read comments from other users.
- [X] U - Site users can like a post, updating the details and analytics for a plant detail post.
- [X] D - Site users can eliminate their like if desired on a plant detail post.

<img width="477" alt="image" src="https://user-images.githubusercontent.com/97494262/209538824-f613791d-53b6-43e4-a305-f14a52026443.png">

- [X] C - Site users can create their own comments using a form on each blog post.
- [X] R - Site users can read comments from other users.
- [X] U - Site users are able to update/edit their comments using a form.
- [X] D - Site users are able to delete their comments.

## WIREFRAMES

### Landing Page 
(screenshot)
- XX
- XX

### Services Page
(screenshot)
- XX
- XX

### Account Page
(screenshot)
- XX
- XX

### Cat Profile Page
(screenshot)
- XX
- XX

### Bookings Page
(screenshot)
- XX
- XX

## DESIGN CHOICES (UI)

### Colors
(colour palette)
 
- The natural color palette links to the theme of plants and plant care. 
- The headings, icons and body text are darker to ensure clear contrast and readability for the user across the site.
- The green header and footer ensures clear contrast and delineation between sections.
- Due to the lighthouse score for accessibility, the background color for the header and footer was adjusted:

### Typography
(font pairing)

- The font combination was chosen using guidance article from Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The logo and headings use Amatic SC with a fallback of cursive and the body text uses Roboto Condensed with a fallback of san-serif.
- The choice of fonts were selected and installed using [Google Fonts](https://fonts.google.com/).

### Images/Icons
(choices of imagery)

- The icons were chosen to provide clear understanding of each plant and its care requirements.
- Each summary card has the same information structure with all icons standard throughout the site.

### Animations
- The navbar, social icons and buttons across the site have a subtle grow effect when hovered over by the user.
- All links have a color change and underlined effect when hovered for clear distinction from the body text.

### Responsiveness
- The website was designed mobile-first using flexbox to ensure responsiveness throughout the website.
- The standard grid from Bootstrap was used to achieve this.

## FEATURES/STRUCTURE

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

### Features for Future Development
- It will become less efficient for the user to scroll through many posts in the list view so a search bar will allow users to find specific plants they want to read more about.
- It would increase user experience to add a method to 'save' blog posts so users can keep their favourite plants in one place.
- To increase user interactivity from readers, users could rate blog posts on how helpful the information was and give feedback.
- Pending comments can be added so users are aware they are awaiting approval. 

## TESTING

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

### Validation Testing
- HTML
   - No errors were returned when passing through the official [HTML validator]("#").

(screenshots of each page)

- CSS
   - No errors were found when passing through the [CSS validator]("#").

(screenshots of each page)

- JavaScript
   - No errors were found when passing through the [JS validator]("#").

(screenshots of each page)

### Visual (UI) Testing: Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers.

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** |
|-----------------------------|------------------|---------|------------------|
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |
| dev tools: Pixel 2          | Chrome           | android | 411 x 731        |
| real phone: iPhone XR       | safari           | iOs     | 414 x 896 px     |
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |
| browserstack: iPhone 13 Pro | safari           | iOs     | 390px × 844px    |
| real tablet: iPad Pro 11    | Chrome           | iOs     | 834 x 1075 px    |
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |
| browserstack                | Edge 99          | windows | 1440 x 672 px    |

### Manual Testing
- You can view manual testing of the website [here](https://docs.google.com/spreadsheets/d/123Pia98Ms_Fe6at0hPnAWhcNrmeVc4X2RLYmD7VsqX4/edit?usp=sharing).

### Automatic Testing
- Manual testing was done due to time constraints.

## Performance Testing
(screenshot)
- XX

## Accessibility Testing

### WAVE Web Accessibility Evaluation Tool
(screenshot)
- XX

### Lighthouse Audit
- The deployed website was run through lighthouse to check performance, accessibility, best practices and SEO scores.

### Keyboard Navigation
- The users will be able to use the tab button to navigate the website if required.

### Outstanding Defects
- XX

### Defects of Note
- XX

## TECHNOLOGIES USED
- GitPod
- GitHub
- Django
- Bootstrap
- AWS S3
- Summernote
- Crispy Forms
- Heroku
- Balsamiq
- Fontawesome

## DEPLOYMENT
**Step 1:** Create a new app in Heroku, choose a unique name and region.
**Step 2:** Login to ElephantSQL, access the dashboard and create a new instance (input a name, select a region).
**Step 3:** Return to dashboard, copy the database URL:
<img width="800" alt="image" src="https://user-images.githubusercontent.com/97494262/209531384-85d95cc3-a381-4c3c-b56f-215238e0daf8.png">

**Step 4:** Create env.py file (ensure it is included in .gitignore file) and add environment the below variables. Paste the URL from above:

<img width="372" alt="image" src="https://user-images.githubusercontent.com/97494262/209531222-599282ee-2c54-490f-b543-1f09e5255490.png">

**Step 5:** Include a secret key in the variables:

<img width="800" alt="Screenshot 2022-12-26 at 11 25 13" src="https://user-images.githubusercontent.com/97494262/209531979-9ba177cc-3e44-48a7-80dc-884d06932f54.png">

**Step 6:** Include the below code to settings.py file:

<img width="301" alt="image" src="https://user-images.githubusercontent.com/97494262/209532128-acaa1e29-edea-45c3-93ce-2caaf0f71862.png">

**Step 7:** Link the database in settings.py and migrate then push to GitHub:

<img width="303" alt="image" src="https://user-images.githubusercontent.com/97494262/209532393-5283592f-5caf-4e81-b3fd-9d20bd62b111.png">

**Step 8:** In Heroku, add three config vars:

<img width="243" alt="image" src="https://user-images.githubusercontent.com/97494262/209532605-04bff00b-951f-4084-9ad5-6eff111ac6bf.png">

<img width="350" alt="image" src="https://user-images.githubusercontent.com/97494262/209532533-e9b3d879-a40a-4335-a56b-3c0e5c370a8a.png">

**Step 9:** Login to Cloudinary, copy the API Environmental variable to dashboard and add to env.py (see screenshot above) & to Heroku config vars:

<img width="571" alt="image" src="https://user-images.githubusercontent.com/97494262/209533286-4a79143c-6568-4055-99fc-76dd5821a02b.png">

**Step 10:** Add cloudinary to installed apps in settings.py, add static/media file settings:

<img width="407" alt="image" src="https://user-images.githubusercontent.com/97494262/209533445-8f6670c5-490b-4294-95cf-febaaaed2ab2.png">

<img width="500" alt="image" src="https://user-images.githubusercontent.com/97494262/209533629-ab3fb31b-f096-4305-996e-970e4c950a3f.png">

**Step 11:** Add template directories in settings.py, add Heroku host name to allowed hosts and add directory files:

<img width="600" alt="image" src="https://user-images.githubusercontent.com/97494262/209533879-b8284837-e7a1-4315-83e6-9b88d2125882.png">

<img width="501" alt="image" src="https://user-images.githubusercontent.com/97494262/209534100-46723f98-7bd6-40ed-91c1-5226ad6e950d.png">

<img width="313" alt="image" src="https://user-images.githubusercontent.com/97494262/209534271-772afed4-f299-45dc-b72d-d0843b7ad189.png">

**Step 12:** Create a Procfile, then commit and push to GitHub:

<img width="504" alt="image" src="https://user-images.githubusercontent.com/97494262/209534389-5b0cdd3c-54f7-44e8-8a21-99068431365a.png">

**Step 13:** Connect GitHub account in Heroku, connect and deploy branch. Open app and check:

<img width="421" alt="image" src="https://user-images.githubusercontent.com/97494262/209534580-c03fa4fd-8e52-487b-8ecc-23563fd30327.png">

## CREDITS
- The Code Institute 'I Think, Therefore I Blog' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Stockbook Project by Massimo Ranalli assisted with the setup of the edit/delete functions for comments as well as the messaging alerts.
- Code Institute Student Template: [gitpod full template](https://github.com/Code-Institute-Org/gitpod-full-template).
- The articles on the blog were written myself and any additional helpful articles were linked to for the user to access for more information.

### Media
- The fonts were chosen with guidance from an article written by Mai Knoblovits [here](https://artisanthemes.io/great-google-font-combinations-ready-use/).
- The colors for the website was generated using [Color Space]([https://coolors.co/image-picker](https://mycolor.space/?hex=%2333C883&sub=1)).
- The plant images were sourced using [Pexels](https://www.pexels.com) and [Pixabay](https://pixabay.com/).
- The icons for the favicon, footer, about page and location headings were taken from [Font Awesome](https://fontawesome.com/).
- The favicon image was converted using [Favicon.io](https://favicon.io/).

## ACKNOWLEDGEMENTS
- Thank you to my mentor for continuous helpful feedback and support throughout the project.
- The tutors at Code Institute for their patience and support.
- The Code Institute Slack community for tips and guidance.

[Back to the beginning](#table-of-contents)
