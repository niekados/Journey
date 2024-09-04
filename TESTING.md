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

During the validation process, a few warnings were noted, specifically regarding the "Possible misuse of `aria-label`." This warning was due to the use of aria labels for FontAwesome icons. 

Despite the warnings, the errors were intentionally left as they were, as the use of `aria-label` serves a purpose. When creating a journal entry, users select their mood for the day, which is later represented by FontAwesome emojis on the journal cards. Using emojis to convey mood is an integral part of the design. Not including the `aria-label` would result in assistive technology users missing important information regarding their mood selection.

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

### Epic 1: User Authentication
As a user, I want to create an account and log in, so that I can have a private journaling experience.

- **As a user**, I want to register for an account, so that I can start using the personal journal.
    - ✔ The user can sign up using the sign-up page.

- **As a user**, I want to log in to my account, so that I can access my private journal entries.
    - ✔ The user can log in using the sign-in page.

- **As a user**, I want to log out of my account, so that I can ensure my journal entries are secure when I'm finished.
    - ✔ The user can log out using the sign-out page.

### Epic 2: Homepage Experience
As a user, I want to understand the purpose of Journey.

- **As a user**, I want to read the website introduction on the homepage, so I can understand the purpose and ideas behind the website.
    - ✔ Introduction is available on the homepage.

- **As a user**, I want to access instructions on the homepage, so I can easily learn how to use the website.
    - ✔ Instructions are available on the homepage.

### Epic 3: Navigation & Layout
As a user, I want a smooth navigation experience across the site, so I can access features easily.

- **As a user**, I want to find a navigation menu, so I can easily move between different sections of the website.
    - ✔ A navigation bar is implemented on each page.

- **As a user**, I want to access social links, so I can contact or learn more about the developer.
    - ✔ Social links are available in the footer on each page.

- **As a user**, I want to click the website logo, so I can quickly return to the homepage from any page.
    - ✔ The user can return to the homepage using the website logo on each page.

### Epic 4: My Journal
As a user, I want to view and manage my journal entries.

- **As a user**, I want to have an overview of all my journal entries, so I can easily access and manage them.
    - ✔ The user can see all journal entries on the My Journal page.

- **As a user**, I want to create a new journal entry, so I can document my thoughts and moods.
    - ✔ The user can create new entries on the My Journal page.

- **As a user**, I want to update my journal entries, so I can make corrections.
    - ✔ The user can update entries on the My Journal page.

- **As a user**, I want to delete any of my journal entries, so I can remove content that I don't want to keep.
    - ✔ The user can delete entries on the My Journal page.

- **As a user**, I can mark journal entries as public, so I can share my pain or achievements with the community anonymously.
    - ✔ The user can mark entries as public.

### Epic 5: Community Stories
As a user, I want to connect with others through shared experiences.

- **As a user**, I want to read stories shared by other community members, so I can feel connected, find inspiration, or gain reassurance that I am not alone in my experiences.
    - ✔ The user can read community stories on the Community Stories page.

### Epic 6: Administrator Controls
As an administrator, I want to manage and monitor content, so I can maintain a safe environment.

- **As an administrator**, I can update the homepage content, so that I can ensure the information and instructions presented to users are current and accurate.
    - ✔ The administrator can update the homepage content in the admin panel.

- **As an administrator**, I can review and approve user stories before they are published on the Community Stories page, so that I can prevent unsafe content from being shared with the community.
    - ✔ The administrator can review and approve user stories in the admin panel.

- **As an administrator**, I can update published user stories, so that I can make necessary edits or corrections to the content that has been shared.
    - ✔ The administrator can update published user stories in the admin panel.

- **As an administrator**, I can delete published user stories, so that I can remove any content that violates the platform’s rules after it has been published.
    - ✔ The administrator can delete published user stories in the admin panel.


## Manual Testing

