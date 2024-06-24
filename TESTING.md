# **TESTING**

The Guilty Sheep website has been tested manually as well as with automated services like code validators and browser developer tools.

# **Contents**

- [**TESTING**](#testing)
- [**Contents**](#contents)
  - [**Code Validators**](#code-validators)
    - [*w3schools HTML Validator*](#w3schools-html-validator)
    - [*w3schools CSS Validator*](#w3schools-css-validator)
    - [*JsHint JavasScript Validator*](#jshint-javasscript-validator)
  - [**Features Testing**](#features-testing)
  - [**Responsiveness Test**](#responsiveness-test)
  - [**Browser Compatibility**](#browser-compatibility)
  - [**Testing User Stories**](#testing-user-stories)
  - [**Perofrmance**](#perofrmance)
    - [**User Profiles**](#user-profiles)
    - [**Movie Card**](#movie-card)
    - [**Header and Footer**](#header-and-footer)
  - [**Known Bugs**](#known-bugs)
    - [**Resolved**](#resolved)
  - [**Additional Testing**](#additional-testing)
    - [**Lighthouse**](#lighthouse)
  
## **Code Validators**

### *[w3schools HTML Validator](https://validator.w3.org)*

### *[w3schools CSS Validator](https://jigsaw.w3.org/css-validator/)*

![css-validator]()

### *[JsHint JavasScript Validator](https://jshint.com)*

![js-validator]()

[Back to top](#contents)

## **Features Testing**

- ### Navigation Menu
  
    Expected: The feature is expected to redirect to the various website pages.
    Testing: Tested the feature by clicking each link manually and examining the result.
    Result: The feature acted as expected and redirected to other pages.

- ### User Profiles
    - Feature 1: Registration

        Expected: Users should be able to create a personalized profile by registering with a unique username and password.
        Testing: Attempted to register as a new user by providing necessary details such as username, email, and password through the registration form.
        Result: Successfully registered as a new user and was redirected to the login page.

    - Feature 2: Login

        Expected: Existing users should be able to securely sign in to their accounts using their credentials.
        Testing: Entered valid login credentials (username and password) into the login form and attempted to sign in.
        Result: Successfully logged in and was redirected to the user dashboard.

    - Feature 3: Admin Access

        Expected: Admin users should have access to an exclusive admin profile with additional functionalities.
        Testing: Attempted to sign in as an admin user and verified access to admin-exclusive functionalities.
        Result: Successfully accessed the admin profile with privileges to monitor, edit, delete, and create products and reviews.

    - Feature 4: Profile Page

        Expected: Each user should have a personalized profile page where they can view and update their information, look at past orders, and manage their product reviews.
        Testing: Navigated to the profile page after logging in and checked the available functionalities.
        Result: The profile page displayed user information, past orders, and options to manage product reviews as expected.

- ### Product Listing and Details
  
        Expected: Users should be able to browse through a list of products and view detailed information for each product.
        Testing: Navigated through the product listings and clicked on individual products to view details.
        Result: Product listings and details displayed correctly with relevant information.
    

- ### Categories, Collections and Aritists
  
        Expected: Users should be able to filter products by specific categories, collections, or artists.
        Testing: Selected various categories and collections to check the filtered product listings.
        Result: Products were correctly filtered and displayed according to the selected category or collection.
    

- ### Shopping Bag and Wishlist
    - Feature 1: Shopping Bag

        Expected: Users should be able to view items in their shopping bag and review their selections before checkout.
        Testing: Added items to the shopping bag and reviewed the contents.
        Result: Shopping bag displayed the selected items with options to adjust quantities or remove items.
    
    - Feature 1: Wishlist

        Expected: Users should be able to add products to a wishlist for future reference.
        Testing: Added items to the wishlist and checked the wishlist page.
        Result: Wishlist displayed the added products and provided options to move items to the shopping bag.
    
- ### Checkout Process
  
        Expected: Users should be able to securely enter their payment information and complete their purchase.
        Testing: Proceeded through the checkout process by entering billing and shipping information, payment details, and reviewing the order.
        Result: Checkout process completed successfully with order confirmation displayed on the site and sent via email.
    
- ### Search and Filter
    - Feature 1: Search

        Expected: Users should be able to search for products by keywords.
        Testing: Entered various keywords into the search bar to locate specific items.
        Result: Search results displayed relevant products matching the keywords.

    - Feature 2: Filter

        Expected: Users should be able to sort products by various criteria (e.g., price, popularity) and filter based on attributes (e.g., size, color).
        Testing: Applied different sorting and filtering options to the product listings.
        Result: Products were correctly sorted and filtered according to the selected criteria and attributes.
    
- ### User Reviews
    - Feature 1: Add Review

        Expected: Users should be able to add reviews for products they have purchased.
        Testing: Submitted reviews for various products.
        Result: Reviews were successfully added and displayed on the product pages.

    - Feature 2: Manage Reviews

        Expected: Users should be able to view a list of their reviews, and edit or delete them as necessary.
        Testing: Checked the list of reviews in the user profile and edited or deleted some reviews.
        Result: Reviews were correctly displayed, and edits or deletions were successfully applied.
    
- ### Admin Product Management
    - Feature 1: Manage Products

        Expected: Admin users should be able to add, edit, and delete products.
        Testing: Used the admin interface to perform CRUD operations on products.
        Result: Products were successfully managed with changes reflected on the website.

    - Feature 2: Manage Reviews

        Expected: Admin users should be able to manage user reviews to maintain a positive user experience.
        Testing: Accessed the admin review management interface to moderate reviews.
        Result: Reviews were successfully managed with options to approve, edit, or delete as needed
    



