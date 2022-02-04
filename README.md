
![image of am I responsive](media/AmIResponsive.JPG)

# Dia-Eaties Recipe blog
This project is a recipe blog dedicated to low carb and low sugar meals for diabetics, its very difficult to find suitable recipes for diet requirements in the vast sea of recipes online so I felt this site would be nice to have to have everything compiled into a singular space.
I followed the recipe blog for the project development.

## Features
The blog features a number of interacvitiy for the user, it includes the option to
- register
- login
- logout
- create a recipe for logged in users
- like recipes
- leave comments
- read about page
- Profile page
- {future-feature} Pop ups for diabetic slang


### User Account

- Login signout and registration 
![image of login](/media/sign-in.JPG)
![image of signout](media/sign-out.JPG)
![image of signup](media/sign-up.JPG)
 

### Comments

- Comments section for users to interact
![image of comments](media/comment.JPG)


### Create Recipe

- Create a recipe for registered users so users can be part of the webiste experience
![image of create recipe](media/create-recipe.JPG)


### Like Function

- Like function for recipes 
![image of likes](media/like.JPG)

### Contact us 

- Contact page for users to get in touch with us 
![image of contact page](media/contact-us.JPG)

### Navbar
Navbar for user to navigate website
![image of nav ](media/nav.JPG)

### Footer 
- The the website footer with link to personal github
![image of footer](media/footer.JPG)

### About us
- This page gives the user information on what the page is about
![image of about page](media/about-us.JPG)

### Profile
- This is a profile section which has three sections, the published recipes that are visible on the homepage, the draft which is only visible on their profile page and recipes they loved will also display so they can keep track 
![image of profile](media/profile.JPG)

### Update/Delete
- Logged in user can delete or update their recipe 
![image of update and delete](media/update.delete.JPG)

 **Features left to add**

- I would like add more sections to split up the recipes e.g breakfast section, dinner section etc
- I would like to add more resources to organisations that deal with diabetic diets
- Add a more colouful or tasteful section for the ingredients and instructions part of the recipes
- Have pop ups to explain diabetic wording and slang
- There are many things I would like to add in terms of functionality and the overall look

## Program Structure

- This is the original Wireframe for the Dia-Eaties recipe blog

![image of the text flow chart for the project](media/Wireframe.png)
me
- The final result has not changed much lading to the final project 
- The number of recipes has been decreased to two compared to the orginal four 


## Testing

 - I tested the admin approval for comments and recipes, all features work as expected
 - I tested the sign in, register and signout process for the user and admin, all features work as expected
 - I tested the basic functionality of the page. e.g the responsiveness, all features work as expected
 - I tested the process to allow a registered user to create a recipe and post it to the homepage, all features work as expected
 - I tested comment approval within the admin section, all features work as expected
 - I tested the profile page, all features work as expected
 - I had users to test the website (make their own profile, recipe etc), all features work as expected
 - I tested the app in my mobile, desktop and devtools, everything appeared to look up to standard on devtools

### Errors

  - The main error I faced was missing module docsctring and class docstring - these weren't picked up by the PEP8 validator so it is considered clean code. However I'd like to address this in the future when I have time.
  - Another error was the line is too long error which again I could not fix in all cases as it distrupted the code 


### Validator Testing 

- I used PEP8 to validate my python code, the only errors remaining are a couple of line too long errors 

- I used https://validator.w3.org/ to validate html
![image of validator](media/error-free-css.JPG)

- I used https://jigsaw.w3.org/css-validator/ to validate CSS
![image of validator](media/error-free-css.JPG)

- I used https://jshint.com/ to validate Javascript
![image of validator](media/js-works.JPG)

## Deployment 

This project was deployed through Heroku in the following steps:

- A repository was created in github using the student template
- The repo was pushed to the cloud based IDE called GITPOD
- In the GITPOD terminal, django and its supporting libraries were installed using pip3
- The project is then created using using python3 manage.py startproject projectname
- The first app is then created using python3 manage.py createapp appname
- The app is then registered in the setting file in the project level settings.py.
- An app is the created in heroku and the installation of postgres is done under
resources making sure to add postgres url to config vars
- Back in the GITPOD terminal, install Django Database and psycopg2
- Import dj database url in your settings file and replace default database with dj database passing it postgres url
- Migrate database and load data in gitpod terminal
- Create another super user
- Create an if else statement that checks the database url and runs the correct database accordingly.
- Install gunicorn, create a procfile and log into heroku in the terminal.
- Disable the static files using heroku config:set, DISABLE_COLLECTSTATIC=1 --app appname
- Add heroku app and localhost to allowed hosts in settings.py
- Generate a secret key using Django secret key generator and add to config vars whilst linking it to settings.py
- Add, commit and push changes to Github
- Set heroku to automatically deploy but setting it to Github and searching/connecting to correct repo.

  The live links to my project are - 
   - https://8000-diabekki-diaeaties2-a2zlno4cqy0.ws-eu30.gitpod.io/
   - https://dia-eaties-2.herokuapp.com/

   Link to User-Stories project section
   - https://github.com/Diabekki/Dia-eaties-2/projects/1



## Acknowledgements

I want to thank my Fiance who kept pushing me to keep bettering myself and not letting me give up and for giving me advice on how to get the readme to sound more structured and professional.
Fellow students for letting me vent frustrations when I felt overwhelmed with the work.
Kasia who keeps up our morale and always checks to see if we are doing okay, she keeps us going through all of this. 



