## TESTING

## Validation Testing
[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator.

| Page | Result | Evidence |
| :--- | :--- | :---: |
| Home Page | Pass | [Home Page Validation](#) |
| Services | Pass | [Privacy Page Validation](#) |
| Cat Profile | Pass | [Terms & Conditions Page Validation](#) |
| Cat Detail| Pass | [Delivery Page Validation](#) |
| Edit Cat | Pass | [Contact Form Page Validation](#)|
| Delete Cat | Pass | [Contact Success Page Validation](#) |
| Booking | Pass |[Product Page Validation](#) |
| Booking Success | Pass | [Product Detail Page](#) |
| 400 Error | Pass | [Profile Page Validation](#) |
| 403 Error | Pass | [Bag Page Validation](#) |
| 404 Error | Pass | [Checkout Page Validation](#) |
| 500 Error | Pass | [Checkout Success Page](#) |
| 404 Error Page | Pass | [404 Page Validation](#) |

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
| custom_storages.py | Pass | [custom_storages.py validation](#) |
| **PURRFECT SITTERS** |
| seaside_sewing/settings.py | Pass | [settings.py validation](#) |
| seaside_sewing/urls.py | Pass | [urls.py validation](#) |
| **HOME** |
| bag/apps.py | Pass | [apps.py validation](#) |
| bag/contexts.py | Pass | [contexts.py validation](#) |
| **SERVICES** |
| checkout/admin.py | Pass | [admin.py validation](#) |
| checkout/apps.py | Pass | [apps.py validation](#) |
| **CAT** |
| home/apps.py | Pass | [apps.py validation](#) |
| home/urls.py | Pass | [urls.py validation](#)|
| **BOOKING** |
| products/admin.py | Pass | [admin.py validation](#) |
| products/apps.py | Pass | [apps.py validation](#) |

## Visual (UI) Testing: Cross Browser and Cross Device Testing
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
