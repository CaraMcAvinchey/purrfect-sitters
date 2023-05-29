# Purrfect Sitters - Testing Documentation

[image](https://github.com/CaraMcAvinchey/purrfect-sitters/assets/97494262/d696328a-dc32-434a-9083-ba7c8d9e99ab)

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
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass | [Home Page](#) |
| Services | Pass | [Service Page](#) |
| Cat Profile | Pass | [Cat Profile](#) |
| Cat Detail| Pass | [Cat Detail](#) |
| Edit Cat | Pass | [Edit Cat Page](#)|
| Delete Cat | Pass | [Delete Cat Page](#) |
| Booking | Fail |[Booking Page](#) |
| My Bookings | Pass | [My Bookings](#) |
| Checkout | Pass | [Checkout Page](#) |
| Checkout Success | Fail | [Checkout Success Page](#) |
| 404 Error | Pass | [Checkout Page](#) |

**Please note:**
The screenshots will show two warnings which I chose to ignore, both concerning the "type" attribute is unnecessary for JavaScript resources. Because these scripts concern my AWS S3 and I had a lot of difficulty getting my static files to load, didn't want to risk any issues on my deployed site. 

### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS.

| File | Result | Evidence |
| :--- | :--- | :---: |
| static/base.css | Pass | [static/base.css validation](#) |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File | Result | Evidence |
| :--- | :--- | :---: |
| checkout/static/checkout/js/stripe-elements.js | Pass | [stripe-elements.js](#) |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python. I have also installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE to enable me to check my code meets PEP8 guidelines during development.

| File | Result | Evidence |
| :--- | :--- | :---: |
| custom_storages.py | Pass | [urls.py validation](#) |
| **PURRFECT SITTERS** |
| purrfect_sitters/urls.py | Pass | [urls.py validation](#) |
| **HOME** |
| home/views.py | Pass | [apps.py validation](#) |
| home/urls.py | Pass | [contexts.py validation](#) |
| **SERVICES** |
| service/models.py | Pass | [admin.py validation](#) |
| service/views.py | Pass | [apps.py validation](#) |
| service/admin.py | Pass | [apps.py validation](#) |
| service/urls.py | Pass | [apps.py validation](#) |
| **CAT** |
| cat/models.py | Pass | [apps.py validation](#) |
| cat/views.py | Pass | [urls.py validation](#)|
| cat/urls.py | Pass | [urls.py validation](#)|
| cat/admin.py | Pass | [urls.py validation](#)|
| cat/form.py | Pass | [urls.py validation](#)|
| **BOOKING** |
| booking/models.py | Pass | [apps.py validation](#) |
| booking/views.py | Pass | [urls.py validation](#)|
| booking/urls.py | Pass | [urls.py validation](#)|
| booking/admin.py | Pass | [urls.py validation](#)|
| booking/form.py | Pass | [urls.py validation](#)|

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

## Automatic Testing
- Manual testing was done due to time constraints.

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
- XX

## Defects of Note
- XX

[Back to the beginning](#table-of-contents)
