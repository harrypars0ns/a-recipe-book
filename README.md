# Primal Recipes

## Table Of Contents

- General Information
- Demo
- UX and Wireframes
- Features
- Features Left to Implement
- Technologies Used
- Testing and Validation
- Deployment
- Credits
- Acknowledgements

## Demo

A live demo of the website can be found [here](https://a-recipe-book.herokuapp.com/).


## General Information

Data Centric Development Milestone Project.

In 2019, I started a Paleo diet, a diet of whole ingredients with no processed sugars. Since January 2020 I have been following a Keto diet which has similar rules but stricter. Since starting these diets I have been at a loss for a good way to find good Paleo/Keto recipes as well as a place to keep all MY recipes together. Primal Recipes is both in one app.

This website is basically an interactive digital pocket recipe book catered towards people on a Paleo/Keto diet. It is already pre-loaded with tasty recipes so you'll never have to spend hours wondering what you are eating for dinner! The special part is the app has CRUD functionality to allow you to create, read, update and delete recipes. This makes the app useful to basically anybody that cooks.
Our recipes are all made to fit to a Paleo diet. The paleo diet is designed to replicate food that our hunter-gatherer ancestors ate thousands of years ago. While losing weight is not a goal of the Paleo diet it is a common side effect of eating so healthily.


## UX

### Strategy

I want to let people find recipes they never cooked before and recipes they create as quickly and in as few clicks as possible. Using nice visually pleasing cards that display the recipe, an image and some basic information. The site should be aesthetically pleasing, simple and professional.

The site will be a digital cookbook that is interactive and editable. 

### Scope

The function of the site will be to give users a simple way to find, create, read, update and delete Paleo/Keto recipes.
You will be able to filter the recipes by vegetarian and extra healthy options.

### Structure

The site was designed to be as user friendly as possible. I wanted to make sure that the UX was viable for people with bad eye-sight, people with dyslexia,
those who aren't comfortable using complex websites and the elderly.

The form inputs are clearly labeled and the text on the cards easily readable.

The validation lets you know if you are not inserting a complete recipe. 

The site is very intuitive so nobody will have trouble accessing all the features. Whether you are a pro-cook, rookie or just looking for somewhere to get inspiration for recipes Primal Recipes will give you no problems in your user experience. 

### Skeleton

[Wireframe plan 1 - Add/Edit Recipe Form]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/addeditrecipe.jpg)

[Wireframe plan 2 - Read Recipe Page]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/readrecipe.jpg)

