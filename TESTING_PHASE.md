## Table of Contents

- [Testing Phase](#testing-phase)
- [I. Testing While Developing](#i-testing-while-developing)
- [II. Testing Phase](#ii-testing-phase)
  - [Functional Testing](#functional-testing)
  - [Negative Testing](#negative-testing)
  - [Validators](#validators)
    - [HTML](#html)
    - [CSS](#css)
    - [Python (PEP 8)](#python-pep-8)
- [III. Open Issues](#iii-open-issues)


# Testing Phase**

Overview: The Unique Dining website has undergone extensive manual testing to ensure functionality, usability, responsiveness, and compatibility across various devices and browsers. Below are the major testing categories and results.

## I. Testing While Developing 

 ## II. Testing Phase**

 **Functional Testing**
 **Negative Testing**

**Validators**

- HTML
- CSS
- Python (PEP 8)


## III. Open Issues


## I. Testing while developing 

During development, the following practices and testing approaches were used to ensure each feature worked correctly and the website remained stable:

Iterative Testing:

- Each page and feature was tested immediately after implementation using a test-as-you-build approach:
- Home Page: Ensured the welcome text, hero image, and CTA buttons appeared correctly during layout and design updates.
- Navigation Bar: Tested navigation links after every style or route update.
- Forms (Login, Signup, Book a Table): Inputs were validated continuously with various edge cases during form development.
- Booking Logic: Booking form submission was tested after each logic update to verify time slot and guest handling.

## II. Testing Phase

### Manual Testing:

**Functional Testing**

- FTC_1:

Feature Tested: Home Page
Test Scenario: Load the home page	
Expected Result: Welcome message and navigation menu visible
Actual Result: As Expected
Status: Pass

- FTC_2:

Feature Tested: Menu Page
Test Scenario: View menu categories (Starters, Mains, Desserts, Beverages)	
Expected Result: Menu items displayed properly
Actual Result: As Expected
Status: Pass

- FTC_3:

Feature Tested: Login Page
Test Scenario: Attempt login with valid & invalid credentials.
Expected Result: Access granted or error message shown
Actual Result: As Expected
Status: Pass

- FTC_4:

Feature Tested: Sign Up Page
Test Scenario: Submit sign-up form with missing or invalid fields
Expected Result: Validation messages displayed
Actual Result: As Expected
Status: Pass

- FTC_5:

Feature Tested: Book A Table Page
Test Scenario: Submit booking with valid date, time, and guests
Expected Result: Booking list is displayed with the booking
Actual Result: As Expected
Status: Pass

- FTC_6:

Feature Tested: View Bookings Page.
Test Scenario: User can view confirmed Bookings.	
Expected Result: Shows user’s bookings
Actual Result: As Expected
Status: Pass

- FTC_7:

Feature Tested: Click logout button
Test Scenario: Asked for confirmation from the user and then Session cleared, and logged out
Expected Result: Redirected to homepage.
Actual Result: As Expected
Status: Pass

- FTC_8:

Feature Tested: Check logout Functionality
Test Scenario: Click on logout. Asked for confirmation from the user and then Session cleared, and logged out
Expected Result: Redirected to homepage.
Actual Result: As Expected
Status: Pass


- FTC_9:

Feature Tested: Navigation Bar
Test Scenario: Click all links in home page and when user the logged in.
Expected Result: Navigates to the correct section/page
Actual Result: As Expected
Status: Pass

- FTC_10:

Feature Tested: Footer
Test Scenario: Verify links and social icons work
Expected Result: Correct external links open in new tab
Actual Result: As Expected
Status: Pass

- FTC_11:

Feature Tested: When No bookings are present
Test Scenario: Verify user is displayed with correct information when he has not made any bookings.
Expected Result: Correct message is displayed to the user.
Actual Result: As Expected
Status: Pass

- Responsive Design	Open site on mobile, tablet, and desktop	Content adapts to screen size	As expected	


**_Negative Test Cases_**

- NTC_1:

Feature Tested: Validation in sign-up form
Test Scenario: Submit empty sign-up form
Expected Result: Show validation error messages
Actual Result: As Expected
Status: Pass

- NTC_2:

Feature Tested: Date validation while booking.
Test Scenario: Provide incorrect date (Date in the past, or invalid format) while booking a table.
Expected Result: Error message or form rejection
Actual Result: As Expected
Status: Pass

- NTC_3:

Feature Tested: Time validation while booking.
Test Scenario: Provide incorrect Time(Time before 10:00 or after 22:00) while booking a table.
Expected Result: Error message or form rejection
Actual Result: As Expected
Status: Pass

- NTC_4:

Feature Tested: Table Size validation
Test Scenario: Provide incorrect table size(>20) while booking a table.
Expected Result: Error message or form rejection
Actual Result: As Expected
Status: Pass


### Bugs and Fixes:

During development phase some of the bugs were identified by myself and has been fixed while testing over a live server. over multiple screen resolution simulated the scenarios where a user will try to use the website.

Bugs discovered when testing using VSCode's live server addon is provided below. I experimented with every element to see how it would appear to potential consumers on a variety of screen widths, ranging from 320px to 4000px:

 #### 1. Expected Outcome
Logged in user is able to book a table
**_Issue Found:_**
-   When user clicked on Book A Table link, link was broken.
**_Solution Used:_**
- Updated the Book A Table link correctly

#### 2. Expected Outcome
User Profile information Should be displayed correctly excluding emply values.
**_Issue Found:_**
- User Profile information had blank values and inconsistent values. 
**_Solution Used:_**
- Resolved this issue by adding logical checks and validated for consistent and valid information

#### 3. Expected Outcome
All the pagination in 'View Bookings' page is working properly.
**_Issue Found:_**
- Pagination links and data were not displayed properly. Morethan 5 booking reservations were excluded
**_Solution Used_**:
- Fixed the issue in the code by adding page obejcts values and its functionality for pagination

#### 4. Expected Outcome
User should be able to book a table only in the future date.
**_Issue Found:_**
- User was able to book a table in the past date.
**_Solution Used:_**
- Fixed it by adding validation to the date field to include date > current date

#### 5. Expected Outcome
User should not be able to book with table size as 0.
**_Issue Found:_**
- User was able to book a table with table size as 0.
**_Solution Used:_**
- Fixed the code where logical check was not evaluating the condition properly

#### 6. Expected Outcome
All the cosmetic changes should be correct.
**_Issue Found:_**
- Had found many cosmetic issues throughout the website.
**_Solution Used:_**
- All the cosmetic issues were fixed and revalidated throughout the website

#### 7. Expected Outcome
User should be able to edit/modify his/her booking
**_Issue Found:_**
- User waa not able to edit his/her booking if he/she changes their mind
**_Solution Used:_**
- Fixed the issue by loading the static file correctly

#### 8. Expected Outcome
Validations for the book a table should be present
**_Issue Found:_**
- Validations for the updating a table form was present, and user could book a table with 0 users, in the past date and before/after 10:00 and 22:00
**_Solution Used:_**
- Fixed the views for update booking to include validate code 


**1. Validators**

**_HTML_** **-** [**https://validator.w3.org/nu/**](https://validator.w3.org/nu/)

- Home Page: 
![homepage screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/homepage.jpg)

- Menu Page:
![menupage screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/menupage.jpg)

- Signup Page:
![register screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/signup.jpg)

- Login Page:
![login screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/loginpage.jpg)

-AboutUs Page:
![aboutus screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/aboutus.jpg)

- Book A Table Page:
![bookatable screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/bookingpage.jpg)

- View Bookings Page:
![viewbookings screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/viewbookings.jpg)

- User Profile Page
![userprofile screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/userprofile.jpg)

- Logout Page:
![logout screenshot](https://github.com/sowmya1283/heavenlydining/blob/main/docs/screenshots/htmlvalidators/logout.jpg)

**_CSS_** **-** [**https://jigsaw.w3.org/css-validator/**](https://jigsaw.w3.org/css-validator/)
- An error and vendor warnings are present in CSS file.

![CSS validator screenshot]()

**_Python Validators_** **-** [**https://pep8ci.herokuapp.com/**](https://pep8ci.herokuapp.com/)
- Some of the warning for spaces and length too long errors were present in the python code. This will be fixed in the future.

![Views python screenshot]()
![Settings python screenshot]()

## III. Open Issues

- Currently there are no known open issues. (Functionality issues)
- Some CSS styling can be added in future. 
- Need to fix CSS style sheet error and vendor warnings.
- Nav bar active page links have inconsitant behaviour, will be fixed in next build.