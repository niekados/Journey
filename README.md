# Journey

"Journey" is a journalling app with a twist. This application, built using the Django framework, allows users to journal their moods, daily events and their progress. Embark on a journaling journey where you can reflect on your experiences and personal growth whether you want to record your thoughts or track your mood and achievements. This app features a unique function where users can anonymously let go of their worries or share their happy moments by publishing their diary entries (stories).

**[Link to the deployed application](#)**

## Index

- [Project Inception](#project-inception)
- [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframes](#wireframes)
- [Surface](#surface)
    - [Fonts](#fonts)
    - [Colours](#colours)
- [Features](#features)
    - [Feature1](#feature-1)
    - [Feature2](#feature-2)
    - [Feature3](#feature-3)
- [Future Features](#future-features)
- [Database Schema](#database-schema)
  -[Entity Relationship Diagram](#entity-relationship-diagram)
- [Agile](#agile)
  - [MoSCoW](#moscow)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Deploying Project to Heroku](#deploying-project-to-heroku)
- [Technologies Used](#technologies-used)
- [Libraries & Frameworks](#libraries-&-frameworks)
- [Credits](#credits)
- [Testing](#testing)

## Project Inception

Sometimes we have that pure and genuine connection with our journal, where we confide our deepest and truest secrets or our biggest and darkest fears. But what if keeping these thoughts in becomes too heavy? What if there is no one to share them with, or sharing them feels too scary? And what if sharing your stories, fears, and achievements could help and encourage others?

Imagine if there were a way to share your achievements safely and anonymously, without the fear of judgment. What if you didn't have to hold on to the weight of your experiences all by yourself? Journey allows you to safely let go of these burdens. Share your stories and connect with others in a meaningful way, all while maintaining your anonymity.

It's like a journey full of stories, strangers, and people we encounter on our way, whom we may never meet again. In your wanderings with strangers, sometimes your stories are the purest and truest, and they can be shared and left with strangers you will never meet again. We are wise and interesting, just sometimes too shy or lost to realize it. Talking things out is the best therapy, and Journey creates that space for us. 

Journey is for the lonely, shy, scared, silent, brave, radiant, energetic, and loving. Journey is for you.

## User Stories

### Home Page
- As a user, I want to read the website introduction on the homepage, so I can understand the purpose and ideas behind the website.
- As a user, I want to access clear instructions on the homepage, so I can easily learn how to use the website.

### Navigation & Layout (Base.html)
- As a user, I want to find a navigation menu, so I can easily move between different sections of the website.
- As a user, I want to see authentication links, so I can log in, register, or log out of my account as needed.
- As a user, I want to access social links, so I can contact or learn more about the developer.
- As a user, I want to click the website logo, so I can quickly return to the homepage from any page.

### My Journey
- As a user, I want to have an overview of all my journal entries, so I can easily access and manage them.
- As a user, I want to mark specific journal entries as public, so I can share my thoughts or achievements with the community anonymously.
- As a user, I want to update my journal entries, so I can make corrections or reflect changes in my thoughts.
- As a user, I want to delete any of my journal entries, so I can remove content that I no longer wish to keep.

### Journal Entry
- As a user, I want to create a new journal entry, so I can document my daily experiences and thoughts.

### Community Stories
 - As a user, I want to read stories shared by other community members, so I can feel connected, find inspiration, or gain reassurance that I am not alone in my experiences.

### Administrator
- 
- 
- 

## Strategy 

The Journey website focuses on addressing the emotional and psychological needs of its users. The goal of the website is to provide a safe and supportive space for personal journaling, allowing users to reflect on their daily experiences, track their emotions, and connect with a community in an anonymous way. The objectives of Journey are as follows:

- **User Empowerment:** Empower users by providing a platform where they can document their thoughts, moods, and experiences, promoting self-reflection and personal growth.
- **Anonymity and Safety:** Users can share their stories and experiences anonymously, creating a safe environment free from judgment or fear of exposure.
- **Community:** Create a sense of community by enabling users to share their stories with others, helping them feel less isolated and more connected to people who are experiencing similar challenges.
- **Ease of Use:** Design the website to be intuitive and user-friendly, so users can easily access features, navigate the platform, and focus on journaling without distractions.
- **Emotional Well-being:** Support the emotional well-being by providing a private space to analyze and constructively document their thoughts and feelings.


## Scope

The Journey website includes features and functionalities designed to meet the objectives of the user. These features are developed with a focus on usability and accessibility. The scope of the Journey website includes:

- **Homepage Introduction:** A welcoming and informative homepage that introduces users to the idea and purpose of Journey, setting a warm and inviting tone for the user experience.
- **User Authentication:** Secure login, registration, and logout functionalities, enabling users to create personal accounts where they can manage their journal entries.
- **Journal Entry Management:** Tools for creating, editing, and deleting journal entries. Users can document their daily thoughts and experiences privately.
- **Anonymous Sharing:** A feature allowing users to mark specific journal entries as public, sharing them safely and anonymously with the community without revealing their identity.
- **Community Stories:** A section where users can read stories shared by others in the community, helping them find inspiration, reassurance, and a sense of belonging.
- **Navigation and Layout:** An intuitive navigation structure, including a menu, social links, and a clickable logo that returns users to the homepage. This ensures that users can easily find their way around the website.
- **Responsive Design:** A layout that adapts seamlessly to various screen sizes and devices, ensuring a consistent user experience whether accessed on a desktop, tablet, or mobile device.

## Structure

The Journey website is designed with a clear and consistent structure that enhances user navigation and interaction across all pages. 

### Navigation Bar
- The navigation bar is located at the top of every page, providing links to the Homepage, My Journey, and Community Stories.
- Depending on the user’s authentication status, the navigation bar will display either Login/Register or Logout links.
- A footer containing social links is also present across all pages, allowing users to connect with the developer through the social links.

### Pages Overview
- **Homepage:** The welcome page where users can read the website introduction, access instructions, and navigate to other areas, such as their journal or community stories.
- **My Journey:** A personalized dashboard where users can view and manage all their journal entries. Users can create new entries, edit or delete existing ones, and mark entries as public for anonymous sharing.
- **Community Stories:** A section dedicated to anonymously shared stories from other users, organized by most recent entries, enabling easy browsing and exploration.
- **Journal Entry:** A dedicated page containing a form for creating or editing journal entries, allowing users to document their thoughts and experiences.
- **Authentication Pages:** Separate pages for login and registration, ensuring users can easily access their accounts.

### User Flow
- **Homepage to Journaling:** Users start on the homepage, where they are introduced to the app. From here, they can easily log in or register and navigate to My Journey page where they can create a new journal entry or access their existing entries.
- **Journal Entry Management:** Users can manage their journal entries from the My Journey dashboard. They can create, edit, or delete entries, with the interface providing immediate feedback on successful actions or alerting users in case of any issues.
- **Anonymous Sharing:** When marking an entry as public, users go through a confirmation process that ensures their story will be shared anonymously with the community. This ensures that users can share their experiences without fear of identity exposure.
- **Form Validation:** The forms for creating or editing journal entries include validation checks, alerting users to issues such as missing content or invalid inputs before submission.
- **Deletion Confirmation:** When a user requests to delete a journal entry, a delete confirmation will appear, asking the user to confirm the deletion. This extra step ensures that entries are not accidentally deleted.