[Wireframe plan 2 - Main Recipes Page]  (https://github.com/harrypars0ns/a-recipe-book/blob/master/Wireframes/recipes.jpg)

### Surface
  
I want my users to be able to look at the recipes displayed and have no trouble reading the recipe's basic information. I chose a green color scheme to play into the 'natural' brand of Primal Recipes. The simple black text is simple but still looks striking and professional. The most important thing is that the website is nice to look at for everyone including people with bad eye-sight, people with dyslexia and the elderly.

I chose to display the recipes on Materialize cards as the high quality image really elicits a positive emotional reaction.
The font sizes have been set to the biggest and most legible they can without sacrificing the usability and aesthetic of the website.

## Features

The cards are generated on beautiful Materialize cards which is a simple but visually effective way of displaying my recipes.

The app has 6 basic functions, to allow you to: display, filter create, read, update and delete recipes. The filters let you select only healthy options (users chooses what is healthy for them) and vegetarian options. Both of these are selected when adding or editing a recipe.

When adding recipes the form fields contain: the recipe name, description, cost, cooking time, cuisine (this selects the image displayed on the recipes card), ingredients separated in an array in the database and instructions/steps separated in an array in the database.

When deleting a recipe a Javascript function is run that asks for confirmation before permanently deleting from the database. This is fairly trivial and not loaded before the HTML so it is included in script tags in the HTML document.

When editing a recipe the selected recipe's information in already in the form so you don't have to update every single field when you just want to edit (for example) the description.  

The site has both frontend and backend validation, the front end uses html attributes on the inputs such as 'maxlength' and required attributes. The backend validation was done with a series of conditional statements that did not allow the recipes to be inserted into the database without the conditions being met. The conditions vary among the fields, but they usually require the field to be 'not empty' and that they dont exceed the character limit.

The read recipe pages are laid out simple to make them very easily printable. 

### Features Left to Implement

- When I have time, I would like to make: A profile data base so users could sign-in and add their own private recipes, as well as being able to favorite certain recipes. There could be a way certain admins could make certain user created recipes display on everybody's accounts.

- Another great feature to let users input the contents of their fridge and the app suggests recipes that have ingredients that the user already has.

- Vegan and Keto Filters

- Scrolling rows where each row is a different category of food eg. Brunches, Stews, Soups

- If I had a user profile database users would be able to upload their own images. 

- A database of ingredients with the macro-nutrient information would allow the app to calculate the nutritional information of a whole recipe. This would be perfect for a Keto diet.

## Technologies Used

- HTML
- CSS
- Javascript
- Python3
- Git
- Github
- Heroku deployment
- MongoDB hosts database

- [Materialize CSS](https://materializecss.com/)
    - The project uses **Materialize** **CSS** for aiding placement and responsive design plus components such as cards and the navbar.
- [Google Fonts](https://fonts.google.com/)
    - The project uses the **Google Fonts** typeface 'Exo' in varying weights and sizes.
- [jQuery](https://jquery.com/)
    - The project uses the **jQuery** to initialize some of the functions of Materialize CSS components.
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    - The project uses the **Flask** a framework for building the app.
- [Pymongo](https://pymongo.readthedocs.io/en/stable/)
    - The project uses the **Pymongo** to connect the database to the app.

## Testing
 
My first thought when choosing how the user chooses the image for each recipe was to have a text input that they would paste an image URL into. The app would check if it was a .jpg, .jpeg or .png file format and then put it on the card.
There was a couple issues with this including: some image formats are not jpg, jpeg or png so the app was rejecting perfectly good images, very annoying for the user.
Another issue was that some image links are 1000 characters long. I decided to go for a super secure system of the user selecting from a pre-determined set of images that correspond to its cuisine.

My cards used to have a reveal function that would display a short description of the recipe when you clicked the bottom half of the card. This was clunky, the page would sometimes jump when 'revealing'. The description would often be too long and spill out of the card. I binned this feature and a longer description is now available on the read recipe page. Much better UX.

The site has both frontend and backend validation, the front end uses html attributes on the inputs such as 'maxlength' and required attributes. The backend validation was done with a series of conditional statements that did not allow the recipes to be inserted into the database without the conditions being met. The conditions vary among the fields but they usually require the field to be 'not empty' and that they don't exceed the character limit.

The responsive navbar gave me more problems than it should have. It didn't open on mobile properly. This turned out not to be a html problem, but I was using jQuery syntax that was from the old version of jQuery and an old Materialize CDN. 

The brand logo in the top left of the screen created some issues on mobile. The logo is in the top left, the left margin is 50px to give it some space. On the mobile version the margin-left was putting the logo off center. This was fixed with a quick media query.

When creating the recipe_cost and recipe_time inputs, they started off as sliders that you would select the number of pounds on the cost slider and the number of minutes on the time slider. This turned out to be terrible UX and would be much improved by making the recipe_cost a dropdown with 3 price settings: £, ££ and £££ (cheap, middling, expensive).
The time slider was replaced with a simple text input, this allows the user to choose their own unit of time, hours or minutes. 

Once you'd added a recipe, the site would redirect to the main page of all recipes. I changed this so that when you insert a recipe it redirects you to the recipe page of the recipe you have just inserted.

I chose to remove the icons on the mobile version of the site which took some work as the icon elements were only hidden rather that actually not being there. To fix this I had to move all the other elements on the page to the left to make them centered on the page.

When planning how the user will input the ingredients and instructions into the database I thought I would have the user enter an ingredient in a textbox and click a button to add it to the database. This was much more complicated than needed, I ended up opting for a method where the user enters each ingredient/instruction on a new line within a textbox. The insert_recipe function splits the string on every 'new line' into an array with each line in a new index.
In the edit recipe form I do the reverse and join the indexes of the array on a new line so it looks the same as when you are adding a recipe.

All images are cropped to the same aspect ratio so they look good on all screens.

I ran the CSS and HTML through the W3C Jigsaw validator with no errors found. The Javascript was run through the JSHint validator with no major issues. The Python was ran through a validator with no issues as well as checked with pep8online.com.

I had trouble when deploying my project to Heroku after setting my environment variables 

The site works across many browsers including: Chrome, Firefox, Safari and Edge.

## Deployment

I am hosting the site on Heroku on the master branch. I had a already been committing to GitHub before.

My MongoDB SRV string and secret key is in an environment variable with .gitignore set.

I have my git repository hosted on Github and the website is hosted on Heroku. I have commits after I've finished a feature or fixed a bug. When I use git push the Github repository is updated and I use git push heroku master to push the updates to Heroku.

To deploy on Heroku you have to:
Create an app on the main page of your Heroku dash.
Go to settings, press 'reveal config vars' I used IP (0.0.0.0), PORT (5000), Secret Key and MongoDB URI string.
Gitpod has Heroku already installed so just use 'heroku login' in your terminal.
Add a requirements.txt with 'pip3 freeze > requirements.txt'.
Add a Procfile with 'echo web: python app.py > Procfile'.

If you want to run the code locally you can use 'git clone'. Alternatively you 
can download all the files in a .zip file and open 'index.html' in your browser of choice.

## Credits

### Content

I built the Nav, form, buttons and cards using Materialize. 
All HTML, CSS and Javascript and Python was written by me. 

### Media
I used Pexels (stock images) for my images, and font awesome for my icons .

### Acknowledgements

- Thanks to Brian Macharia for all the help he's given me making this. Couldn't have done it without you.
- Thanks to Luca from CodeInstitute for help with environment variables.
