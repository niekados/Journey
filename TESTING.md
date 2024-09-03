# Testing

## Index

- [Validation](#validation)
    - [HTML Validation](#html-Validation)
    - [CSS Validation](#css-validation)
    - [PEP8 Validation](#pep8-validation)
    - [Lighthouse Testing](#lighthouse-testing)
- [Testing User Stories](#testing-user-stories)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
- [Known Bugs](#known-bugs)

## Validation

### HTML Validation

The HTML code for the Journey app was validated using the [W3C Markup Validation Service](https://validator.w3.org/). 

- **Validation Method**:
  - URI validation was employed for all pages that did not require user login.
  - Direct input validation was used for pages that required a login. The HTML code was extracted by viewing the page's source directly. 

During the validation process, a few warnings were noted, specifically regarding the "Possible misuse of aria-label." This warning was due to the use of aria-labels for FontAwesome icons. 

Despite the warnings, the errors were intentionally left as they are, as the use of aria-labels serves a purpose. When creating a journal entry, users select their mood for the day, which is later represented by FontAwesome emojis on the journal cards. Using emojis to convey mood is an integral part of the design. Not including the aria-label would result in assistive technology users missing important information regarding their mood selection.

- Home Page
    - <img src="documentation/validation/html-home.png" alt="Home page" style="width:70%;">

- Community Stories
    - <img src="documentation/validation/html-stories.png" alt="Stories page" style="width:70%;">

- Journal Page
    - <img src="documentation/validation/html-journal.png" alt="Journal page" style="width:70%;">

- Journal Entry Detail
    - <img src="documentation/validation/html-journal-detail.png" alt="Journal entry detail" style="width:70%;">

- Edit Journal Entry
    - <img src="documentation/validation/html-journal-edit.png" alt="Edit journal entry" style="width:70%;">

- Delete Journal Entry Confirmation
    - <img src="documentation/validation/html-journal-confirm-delete.png" alt="Delete journal entry confirmation" style="width:70%;">

- Add Journal Entry
    - <img src="documentation/validation/html-journal-add-entry.png" alt="Add journal entry" style="width:70%;">

- Sign In Page
    - <img src="documentation/validation/html-sign-in.png" alt="Sign in page" style="width:70%;">

- Sign Up Page
    - <img src="documentation/validation/html-sign-up.png" alt="Sign up page" style="width:70%;">

- Sign Out Page
    - <img src="documentation/validation/html-sign-out.png" alt="Sign out page" style="width:70%;">

- Error 403
    - <img src="documentation/validation/html-403.png" alt="Error 403" style="width:70%;">

### CSS Validation

The CSS code for the Journey app was validated using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

<img src="documentation/validation/css.png" alt="CSS validation" style="width:70%;">

### PEP8 Validation

The Python code for the Journey app was checked for PEP8 compliance using the [Code Institute's Python Linter Tool](https://pep8ci.herokuapp.com/).

#### Home

- admin.py
    - <img src="documentation/validation/python-home-admin.png" alt="home admin.py" style="width:70%;">

- models.py
    - <img src="documentation/validation/python-home-models.png" alt="home models.py" style="width:70%;">

- views.py
    - <img src="documentation/validation/python-home-views.png" alt="home views.py" style="width:70%;">

- urls.py
    - <img src="documentation/validation/python-home-urls.png" alt="home urls.py" style="width:70%;">

#### Stories

- admin.py
    - <img src="documentation/validation/python-stories-admin.png" alt="stories admin.py" style="width:70%;">

- models.py
    - <img src="documentation/validation/python-stories-models.png" alt="stories models.py" style="width:70%;">

- views.py
    - <img src="documentation/validation/python-stories-views.png" alt="stories views.py" style="width:70%;">

- urls.py
    - <img src="documentation/validation/python-stories-urls.png" alt="stories urls.py" style="width:70%;">

#### Journal

- admin.py
    - <img src="documentation/validation/python-journal-admin.png" alt="journal admin.py" style="width:70%;">

- models.py
    - <img src="documentation/validation/python-journal-models.png" alt="journal models.py" style="width:70%;">

- views.py
    - <img src="documentation/validation/python-journal-views.png" alt="journal views.py" style="width:70%;">

- forms.py
    - <img src="documentation/validation/python-journal-forms.png" alt="journal forms.py" style="width:70%;">

- urls.py
    - <img src="documentation/validation/python-journal-admin.png" alt="journal urls.py" style="width:70%;">

#### Journey (project)

- urls.py
    - <img src="documentation/validation/python-journey-urls.png" alt="journey urls.py" style="width:70%;">

### Lighthouse Testing

Lighthouse, a tool provided by Google Chrome DevTools, was used to audit the Journey app's performance, accessibility, best practices, SEO, and progressive web app (PWA) features. 

During the testing of the 403 error page (a feature of the app), a warning was received: "Lighthouse was unable to reliably load the page you requested. Make sure you are testing the correct URL and that the server is properly responding to all requests. (Status code: 403)." This warning is expected, as the page returns a 403 status, indicating that access is forbidden. The warning was left as is, and no further action was taken.

- Home Page
    - Mobile
        - <img src="documentation/lighthouse/home-mobile.png" alt="Mobile home page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/home-desktop.png" alt="Home page" style="width:70%;">

- Community Stories
    - Mobile
        - <img src="documentation/lighthouse/stories-mobile.png" alt="Mobile stories page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/stories-desktop.png" alt="Stories page" style="width:70%;">

- Journal Page
    - Mobile
        - <img src="documentation/lighthouse/journal-mobile.png" alt="Mobile journal page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/journal-desktop.png" alt="Journal page" style="width:70%;">

- Journal Entry Detail
    - Mobile
        - <img src="documentation/lighthouse/journal-detail-mobile.png" alt="Mobile journal entry detail" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/journal-detail-desktop.png" alt="Journal entry detail" style="width:70%;">

- Edit Journal Entry
    - Mobile
        - <img src="documentation/lighthouse/journal-edit-mobile.png" alt="Mobile edit journal entry" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/journal-edit-desktop.png" alt="Edit journal entry" style="width:70%;">

- Delete Journal Entry Confirmation
    - Mobile
        - <img src="documentation/lighthouse/journal-delete-mobile.png" alt="Mobile delete journal entry confirmation" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/journal-delete-desktop.png" alt="Delete journal entry confirmation" style="width:70%;">

- Add Journal Entry
    - Mobile
        - <img src="documentation/lighthouse/journal-add-mobile.png" alt="Mobile add journal entry" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/journal-add-desktop.png" alt="Add journal entry" style="width:70%;">

- Sign In Page
    - Mobile
        - <img src="documentation/lighthouse/sign-in-mobile.png" alt="Mobile sign in page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/sign-in-desktop.png" alt="Sign in page" style="width:70%;">

- Sign Up Page
    - Mobile
        - <img src="documentation/lighthouse/sign-up-mobile.png" alt="Mobile sign up page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/sign-up-desktop.png" alt="Sign up page" style="width:70%;">

- Sign Out Page
    - Mobile
        - <img src="documentation/lighthouse/sign-out-mobile.png" alt="Mobile sign out page" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/sign-out-dekstop.png" alt="Sign out page" style="width:70%;">

- Error 403
    - Mobile
        - <img src="documentation/lighthouse/403-mobile.png" alt="Mobile error 403" style="width:70%;">
    - Desktop
        - <img src="documentation/lighthouse/403-desktop.png" alt="Error 403" style="width:70%;">

## Testing User Stories

## Manual Testing

## Bugs

