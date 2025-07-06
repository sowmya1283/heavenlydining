

# Unique Dining

## I. Site Overview

A website where dining is more than just a meal — it’s an experience. Our unique dining concept blends culinary artistry with immersive storytelling, creating unforgettable moments that engage all your senses.

Whether you’re joining us for a candlelit forest-inspired supper, a secret rooftop tasting, or a multi-course journey through global flavors, every dish is thoughtfully designed to tell a story. From the ambiance to the aroma, every detail is curated to surprise, delight, and transport you.

We don’t just serve food — we craft atmospheres. Our menus evolve with the seasons and inspirations, offering limited-seat experiences that focus on intimacy, creativity, and connection. Whether you’re a curious foodie, a romantic explorer, or someone seeking a new way to connect over cuisine, this is your invitation to dine differently.

Discover something extraordinary. Step into a dining adventure that awakens your palate and stirs your imagination.

![Hero image](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/responsiveui.jpg)

## Table of contents:

- [I. Site Overview](#i-site-overview)
- [II. Planning Stage](#ii-planning-stage)
  - [Target Audiences](#target-audiences)
  - [User Stories](#user-stories)
  - [Site Aims](#site-aims)
  - [How This Will Be Achieved](#how-this-will-be-achieved)
  - [Wireframes](#wireframes)
  - [Colour Scheme](#colour-scheme)
- [III. Current Features Common to all pages](#iii-current-features-common-to-all-pages)
  - [Navbar Description](#navbar-description)
      - [Navigation Bar](#navigation-bar)
      - [Navigation Links](#navigation-links)
  - [Footer](#footer)
  - [Typography](#typography)
- [IV. Individual Page Content Features](#iv-individual-page-content-features)
  - [Admin Page](#admin-page)
  - [Home Page](#home-page)
  - [Menu Page](#menu-page)
  - [Login Page](#login-page)
  - [Sign Up Page](#sign-up-page)
  - [View Bookings Page](#view-bookings-page)
  - [Book A Table Page](#book-a-table-page)
  - [Logout Page](#logout-page)
  - [About Us Page](#about-us-page)
- [V. Future Enhancements](#v-future-enhancements)
- [VI. Testing Phase](#vi-testing-phase)
- [VII. Deployment](#vii-deployment)
- [VIII. Credits](#viii-credits)
  - [Honourable Mentions](#honourable-mentions)
  - [General References](#general-references)
  - [Content](#content)
  - [Media](#media)


## II. Planning stage

### Target Audiences:

- Local Food Enthusiasts: Irish locals who enjoy trying unique, high-quality food experiences.
- Tourists Visiting Ireland: International visitors seeking authentic Irish experiences.
- Couples & Special Occasion Diners:  People celebrating anniversaries, engagements, or birthdays.
- Young Professionals & Foodies: Millennials and Gen Z in urban areas with disposable income.
- Corporate & Group Diners: Teams or companies looking for team meals, networking events, or client dining.

### User Stories:

- As a new user, I want to create an account so I can book a table and manage my reservations.
- As a returning user, I want to log in securely. so I can access my personal booking dashboard.
- As a logged-in user, I want to book a table by selecting the date, time, and number of guests so I can plan my dining experience in advance.
- As a logged-in user, I want to view my upcoming reservations so I can remember my dining plans.
- As a logged-in user, I want to cancel or modify my reservation so I can change my plans without needing to call.
- As a guest (unauthorized user), I want to be redirected to log in or sign up when I try to book a table so I understand that booking is only available to registered users.
- As a logged-in user, I want to view my past reservations so I can keep track of my dining history.


### Site Aims:

- To introduce and celebrate Irish cuisine through a thoughtfully crafted menu highlighting local ingredients and traditional recipes.
- To provide easy access to information about the restaurant’s offerings, location, and ambiance.
- To enable seamless table reservations for a smooth customer experience.
- To create a strong brand identity that resonates with both Irish locals and international visitors.
- To encourage visitors to choose Unique Dining as their go-to destination for special occasions, casual meals, or cultural food journeys in Ireland.

### How This Will Be Achieved:

- The homepage introduces users to the unique Irish dining experience offered.
- It provides information on the restaurant’s philosophy and what makes its cuisine special.
- The menu section displays traditional Irish dishes with descriptions and prices in euros.
- Users are provided with Signup(New user) and Login(Registered user) page to create their booking.
- The site includes an online table booking system accessible only to authorized users.
- Users can view and manage their reservations through view booking page and different actions like edit, delete.
- The contact page offers location details, opening hours, and easy ways to get in touch.

### Wireframes:

Wireframes were added to this project to keep my thoughts structured and to avoid any discrepancies from the actual website design. Links to the five targeted pages on desktop and mobile platforms are provided below.


**_Wireframe Links:_**

[Welcome Home Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/home.jpg)

[Menu Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/menu.jpg)

[Signin Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/signin.jpg)

[SignupPage](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/signup.jpg)

[Book Table Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/bookatable.jpg)

[View Bookings Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/bookinglist.jpg)

[Logout Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/logout.jpg)

[About Us Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/aboutus.jpg)

[User Profile Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/wireframes/userprofile.jpg)

### Database Schema:

I have used DrawSQL​ to draw the structure of my database. Please find the attached image below.

![DataBase Schema](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/dbschema.jpg)

### Colour Scheme:

For the Unique Dining website, I opted for a stylish yet subtle color palette with dark colored navigation bar, paired with white and an oragne variant colors for heading and nav bar text items. The goal was to keep the design dark and not overly radiant, maintaining a refined and inviting atmosphere. To ensure all text remained legible and accessible, I used a contrast grid tool (https://contrast-grid.eightshapes.com/) to test various combinations. This helped guarantee that the site offers strong visual contrast while remaining comfortable for all visitors to navigate and read.

![Color grid used](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/colorgrid.jpg)

## III. Current Features Common to all pages

### Navbar Description

The navigation bar serves as a consistent and accessible way for users to explore the Unique Dining website. Positioned at the top of every page, the navbar remains visible and responsive across all devices.
The navbar is implemented using Bootstrap’s navbar component for built-in responsiveness and styling.

**_Navigation Bar:_**

- The navigation bar (navbar) serves as a consistent, fixed element at the top of the website, allowing users to easily navigate through the different sections of the Unique Dining site. Styled with Bootstrap’s navbar-dark and bg-dark classes, it features a dark background with light text for strong contrast and readability.
- The navbar prominently displays the site title, “Unique Dining,” as a clickable brand link on the left side.
- It is mobile-friendly, using the Bootstrap navbar-toggler button to collapse and expand the menu on smaller screens.

![Nav Bar](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/navbar.jpg)

**_Navigation Links:_**

Links to main pages like Home, Menu, and About Us.

Conditional rendering based on user authentication:

For logged-in users:
- Book a Table
- View Bookings
- My Profile
- Logout

For New Users:
- Register
- Login

- Navigation links are aligned to the right (ms-auto), enhancing layout and readability.
- If fixed-top or sticky-top is added, the navbar can stay at the top of the page as users scroll.


![Hover over highlight](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/navlinkhover.jpg) 

### Footer

- The footer section of the Unique Dining website is designed to be clean and informative while maintaining consistency with the site’s dark color scheme. It includes the following elements:
- Copyright Notice: Displays a centered copyright message with the business name and year.
- Social Media Icons:
   Direct links to Facebook, Instagram, and Twitter accounts for Unique Dining are included.
   Icons are added using Font Awesome and styled to be compact and visually subtle with a consistent light color.
   Each icon opens the social platform in a new tab (target="_blank").
   Font Awesome is loaded via JavaScript at the bottom of the page for performance and proper rendering.
- Legal Links:
   A link to the Privacy Policy page is provided to support transparency and compliance.
- A statement is planned to indicate that the website content—including photographs—is the property of Unique Dining and is for educational purposes only, as per guidance received from the Code Institute community

![Footer](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/footer.jpg)

### Typography

The website uses a clean and professional typography style to enhance readability and visual appeal:

- Roboto – Imported from Google Fonts, Roboto is used throughout the body text for its modern, geometric design and excellent legibility across devices. The link is included in the <head> of the HTML
- Segoe UI – A system font used for headers and navigation areas. Known for its sharp, elegant design, it adds a subtle modern touch while ensuring good performance on Windows systems.
- A fallback of sans-serif ensures that if the custom fonts are unavailable, the site remains readable and clean using the browser’s default sans-serif font
- All fonts are selected with accessibility and user experience in mind, and performance is optimized by using widely supported, lightweight fonts.

## IV. Features

### Admin Page:
The Admin Page is a backend interface provided by Django (or your web framework) that allows site administrators to manage the website’s data and content through a secure, user-friendly interface. This page was the first page to setup.

![Admin Page]()

### Home Page:

- The Home Page of Unique Dining serves as the welcoming entry point for visitors, offering a quick snapshot of what the restaurant stands for. 
- The top section features a hero image that visually represents the ambiance and character of Unique Dining. 
- Overlaying the image is a bold, warm welcome message with the tagline “Experience Ireland’s Most Unique Culinary Journey”, setting the tone for a premium dining experience.

- Below the hero section, three informational columns highlight the restaurant’s key strengths:

   Fresh Ingredients – Emphasizing the use of high-quality, locally sourced Irish produce.
   Cozy Atmosphere – Reflecting the welcoming environment suitable for families, couples, and special occasions.
   Easy Online Booking – Showcasing the modern, user-friendly table reservation feature.

- The layout is responsive, with Bootstrap classes ensuring the content is well-aligned and accessible across all screen sizes. This page is designed to be visually engaging, informative, and easy to navigate, guiding users further into exploring the menu or booking a table.

![Home Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/homepage.jpg)

**_Hero-Image:_**

- The hero image is the visual centerpiece of the homepage, designed to immediately capture the visitor’s attention and reflect the essence of the dining experience. 
- The image features a high-quality photograph (hero2.jpg) that conveys a sense of warmth, elegance, and Irish hospitality—perfectly aligning with the brand identity.

- Overlaid text includes:

   A main heading: “Welcome to Unique Dining”
   A subheading/tagline: “Experience Ireland’s Most Unique Culinary Journey”

- This combination of imagery and text sets the emotional tone of the site, inviting users to explore the restaurant and what it offers. - The hero section spans the full width of the page and adapts to different screen sizes, ensuring consistent visual impact across devices.

This hero image helps establish a strong first impression and creates a memorable visual identity for the restaurant.

![Hero Image](https://github.com/sowmya1283/heavenlydining/blob/main/staticfiles/images/hero/hero2.jpg)

### Menu Page:

- The Menu Page of Unique Dining offers a clear and inviting display of the restaurant's full culinary selection. 
- Designed for ease of use and elegant presentation, the page is structured to guide the user through various sections of the menu. 
- The page opens with a centered title: “Our Menu”, providing immediate context. The menu is categorized into four main sections:

   Starters: Includes traditional Irish appetizers like Smoked Salmon on brown bread and Potato & Leek Soup.
   Main Courses: Highlights comforting dishes such as Guinness Beef Stew and Irish Lamb Shank.
   Desserts: Offers indulgent sweet options including Baileys Cheesecake and Sticky Toffee Pudding.
   Beverages: Lists classic Irish drinks such as Irish Coffee, Barry’s Tea, and Guinness Draught.

- Each item is presented using Bootstrap's list group component for consistency and readability. 
- Prices are clearly marked in euros (€) and aligned to the right using float-end for a professional menu layout. Responsive design ensures the menu is accessible and legible on all screen sizes. 
- This page provides users with a flavorful glimpse into the Unique Dining experience, combining traditional Irish cuisine with a polished and accessible presentation.

![Menu Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/menupage.jpg)

### Login Page:

- The Login Page of Unique Dining is designed to provide a seamless and user-friendly experience for returning users who wish to access personalized features.
- The page allows registered users to log in securely using their email or username and password.
- It uses Django Allauth's built-in authentication system for robust and secure login handling.
- The interface is clean and minimal, keeping user focus on the login form.
- The login page also contains a link to the registration page, encouraging new users to sign up if they don’t have an account.

![Login Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/loginpage.jpg)

### Sign up Page:

- The Sign Up Page provides new users with a simple and secure way to create an account on the Unique Dining platform, unlocking personalized dining experiences.
- The form allows users to register by entering a username, Optional Fields (email address, phone number, address) and password (with confirmation).
- The page uses Django Allauth for secure authentication and validation.
- Fields are clearly labeled and include helpful validation messages to guide users.
- A "Log in" link is provided for users who already have an account.

After signing up, users can:

- Log in and access the table booking features.
- View and manage their personal profile and booking history.

![Signup Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/signuppage.jpg)

### View Bookings Page

- The View Bookings Page allows authenticated users to view all their past and upcoming reservations in one convenient place.
- Table Display: Bookings are presented in a clean, tabular format showing essential details such as:

   User 
   Date & Time of booking
   Table Size that is Number of guests
   Actions (With Edit and Delete links)

- Only the bookings related to the logged-in user are shown.
- If no bookings exist, a friendly message like "You have no upcoming reservations" is displayed.
- Users may have the option to edit or cancel a booking directly from this page, depending on the project’s scope and implementation.
- User can go back to 'Book A Table' link anytime and book a new table.
- This page offers a centralized hub for users to manage their dining plans, enhancing usability and giving users a sense of control and trust in the platform.

![View Bookings Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/viewbookings.jpg)

### Book A Table Page

- The Book a Table page is designed to allow registered and logged-in users to seamlessly reserve a table at Unique Dining with just a few inputs.
- A simple, user-friendly form where users can input:
   Date of reservation
   Time of booking
   Number of guests
   Special requests

- Only authenticated users can access this page.
- Field validations are applied to ensure:

   Table sizes are between 1 and 20 guests
   Booking times are between 10 and 22 hrs.
   User cannot book a table for past time.
   Required fields are properly filled

With this setup, Unique Dining ensures efficient table management while providing guests with a smooth, reliable booking experience.

![Book Table Page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/bookatable.jpg)

### Logout Page

- The Logout Page allows users to securely end their session on the Unique Dining platform. Once a user clicks the Logout button, they are automatically signed out of their account and redirected to the home page (or login page, depending on the site configuration).
- This ensures that user data and booking information remain private and secure. A confirmation message is displyed to the user asking whether they really want to logout?
- This functionality is managed using Django Allauth, which handles session termination securely and efficiently.

![Logout page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/logoutpage.jpg)

### About Us Page

- The About Us page of the Unique Dining website introduces visitors to the restaurant’s identity, philosophy, and story. Designed with a clean and professional layout, the page emphasizes the brand’s core values: passion for food, elegance in ambiance, and a commitment to memorable dining experiences.

Key highlights of the page include:

- Brand Introduction: A compelling narrative about Unique Dining’s mission to blend global flavors with locally sourced ingredients.
- Dining Experience: It communicates the atmosphere of the restaurant — refined, inviting, and suitable for everything from casual meals to special celebrations.
- Chef Philosophy: The emphasis on handcrafted, innovative dishes conveys quality and creativity in the kitchen.
- Contact Details: Essential contact information such as phone number, email, and address is clearly presented, allowing customers to reach out or plan their visit with ease.

The content is wrapped in a styled card using Bootstrap classes (card, shadow-sm, p-4), offering a visually appealing and readable format that matches the overall theme of the website.

![About us page](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/aboutus.jpg)

## V. Future-Enhancements

- Booking as a guest: Allow users to book a table without needing to register or log in. A simple form would collect basic details like name, email, and phone number.
- Online Food Ordering System: Enable users to browse the full menu, add items to a cart, and place food orders for delivery or pickup.
- Admin Dashboard: Implement a secure admin interface for restaurant staff to manage bookings, view statistics, and update menu items dynamically.
- Live Table Availability: Display real-time availability of tables so users can see open slots before starting the booking process.
- Email & SMS Notifications: Send automatic booking confirmations and reminders to users via email or text message.
- Google Maps Integration: Embed Google Maps to help users easily locate the restaurant and get directions.
- User Reviews & Ratings: Allow users to leave reviews and rate their dining experience to help others make informed choices.
- Loyalty & Rewards Program: Introduce a points-based loyalty system to reward frequent diners with discounts or special offers.
- Allergy Preference Save Option: Let users save dietary preferences or allergy information in their profiles for faster future bookings
- Multilingual Support: Add support for multiple languages to make the site accessible to a broader audience.
- Accessibility Improvements: Improve accessibility for users with disabilities by refining keyboard navigation, adding ARIA labels, and adjusting contrast settings.

## VI. Testing Phase

Testing has been taken care and the report can be found in a separate document. Manual Testing is only considered due to time crunch and will be enhanced in future to include Automation Testing. [TESTING_PHASE.md](https://github.com/sowmya1283/heavenlydining/blob/main/TESTING_PHASE.md) that contains information about testing both during and after development.

## VII. Deployment





## VIII. Credits

### Honourable mentions:

This project could not have happened without the support of the following people listed in no particular order:

- [Richard Wells](https://github.com/D0nni387) - Code Institute Mentor who has been helping me to structure the project and guiding me all along the development of Book A Table website. 
- Code institute tutor support are always helpful and available to students anytime. I have used them whenever I was stuck with the project. Without them project wouldn't have been completed successfully.

### General reference:

- The Code Institute’s walkthrough project 'I Think Therefore I Blog' is referred all along for structure, authentication, views, model creations, to install required software and deployment and much more.

- For reference throughout the project, I have used ChatGPT, Google, Various Design website etc..

- For learning python and Django basics I have used the CS50 courses on youtube.
   https://www.youtube.com/watch?v=nLRL_NcnK-4
   https://www.youtube.com/watch?v=YzP164YANAU&list=PLhQjrBD2T380xvFSUmToMMzERZ3qB5Ueu&index=6

### Content:

- Content was from myself and some reference has been taken from chatGPT: https://chatgpt.com/
- Some of the research was done through google for the website functionality: https://www.google.com
- Icons in the footer were taken from Font Awesome: https://fontawesome.com/
- Header, text content fonts imported from Google Fonts: https://fonts.google.com/

### Media:

1. Only hero image is the media in the website and it is designed using Canva.

