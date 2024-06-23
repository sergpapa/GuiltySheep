# **Guilty Sheep - Join the Heard**

## **Introduction**

Guilty Sheep is a trendsetting e-commerce platform dedicated to offering unique, stylish products curated from various categories, collections, and artists. Guilty Sheep aims to provide a seamless shopping experience with user-friendly navigation, efficient purchasing options, and personalized user profiles.

*Welcome to [Guilty Sheep](https://guilty-sheep-d1a7abf9637c.herokuapp.com)*

![Guilty Sheep mockup]()

# **Contents**

- [**Guilty Sheep - Join the Heard**](#guilty-sheep---your-trendy-e-commerce-haven)
    - [**Introduction**](#introduction)
- [**Contents**](#contents)
- [**User Experience (UX)**](#user-experience-ux)
    - [**User Stories**](#user-stories)
    - [**Wireframes**](#wireframes)
    - [**Site Structure**](#site-structure)
  - [**Design**](#design)
- [**Features**](#features)
  - [**Existing features**](#existing-features)
  - [**Technologies Used**](#technologies-used)
- [**Testing**](#testing)
- [**Deployment**](#deployment)
- [**Credits**](#credits)
- [**Acknowledgements**](#acknowledgements)


# **User Experience (UX)**

## **User Stories**

- **Viewing and Navigation:**
    - As a user, I want to view a list of products, so I can browse through available items.
    - As a user, I want to view a specific category, collection, or artist, so I can find products that suit my preferences.
    - As a user, I want to view individual product details, so I can learn more about the item before purchasing.
    - As a user, I want to view the total of my purchases at any time, so I can keep track of my spending.
    
- **Registration and User Access:**
    - As a new user, I want to easily register, so I can create an account and start shopping.
    - As a returning user, I want to log in or log out effortlessly, so I can access my account securely.
    - As a user, I want to recover my password if forgotten, so I do not lose access to my account.
    - As a user, I want to receive an email confirmation upon registration, so I know that my account has been successfully created.
    - As a user, I want a personalized user profile, so I can view and manage my account details and purchase history.

- **Sorting and Searching:**
    - As a user, I want to sort products by various criteria (e.g., price, popularity), so I can easily find what I am looking for.
    - As a user, I want to filter products based on attributes (e.g., size, color), so I can narrow down my choices.
    - As a user, I want to search for products by keywords, so I can quickly locate specific items.
    
- **Purchasing and Checkout:**
    - As a user, I want to select a product, size, and quantity, so I can add the correct items to my cart.
    - As a user, I want to view items in my shopping bag, so I can review my selections before checkout.
    - As a user, I want to adjust the quantity or remove items from my shopping bag, so I can modify my purchase as needed.
    - As a user, I want to enter my payment information securely, so I can complete my purchase.
    - As a user, I want to see an order confirmation on the site and receive an email confirmation, so I know my order has been successfully placed.

- **Reviewing Products:**
    - As a user, I want to add a review for a product, so I can share my experience with other customers.
    - As a user, I want to see a list of my reviews in my profile, so I can keep track of the products I have reviewed.
    - As a user, I want to manage my reviews (edit or delete), so I can update or remove my feedback as necessary.

- **Admin and Moderation:**
    - As an admin, I want to manage products (add, edit, delete), so I can keep the product listings up to date.
    - As an admin, I want to manage reviews, so I can moderate content and ensure a positive user experience. 

[Back to top](#contents)


# **Deployment**

### **Project Deployment Instructions**

This website is deployed on Heroku. Follow these steps to deploy the project:

- **Local Setup**

    - **Clone the Project:** 
        - Log in to GitHub, navigate to the repository, and click on the "Code" button. Select "Open with GitHub Desktop" and follow the instructions to clone the repository locally.
    - **Install Requirements:** 
        - In your local workspace, open a terminal window and navigate to the project directory.
        - Use the command `pip3 install -r requirements.txt` to install all necessary dependencies.
    - **Set Up MongoDB:** 
        - Sign up or log in to your MongoDB account. 
        - Create a cluster and a database, then create the necessary collections: products, categories, users, orders, and reviews. 
        - Populate these collections with the appropriate data according to the project's information architecture.
    - **Create Environment Variables:**
        - Create a `.gitignore` file in the project's root directory.
        - Add `env.py` to the `.gitignore`.
        - Create the `env.py` file and define the required environment variables using the `os` module.
    - **Run the App:** 
        - In your terminal window, run the command `python3 app.py` to start the application locally.

- **Heroku Deployment:** 

    - **Set Up Local Workspace for Heroku:**
        - Generate `requirements.txt` by running `pip3 freeze --local > requirements.txt`.
        - Create a `Procfile` specifying the entry point for Heroku using the command `echo web: python app.py > Procfile`.
    
    - **Set Up Heroku:**
        - Create a Heroku account and a new app, selecting your preferred region.
        - Choose the "GitHub" deployment method and connect your repository to Heroku.
    
    - **Configure Environment Variables:**
        - In Heroku, navigate to the app's settings and find "Config Vars."
        - Enter the variables from your `env.py` file: `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `DATABASE_URL`, `EMAIL_HOST_PASS`, `EMAIL_HOST_USER`, `SECRET_KEY`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WH_SECRET` and `USE_AWS`.
    
    - **Push Files to Repository:**
        - Add and commit `requirements.txt` and `Procfile` to your Git repository.
    
    - **Automatic Deployment:**
        - In the Heroku dashboard, go to the deploy tab and enable automatic deployments.
        - Heroku will fetch the code from GitHub and deploy the app using the specified packages.
        - Click "Open app" to access the live version.

You can access the live link to the deployed version on Heroku - [https://guilty-sheep-d1a7abf9637c.herokuapp.com](https://guilty-sheep-d1a7abf9637c.herokuapp.com)

[Back to top](#contents)