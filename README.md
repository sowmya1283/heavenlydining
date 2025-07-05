

# Unique Dining

## I. Site Overview

A website where dining is more than just a meal — it’s an experience. Our unique dining concept blends culinary artistry with immersive storytelling, creating unforgettable moments that engage all your senses.

Whether you’re joining us for a candlelit forest-inspired supper, a secret rooftop tasting, or a multi-course journey through global flavors, every dish is thoughtfully designed to tell a story. From the ambiance to the aroma, every detail is curated to surprise, delight, and transport you.

We don’t just serve food — we craft atmospheres. Our menus evolve with the seasons and inspirations, offering limited-seat experiences that focus on intimacy, creativity, and connection. Whether you’re a curious foodie, a romantic explorer, or someone seeking a new way to connect over cuisine, this is your invitation to dine differently.

Discover something extraordinary. Step into a dining adventure that awakens your palate and stirs your imagination.

![Hero image](https://github.com/sowmya1283/heavenlydining/blob/main/Static/images/hero/hero2.jpg)

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
  - [Header Element](#header-element)
    - [Navigation Bar](#navigation-bar)
    - [Navigation Links](#navigation-links)
    - [Hero Image](#hero-image)
  - [Footer](#footer)
  - [Typography](#typography)

## IV. Individual Page Content features
### - Home Page or Welcome Home Page
### - Crazy for Crochet Content Page
### - Mosaic Art Content Page
### - Quilling Craft Content Page
### - Sign Up Page
## V. Future-Enhancements
## VI. Testing Phase
## VII. Deployment
## VIII. Credits
### - Honourable mentions
### - General reference
### - Content
### - Media


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


**_Desktop wireframes:_**

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

The header element stays fixed at the top of the page when the user first scrolls through (or scrolls up and down). A Code Institute alumnus pointed out that the sticky header will improve user experience and adhere to prevailing trends. The header itself contains the below elements.


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

![Footer]()

### Typography

The website uses a clean and professional typography style to enhance readability and visual appeal:

- Roboto – Imported from Google Fonts, Roboto is used throughout the body text for its modern, geometric design and excellent legibility across devices. The link is included in the <head> of the HTML
- Segoe UI – A system font used for headers and navigation areas. Known for its sharp, elegant design, it adds a subtle modern touch while ensuring good performance on Windows systems.
- A fallback of sans-serif ensures that if the custom fonts are unavailable, the site remains readable and clean using the browser’s default sans-serif font
- All fonts are selected with accessibility and user experience in mind, and performance is optimized by using widely supported, lightweight fonts.

## IV. Individual Page Content features

### Home Page Or ‘Welcome Home!’ Page:

**_Hero-Image:_**

Very striking and colourful hero image for a website that displays a range of artistic crafts. A variety of colourful supplies and equipment, including yarn, coloured pencils, beads, fabric and paintbrushes are used in the scenario. There’s a hand-drawn sign in the foreground that says “Handmaade Hobbies.” As you can see, the image has two ‘AA’’s in the ‘HANDMAADE’ just to be more creative.
The background image is configured to cover with the position centre, thus the image appears fantastic on all screen resolution.

![Hero Image](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/hero.png)


Inside the hero image, an overlay with the craft categories are listed in this web site. This is added because to create an customer attention or to make a positive impact to a new visitor on the website. This text is made readable with a transparent background making it easier to notice. The position of this overlay is made absolute so that it can be placed on top of the Hero image.

**_What? , Why? and Benefits! Section:_**

The main purpose of the website is to inspire, convey information or benefits of handmade craft items , connect with like-minded hobbyists , to reach out to the author for any collaborative work and etc. Therefore the section below the hero image is divided into three parts with detail information about ‘What is’ handmade hobbies is all about? ‘Why’ Handmade hobbies? and ‘Benefits’ of Handmade hobbies for any individual.

As you can see the images below, they are having a title information as mentioned above.

![What are handmade hobbies](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/what.png)

![Why handmade hobbies](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/why.png)

![Benefits of handmade hobbies](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/benefits.png)

The above section is also made responsive based on the Mobile, Tablet and Laptop version. Enough padding is added to make the content displayed neatly within the div for larger screens. Whereas padding has been reduced to make sure that this content is more readable on mobile devices.

**_Circular image:_**

Circular image has been added to match the handmade hobbies content which is mentioned above and is responsive according to the screen resolution.

The circular image conveys the message that what users will be doing when they see handmade hobbies. The image has seven sections where people are involved in crochet, knitting, moulding clay, painting etc.

![Added circular screenshot](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/circularimage.png)

**_Meetup Times:_**

The last section of our welcome home page is our ‘Meetup times’ section. A website’s “Meetup” section can greatly increase consumer interaction, offer social and educational benefits, and also will help to create a solid, dedicated client base. It may provide lively and engaging environment for their clients by providing a range of activities and making sure that communication is simple.

This section provides visitors about all the necessary information about our timings of meetup events happening over the complete week. Based on the information provided on the website user can decide which meetup session they want to join.
this meetup events tell information like time, day of the meetup and what will be the agenda of the meetup.

![Meetup time screenshot](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/meetup_times.png)

## All the other page contents(Similar to Gallery)

All the pages apart from welcome home page in the website are similar like ‘Gallery’ pages. They have different images files loaded and are responsive to the screen sizes. On mobile screens, these images are loaded in single column. As the screen size increases the column are spread-out. To help the visually impaired users on the scenario of failed image loading, an alt text has been added to each image. In-case of image loading fails, the alt text displays. Columns will increase according to the screen size. (eg., for mobile single column, for tablet 3 columns and laptops four columns)

### Crazy For Crochet Page:

- A wide range of creative possibilities are offered by Crochet. Some examples are clothing, baby items, home decor items, accessories, seasonal items etc.
- This crochet gallery page has some beautiful images to inspire the hobbyists.
- The gallery page has only image content, no text content has been added to this.

![Crazy for crochet gallery page ](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/Crazyforcrochetpage.png)

### Mosaic Art Page:

- Mosaic art is a form of decorative art mainly from different cultural background like Greece, Roman and Islamic traditions. Created using small piece of materials such as stone, glass pieces, ceramic or tiles etc.
- This Mosaic gallery page has some beautiful images to inspire the hobbyists.
- The gallery page has only image content, no text content has been added to this.

![Mosaic art page](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/MosaicArtPage.png)

### Quilling Craft Page:

- Quilling is a form of paper art which is made using strips of paper. These stripes are rolled, glued to create different shapes.
- The Quilling Craft gallery page has some beautiful images to inspire the hobbyists.
- The gallery page has only image content, no text content has been added to this.

![Quilling craft page](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/QuillingCraft.png)

### Sign Up page content

- The purpose of this page is to simulate the process of submitting a form.
- A background image with light golden colour which is in contrast for the form colour.
- A hand holding heart font has been added before the ‘Let’s get you signed up!’ text. This icon is from font-awesome.
Adjusted the image and the form properly by using margin-top. The large gap between the nav and the form were reduced using this property.
- All the radio buttons were not aligned properly at the initial stage and they have been made to spread-out with justify content property.

![Sign up page](https://github.com/sowmya1283/handmadehobbies/blob/main/docs/screenshots/Signuppage.png)

## V. Future-Enhancements

- The future intention of the site would be to serve as a website specifically to grow visitors and involve more hobbyists to sign up to the website. To add more content related to new designs, tutorials, different type of materials used. If possible enhance the website to create a buy and sell platform at later stages.
- At first, the purpose would remain to inspire people and spread awareness about benefits of hand-crafted items. However, There would be additional content as mentioned above.
- Video tutorials of all the handmade craft items.
- How to choose materials to use for different kind of handmade craft items.
- Handmade hobbies account creation on different social media platforms and linking them to the website.
- Bringing users designs on the webpage.
- Improvising the media content format on the different gallery pages.
- I would also make the contact form fully function with a post request and have a database to collate data for the mailing list.

## VI. Testing Phase

I have a second document named [TESTING_PHASE.md](https://github.com/sowmya1283/handmadehobbies/blob/main/TESTING_PHASE.md) that contains information about testing both during and after development.

## VII. Deployment

I deployed the page on GitHub pages via the following procedure: -

- From the project’s repository, go to the Settings tab.
- From the left-hand menu, select the Pages tab.
- Under the Source section, select the Main branch from the drop-down menu and click Save.
- A message will be displayed to indicate a successful deployment to GitHub pages and provide the live link.
- You can find the live site via the following URL- https://sowmya1283.github.io/handmadehobbies/

## VIII. Credits

### Honourable mentions:

This project could not have happened without the support of the following people listed in no particular order:

- [Richard Wells](https://github.com/D0nni387) - Code Institute Mentor who has gone above and beyond what was expected of him to help me get this far in the course.
- Lewis Dillon: From Code institute For the longest and most comprehensive peer review that I received via our stand-up calls. His feedback was truly amazing
- Tulio Minini: One of my friend from code institute has been helping me in reviewing the website and provided some great comments.
- The code institute Slack community as a whole who tested and supported throughout.
- And the biggest thanks goes to my daughter and my mother who inspires me and encourages me to keep learning.
- Code institute tutor support are awesome, they always help in fixing any workspace issues or launching website issues has been very helpful or even tutoring was very helpful.

### General reference:

- The Code Institute’s “Love Running” code-along initiative had an impact on the project. Even though I made every effort to diverge, there might still be some code similarities.
- Throughout the project, I used stack overflow, google, and W3schools as general references.

### Content:

- All content was written by myself except some used from chatGPT: https://chatgpt.com/
- Some of the handcraft text contents were inspired by wikipedia: https://www.wikipedia.org/
- Icons in the footer were taken from Font Awesome: https://fontawesome.com/
- Header, text content fonts imported from Google Fonts: https://fonts.google.com/

### Media:

1. Handmade Hobbies logo is generated and modified from - https://ideogram.ai/ and Canva respectively.
2. Some Quilling Craft gallery images are taken from - https://www.freepik.com/
3. Some Quilling Craft gallery images are taken from - https://stock.adobe.com/
4. Some Mosaic Art gallery images are taken from - https://stock.adobe.com/
5. Some Crazy For Crochet gallery images are generated from - https://ideogram.ai/
6. Some Crazy For Crochet gallery images are generated from - https://stock.adobe.com/
7. Some Crazy For Crochet gallery images are generated from - https://www.freepik.com/
8. Screenshot under README.md section titled “site overview” was created using - https://ui.dev/amiresponsive
9. Some of the images are from google images - https://www.google.com/imghp?hl=en-GB&tab=ri&authuser=0&ogbl
10. Some of the images are resized using - https://www.tinypng.com