| Test                                            | Expected Result                                                                    | Pass/Fail |
|-------------------------------------------------|-----------------------------------------------------------------------------------|-----------|
| Testing navbar links                            | All links should navigate to the correct sections.                                | PASS      |
| Testing footer links                            | All footer links open in a new tab and lead to the correct page.                 | PASS      |
| Form validation for new journal entries        | Mandatory fields are validated, while optional fields can remain blank.           | PASS      |
| User can register                               | User successfully creates an account and is logged into the journal page.         | PASS      |
| User can sign in                                | After signing in, the user is redirected to their journal dashboard and receives a confirmation message. | PASS      |
| User can sign out                               | User is successfully logged out and redirected to the homepage.                   | PASS      |
| Delete button confirmation                      | Clicking the delete button redirects the user to a confirmation page.             | PASS      |
| Confirm deletion of journal entry               | The entry is deleted, and the user is redirected to the My Journal page.          | PASS      |
| Cancel deletion of journal entry                | The entry remains intact, and the user is redirected back to the My Journal page. | PASS      |
| Clicking the journal entry card opens the details page | The details of the selected entry are displayed correctly.                        | PASS      |
| Edit and delete buttons in entry details       | Both buttons are available to edit or delete the entry.                          | PASS      |
| Users who are not logged in cannot access journal entries | The user is redirected to the Sign In page when trying to access those entries.      | PASS      |
| Users who are not logged in can access the home page and stories | The home page and stories page are accessible without login.                    | PASS      |
| Django messages after actions                   | Correct messages are displayed after user actions, confirming the action taken.   | PASS      |
| Search field functionality                      | Relevant entries are returned when searching; leaving the field empty returns all entries. | PASS      |
| The user can add a journal entry                      | A new entry is created and appears in the journal list.                          | PASS      |
| The user can edit a journal entry                     | The entry is successfully updated with the new information.                       | PASS      |
| The user can view journal entry details             | All relevant information for the entry is visible and correctly displayed.       | PASS      |
| The user can share a journal entry with the community     | The journal entry is tagged as "published" and awaits admin approval.            | PASS      |
| Published stories wait for admin approval       | Stories remain hidden from public view until they are approved by an admin.      | PASS      |
| Error handling on unauthorized delete           | An appropriate error message is shown when attempting to delete an entry not owned by the user. | PASS      |
| Error handling on unauthorized access           | The user receives a 403 error when attempting to access an entry that they do not own. | PASS      |


The Journey app was tested across various devices and browsers to ensure compatibility and responsiveness. The following devices have been used for testing:

### Devices Tested
- **iPhone 12**
- **iPhone 14 Pro**
- **Samsung Galaxy A54**
- **Mac Mini**
- **MacBook Air**
- **MacBook Air M2**

### Browsers Tested
- **Safari**
- **Google Chrome**
- **Firefox**
- **Brave Browser**

Although tablets were not available for testing, the app was also evaluated using developer tools to simulate tablet screen sizes and ensure a responsive design.

## Bugs

- ### Adjust `delete_journal_entry` View

**Bug Description**:  
An issue in the delete_journal_entry view allowed unauthorized users to access the delete confirmation template for journal entries they didn’t own, although they couldn’t delete the entry from the database.

**Bug Fix**:  
The code was adjusted to ensure that only the owner of the journal entry can access the delete confirmation template.

- ### Exclude Journal Entry in Admin Story Section

**Bug Description**:  
In the admin interface, the entry author's name was displayed in the Stories section, which revealed the author's identity and was not part of the design.

**Bug Fix**:  
The following changes were made to ensure the journal entry author’s name is not displayed in the admin Stories section:

1. Updated the `__str__` method for the JourneyEntry model to return the story description with the date, instead of the author's name.
2. Excluded `journal_entry` from being displayed in `StoryEntryAdmin`.

- ### Correct Journal Entry Confirm Delete Template Extension

**Bug Description**:  
The `journal_entry_confirm_delete` template had an incorrect file extension of `.html.html`, which caused issues when trying to render the template.

**Bug Fix**:  
The file extension was corrected by reverting it to a single `.html` extension.

- ### Change Mood Field Type in Model

**Bug Description**:  
The `mood` field in the model was incorrectly set as an `IntegerField`, which was an oversight from when the model originally used numerical selections for choices. 

**Bug Fix Implementation**:  
The field type was changed from `IntegerField` to `CharField` to accommodate string choices instead of numbers, reflecting the updated design requirements.

- ### Resolve Circular Import Issue Between Models

**Bug Description**:  
There was a circular import issue between the `StoryEntry` and `JournalEntry` models. This occurred because both models attempted to import each other, leading to an infinite loop.

**Bug Fix Implementation**:  
To resolve this circular import problem, a lazy loading was utilized. By using Django’s app registry, the `apps.get_model()` function was implemented to import the `StoryEntry` model only when it was needed, rather than at the top of the file.

