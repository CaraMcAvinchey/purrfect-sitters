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
- [Usability Testing](#usability-testing)
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
| [My Bookings](documentation/testing/html/home-page.jpg) | Pass |
| [Checkout Page](documentation/testing/html/home-page.jpg) | Pass |
| [Checkout Success Page](documentation/testing/html/home-page.jpg) | Pass |
| [Error 404](documentation/testing/html/home-page.jpg) | Pass |

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
| custom_storages.py | Pass | [validation](documentation/testing/python/custom-storages.jpg) |
| **PURRFECT SITTERS** |
| purrfect_sitters/urls.py | Pass | [validation](documentation/testing/python/purrfectsitters-urls.jpg) |
| **HOME** |
| home/views.py | Pass | [validation](documentation/testing/python/home-views.jpg) |
| home/urls.py | Pass | [validation](documentation/testing/python/home-urls.jpg) |
| **SERVICES** |
| service/models.py | Pass | [validation](documentation/testing/python/service-models.jpg) |
| service/views.py | Pass | [validation](documentation/testing/python/service-views.jpg) |
| service/admin.py | Pass | [validation](documentation/testing/python/service-admin.jpg) |
| service/urls.py | Pass | [validation](documentation/testing/python/service-urls.jpg) |
| **CAT** |
| cat/models.py | Pass | [validation](documentation/testing/python/cat-models.jpg) |
| cat/views.py | Pass | [validation](documentation/testing/python/cat-views.jpg)|
| cat/urls.py | Pass | [validation](documentation/testing/python/cat-urls.jpg)|
| cat/admin.py | Pass | [validation](documentation/testing/python/cat-admin.jpg)|
| cat/forms.py | Pass | [validation](documentation/testing/python/cat-form.jpg)|
| **BOOKING** |
| booking/models.py | Pass | [validation](documentation/testing/python/booking-models.jpg) |
| booking/views.py | Pass | [validation](documentation/testing/python/booking-views.jpg)|
| booking/urls.py | Pass | [validation](documentation/testing/python/booking-urls.jpg)|
| booking/admin.py | Pass | [validation](documentation/testing/python/booking-admin.jpg)|
| booking/forms.py | Pass | [validation](documentation/testing/python/booking-forms.jpg)|

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
| browserstack                | Edge 99          | windows | 1440 x 672 px    |Yes

## Lighthouse

I have used Googles Lighthouse testing to test the performance, accessibility, best practices and SEO of the site.

#### Desktop Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Desktop Lighthouse Testing](#) |
| Products Page | ![Products Desktop Lighthouse Testing](#) |

#### Mobile Results

| Page | Result |
| :--- | :--- |
| Home Page | ![Home Page Mobile Lighthouse Testing](#) |
| Products Page | ![Product Mobile Lighthouse Testing](#) |

### Wave

WAVE(Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

| Page | Errors |
| :--- | :--- |
| Home Page | No errors|
| Products Page | No errors |
| Product Details Page | No errors |
| Add Product Page | No errors |
| Edit Product Page | No errors |
| Bag Page | No errors |
| Checkout Page | No errors |
| Checkout Success Page | No errors |
| Profile Page |No errors. |
| Contact Us Page | No errors |
| Privacy Policy Page| No errors |
| Terms & Conditions Page | No errors |
| Delivery Policy Page | No errors |
| 404 Error Page | No errors |

## Automated Testing
- Manual testing was done due to time constraints.
- Testing of each app views will be done using Django unittest module in the next iteration.
- I am keen to investigate HTTP-level request handling, form validation and processing and template rendering using automated tests.
- This is a great area of interest to me, and I was disappointed to not have been able to implement these in time.

## Manual Testing

### Testing User Stories
 User Story ID | As a/an | I want to be able to ... | So that I can... | How is this achieved? | Evidence |
| :--- | :--- | :--- | :---| :--- | :---: |
| **VIEWING & NAVIGATION** |
| 1 | User | XX | XX | XX | [1](#) & [2](#) |
| 2 | User | XX | XX | XX | [1](#) & [2](#) |
| 3 | User | XX | XX | XX | [1](#) & [2](#) |
| 4 | User | XX | XX | XX | [1](#) & [2](#) |

## Usability Testing
- You can view manual testing of the website [here](#).

## Outstanding Defects
- The following outstanding defects are listed below and are ongoing, with steps of how these issues were investigated and dealt with thus far:

**Booking**
- The booking page did not pass validation and raised two errors with can be seen [here](documentation/testing/html/booking-html-error-max.jpg) and [here](documentation/testing/html/booking-html-error-min.jpg) which were a result of the Django date picker widget including min and max value attributes in the input tag.
- To fix this error the SelectDateWidget was investigated as an alternative: https://docs.djangoproject.com/en/4.2/ref/forms/widgets/.
- However, this altered the structure of the form to a less user friendly structure rendering an additonal three fields (one for day, one for month, one for year) which wasn't visually pleasing compared to the calender form and added increased the time to make a booking.
- For the sake of user experience, and concern that the new format would distrupt the passing of data between views, this issue is ongoing and a solution was not found prior to the hand in date. 

## Defects of Note
- XX

[Back to the beginning](#table-of-contents)
