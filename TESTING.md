# Purrfect Sitters - Testing Documentation

![241733671-d696328a-dc32-434a-9083-ba7c8d9e99ab](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/069a88aa-b43d-4e61-a5b5-57a3cef85e77)

## Contents
- [Validation Testing](#validation-testing)
  * [CSS](#css)
  * [JavaScript](#javascript)
  * [Python](#python)
- [Visual (UI) Testing: Cross Browser and Cross Device Testing](#visual--ui--testing--cross-browser-and-cross-device-testing)
- [Lighthouse](#lighthouse)
    + [Desktop Results](#desktop-results)
    + [Mobile Results](#mobile-results)
  * [Wave](#wave)
- [Automatic Testing](#automatic-testing)
- [Manual Testing](#manual-testing)
  * [Testing User Stories](#testing-user-stories)
- [Outstanding Defects](#outstanding-defects)
- [Defects of Note](#defects-of-note)

## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator. You can click each page to see the corresponding screenshot evidence.

| Page | Result |
| :--- | :--- |
| [Home Page](documentation/testing/html/home-page-html.jpg) | Pass |
| [Service Page](documentation/testing/html/service-page-html.jpg) | Pass |
| [Cat Profile](documentation/testing/html/cat-profile-page-html.jpg) | Pass |
| [Cat Detail](documentation/testing/html/cat-detail-page-html.jpg)| Pass |
| [Edit Cat Page](documentation/testing/html/edit-cat-page-html.jpg) | Pass |
| [Delete Cat Page](documentation/testing/html/delete-cat-page-html.jpg) | Pass |
| [Booking Page](documentation/testing/html/booking-page-html.jpg) | Fail |
| [My Bookings](documentation/testing/html/my-booking-page-html.jpg) | Pass |
| [Checkout Page](documentation/testing/html/checkout-html.jpg) | Pass |
| [Checkout Success Page](documentation/testing/html/checkout-success-html.jpg) | Pass |
| [Error 404](documentation/testing/html/error404-page-html.jpg) | Pass |

**Please note:**
- The screenshots will show two warnings which I chose to ignore, both concerning the "type" attribute is unnecessary for JavaScript resources. Because these scripts concern my AWS S3 and I had a lot of difficulty getting my static files to load, didn't want to risk any issues on my deployed site. 

**Booking:**
- The booking page did not pass validation and raised two errors with can be seen [here](documentation/testing/html/booking-html-error-max.jpg) and [here](documentation/testing/html/booking-html-error-min.jpg) which were a result of the Django date picker widget including min and max value attributes in the input tag.
- You can find a detailed write up [here](#outstanding-defects)

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS. You can click each page to see the corresponding screenshot evidence.

| File | Result | 
| :--- | :--- |
| [static/base.css](documentation/testing/css/base-css.jpg) | Pass |
| [checkout/static/checkout.css](documentation/testing/css/checkout-css.jpg) | Pass |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result |
| :--- | :--- |
| [checkout/static/stripe_elements.js](documentation/testing/js/js-hint-stripe.jpg) | Pass |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

| File | Result | Evidence |
| :--- | :--- | :---: |
| [custom_storages.py](documentation/testing/python/custom-storages.jpg)  | Pass | 
| **PURRFECT SITTERS** |
| [purrfect_sitters/urls.py](documentation/testing/python/purrfectsitters-urls.jpg) | Pass |  
| **HOME** |
| [home/views.py](documentation/testing/python/home-views.jpg) | Pass | 
| [home/urls.py](documentation/testing/python/home-urls.jpg) | Pass | 
| **SERVICES** |
| [service/models.py](documentation/testing/python/service-models.jpg) | Pass | 
| [service/views.py](documentation/testing/python/service-views.jpg) | Pass | 
| [service/admin.py](documentation/testing/python/service-admin.jpg) | Pass | 
| [vservice/urls.py](documentation/testing/python/service-urls.jpg) | Pass |  
| **CAT** |
| [cat/models.py](documentation/testing/python/cat-models.jpg) | Pass | 
| [cat/views.py](documentation/testing/python/cat-views.jpg) | Pass | 
| [cat/urls.py](documentation/testing/python/cat-urls.jpg) | Pass | 
| [cat/admin.py](documentation/testing/python/cat-admin.jpg) | Pass | 
| [cat/forms.py](documentation/testing/python/cat-form.jpg) | Pass | 
| **BOOKING** |
| [booking/models.py](documentation/testing/python/booking-models.jpg) | Pass | 
| [booking/views.py](documentation/testing/python/booking-views.jpg) | Pass | 
| [booking/urls.py](documentation/testing/python/booking-urls.jpg) | Pass | |
| [booking/admin.py](documentation/testing/python/booking-admin.jpg) | Pass | 
| [booking/forms.py](documentation/testing/python/booking-forms.jpg) | Pass | 

## Visual (UI) Testing: Cross Browser and Cross Device Testing
- The below combination of devices, browsers, and operating system were used to test the website. A range of viewport sizes were checked to see if users would have the same experience across multiple devices and browsers. Priority was given to mobile devices and tablets. 

| **TOOL / Device**           | **BROWSER**      | **OS**  | **SCREEN WIDTH** | Passed 
|-----------------------------|------------------|---------|------------------|---------
| dev tools: Galaxy Fold      | Chrome           | android | 280 x 653 px     |Yes
| dev tools: iPhone SE        | safari           | iOs     | 375 x 667 px     |Yes
| dev tools: Samsung S8+      | Chrome           | android | 360 x 740 px     |Yes
| real phone: Pixel 6         | Chrome           | android | 393 x 851 px     |Yes
| real phone: iPhone 14 Pro   | safari           | iOs     | 390 x 844 px     |Yes
| browserstack: Nexus 7       | Firefox          | android | 960 x 600 px     |Yes
| real tablet: Pixel Tablet   | Chrome           | android | 834 x 1075 px    |Yes
| real laptop: Macbook Pro    | Firefox & Chrome | iOs     | 1400 x 766 px    |Yes
| broswerstack                | Firefox          | iOs     | 1440 x 672 px    |Yes
| browserstack                | Edge 113         | windows | 1440 x 672 px    |Yes

## Lighthouse

For the performance, accessibility, best practices and SEO of the site for mobile and desktop, [Page Speed](https://pagespeed.web.dev/) and the major pages were passed through the validation. 

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing]() |
| Service Page | ![Service Desktop Lighthouse Testing]() |
| Cat Profile | ![Cat Profile Desktop Lighthouse Testing]() |
| Booking | ![Products Desktop Lighthouse Testing]() |
| Checkout | ![Products Desktop Lighthouse Testing]() |

- Desktop performed well on all major pages of the site with minimal improvements needed.

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Page Mobile Lighthouse Testing](![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/3f6e7683-ab77-4ac4-be30-ba032f97999a)) |
| Service Page | ![Service Desktop Lighthouse Testing](![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ca279d62-faca-400f-8f4c-a1acdcf2770b)) |
| Cat Profile | ![Cat Profile Desktop Lighthouse Testing](![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/73b6a7fc-dfd1-4495-ae10-dd2289de1825)) |
| Booking | ![Products Desktop Lighthouse Testing](![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/34339825-73d0-472e-b55b-9f9e12cb9c8b)) |
| Checkout | ![Products Desktop Lighthouse Testing](![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/ef87ed91-7e76-41a1-848f-b7f0eafc8f8b)) |

- Mobile performance can improve, where performance was slowed in first contentful paint and largest contentful paint metrics.
- This is a result of render-blocking resources mostly from Bootstrap and AWS which requires further investigation to resolve.

![image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/38e7a58e-e690-440a-8a8a-fc6015dbcc87)


### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors. The following pages were tested:

| Page | Errors |
| :--- | :--- |
| Home Page | 1 error|
| Service Page | No errors |
| Cat Profile | No errors |
| Cat Detail| No errors |
| Add Cat | No errors |
| Edit Cat| No errors |
| Booking | No errors |
| Checkout | No errors |

- Below highlights one error which is rooted in the footer caused by a missing form label in the embedded MailChimp newsletter code. This isn't for the input field that the user sees but a hidden field included in the code to prevent spam bots. No changes made to this as to not risk it's functionalities.

<img width="1437" alt="wave-home" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/65355df7-62dd-46ae-a596-9586de536eec">

<img width="575" alt="image" src="https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/e86ff1a7-aad4-4bd3-8db9-88d54d97a3c3">

- This error therefore is present on all pages but is recorded above on the home page and to confirm every other page doesn't have additional errors over and above the one mentioned.

## Automated Testing
- Manual testing was done due to time constraints.
- Testing of each app views will be done using Django unittest module in the next iteration.
- I am keen to investigate HTTP-level request handling, form validation and processing and template rendering using automated tests.
- This is a great area of interest to me, and I was disappointed to not have been able to implement these in time.

## Manual Testing

### Testing User Stories
- Each completed user story on the [sprint backlog](https://github.com/users/CaraMcAvinchey/projects/5) was tested against the acceptance criteria, see the corresponding screenshots as evidence.
- This included reviewing each feature to check the usability, visual design and performance.

|  | USER STORY | TEST CASE | RESULT |
|---|---|---|---|
|  | As a user, I can view the landing page so that I can find key information about the company and it's services. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/30 | PASS |
|  | As a user, I can view the packages offered by Purrfect Sitters, so that I can learn more about the service in detail. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/31 | PASS |
|  | As a new user, I can easily find the contact information of Purrfect Sitters, so that I can reach out to them for more information. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/32 | PASS |
|  | As a user, I can easily connect with the social media accounts of Purrfect Sitters, so that I can learn more about the activities of the brand. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/33 | PASS |
|  | As a user, I can sign up to receive a newsletter from Purrfect Pets, so that I can get updates about the company and its services. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/34 | PASS |
|  | As a new or authenticated user, I can be notified once completing an important action on the website, so I know what I was last doing. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/35 | PASS |
|  | As a new user, I can safely register for an account with an email and password, so that I can book cat-sitting services with Purrfect Sitters. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/36 | PASS |
|  | As an authenticated user, I can view my profile information when logged in, so that I can ensure it is complete and up-to-date. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/37 | PASS |
|  | As a user, I can safely login and logout of my account so that I can keep my information private. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/35 | PASS |
|  | As an authenticated user, I can create a profile with information about each of my cats, so that I can get personalised service from the cat sitter. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/38 | PASS |
|  | As an authenticated user, I can edit/update information about each cat in my profile, so that I can receive accurate services for my cats. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/39 | PASS |
|  | As an authenticated user, I can delete a cat from my profile, so that I can remove a cat that is no longer in need of cat-sitting services. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/40 | PASS |
|  | As an authenticated user, I can receive a notification confirming if I've added, edited or deleted a cat profile so that I can keep track of my cat profiles. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/41 | PASS |
|  | As the site owner, I can access the admin panel as a superuser, so that I can view and manage user profiles when required. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/42 | PASS |
|  | As an authenticated user, I can easily make a booking using a form, so that I can schedule cat-sitting services with Purrfect Sitters. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/43 | PASS |
|  | As an authenticated user, I can easily enter my payment information, so that I can check out quickly and with no hassles. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/44 | PASS |
|  | As a site owner, I want to collect payment for sittings so I do not have to deal with checks or cash collections for my services. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/45 | PASS |
|  | As a site user, I want to pay for my bookings in a secure manner online so I don’t have my personal information stolen. | https://github.com/CaraMcAvinchey/purrfect-sitters/issues/44 | PASS |

## Outstanding Defects
- The following outstanding defects are listed below and are ongoing, with steps of how these issues were investigated and dealt with thus far:

**Booking**
- The booking page did not pass html validation and raised two errors with can be seen [here](documentation/testing/html/booking-html-error-max.jpg) and [here](documentation/testing/html/booking-html-error-min.jpg) which were a result of the Django date picker widget including min and max value attributes in the input tag.
- To fix this error the SelectDateWidget was investigated as an alternative: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/.
- However, this altered the structure of the form to a less user friendly structure rendering an additonal three fields (one for day, one for month, one for year) which wasn't visually pleasing compared to the calender form and added increased the time to make a booking.
- For the sake of user experience, and concern that the new format would distrupt the passing of data between views, this issue is ongoing and a solution was not found prior to the hand in date. 

## Defects of Note
- XX

[Back to the beginning](#table-of-contents)
