# Schöneberg Alert

Schöneberg Alert is a digital community pinboard for the neighborhood of Schöneberg, Berlin. It is common that such community pinboards are placed at the entrace of local supermarkets, where the local authorities and inhabitants alike may post announcements, ads or requests. I decided to create a digital version for it and give it the eyecatching name of "Schöneberg Alert" inspired by the name of sensionalist tabloid newspapers. Schöneberg residents are welcome to sign up and either post an "Alert" or comment on one. My idea is the digitazation of German society at large.

![Responsive mockup](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/mockup.png)

[Link to deployed website](https://project4-pinboard-1c32e796b2e1.herokuapp.com/)

## Table of Contents

- [Schöneberg Alert](#schöneberg-alert)
  - [Table of Contents](#table-of-contents)
  - [User-Experience-Design](#user-experience-design)
  - [Strategy](#strategy)
    - [Site Goals](#site-goals)
    - [Design](#design)
  - [Agile methodology](#agile-methodology)
  - [Technologies](#technologies)
    - [Django Packages](#django-packages)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)
  - [Testing](#testing)
    - [Accessibility](#accessibility)
    - [Solved bugs](#solved-bugs)
  - [Validators](#validators)
    - [Lighthouse Report](#lighthouse-report)
  - [Deployment](#deployment)
  - [Development](#development)
  - [Credits](#credits)
  - [Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

## User-Experience-Design

## Strategy

### Site Goals

The site is aimed at the local community of a particular neighborhood, in this case Schöneberg in Berlin. It is a way for people to keep up on local events or problems of their daily life in the neighborhood. The website should be as intuitive as possible, giving the user the feeling of being part of the community they reside in.

Originally the website would have been catered to two different kind of users: business accounts and private accounts. The admin would have had to approve the business accounts since they woudl have needed to proof that they owned a small business within the limits of Schöneberg. Due to time constrigements I decided to focus only on the private accounts.

### Design

I used the five planes of User Experience to plan the development of this project:

**Strategy**

The strategy for this project is to create a digital platform where people living in the same community can share important information, administrative notices, complaints etc. on an intuitive platform. I have often expressed the wish of being more aware of what is going on in my neighborhood, and Schöneberg Alert is the answer to my wishes.

**Scope**

The scope has been set to enabling the users to post different "Alerts" and the possibility to comment on each other's so that they can stay connected with their neighbors.

**Structure**

The structure of the website is simple and intuitive, there should be a list of posts, or Alerts, and the possibility to see more of one particular post.

**Skeleton**

A skeleton structure has been created with help of Wireframes

<details>
<summary><strong>Wireframes</strong></summary>

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/indexwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/signloginwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/alertwf.png)

</details>

**Surface**

The surface provides soft colors in different shades of grey, white, light blue, light green and red. The colors of text has been checked for contrast. Buttons have been colored either blue or red for better recognizton. The simple layout is thought for older users who might not be accostumed to new technologies.

The fonts chosen, Lato and Roboto, give a familiar yet institutional flair to the website.

![Color Scheme](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/colors.png)

<details>
<summary><strong>Original Site Logic</strong></summary>

![Original Site Logic](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/sitelogic.png)

</details>

## Agile methodology

I used the Github Projects to manage the process using an agile approach. I created user stories and assigned them to two categories: "Must have" and "Can have".

[User Stories](https://github.com/users/AlessandroRossi87/projects/4)

<details>
<summary><strong>Kanban Board</strong></summary>

![Kanban Board](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/kanban.png)

</details>

## Technologies

- HTML has been used for the structure of the website
- Bootstrap has been used for styling the website
- CSS has been used for customizing style
- JavaScript has been user the internal messages and the hamburger menu on narrow screens
- Python has been used within the Django Framework
- Codeanywhere has been used as IDE fror development of the website
- GitHub repository has been used for hosting the code
- Font Awesome has been used for the bell icon, aka the logo
- Favicon.io has been used for the favicon
- ElephantSQL has been used as database solution
- Cloudinary has been used to store media files

### Django Packages

The following Django packages have been installed for this project:

asgiref==3.7.2
cloudinary==1.36.0
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==3.2.22
django-allauth==0.57.0
django-crispy-forms==1.14.0
django-summernote==0.8.20.0
gunicorn==21.2.0
oauthlib==3.2.2
psycopg2==2.9.9
PyJWT==2.8.0
python3-openid==3.2.0
pytz==2023.3.post1
requests-oauthlib==1.3.1
sqlparse==0.4.4
whitenoise==5.3.0

## Features

<details>
<summary><strong>Database Structure</strong></summary>

CRUD functionality has been applied through the database for authenticated users. A user can post an Alert, read it, edit it and delete it.

![Database structure](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/database.png)

</details>

<details>
<summary><strong>Logo</strong></summary>

I created a corporate identity for this website by using a red bell icon from FontAwesome nested between the two words that constitute the website's name. The same red bell can be found as the default image for the alerts.

![Logo](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/logo.png)

![Default Picture](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/default.png)

</details>

### Existing Features

<details>
<summary><strong>Navbar</strong></summary>

The navbar is fully responsive and for unauthenticated users it links to:

- Home Page
- Sign Up Page
- Log In Page

![Unauthenticated Navbar](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/unauthnav.png)

For authenticated users it links to:

- Home Page
- Post an Alert page
- Sign Out Page

![Authenticated Navbar](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/authnav.png)

The navbar menu transforms into an hambuger menu in narrow screens.

![Hamburger Navbar](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/hamburger.png)

</details>

<details>
<summary><strong>Footer</strong></summary>

The footer is fully responsive and same as the navbar for unauthenticated users it liks to:

- Home Page
- Sign Up Page
- Log In Page

![Unauthenticated footer](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/unauthfooter.png)

For authenticated users it liks to:

- Home Page
- Post an Alert page
- Sign Out Page

![Authenticated footer](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/authfooter.png)

The footer also contains liks to social media websites, which open up in a new window

</details>

<details>
<summary><strong>Index Page</strong></summary>

The Index Page extends the base and includes the following sections:

**Hero section**

The hero section features an Image from a street fair in Schöneberg which reflects the neighborhood's diversity, it also features an intro text explaining the goals of this website.

![Hero section](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/hero.png)

**Category filter**

Each Alert can be filtered by its category. There are 9 categories available for the user to choose:

- Business Recommendations
- Environment
- Events
- Health & Wellness
- Housing
- Lost & Found
- News & Updates
- Safety
- Traffic & Transportation

![Categories](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/categories.png)

When the user clicks on a category only posts related to that category are shown. In order to reset the filter the user clicks on "clear" button.

![No Alerts](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/noalerts.png)

If no Alerts are available for a certain category a message is displayed and an extra button to clear the categories and display all alerts.

**Alert section**

This sections lists all the Alerts posted by users. It shows the picture, either from the user or a default one, the title, the date and time of posting, the number of likes and comments, the author and the category. The user can click on the title to read the Alert in detail.

![Alert section](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/postlist.png)

</details>

<details>
<summary><strong>Post an Alert Page</strong></summary>

The page extends the base and it shows the Django form for posting a new Alert. The template is also used for editing the posts. For new Alerts the header reads "Post an Alert" whereas for editing it reads "Edit an Alert". The submit button a the end reads "Submit" for new Alerts or "Update" for editing Alerts.

![Post an Alert](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/newalert.png)

</details>

<details>
<summary><strong>Alert Detail Page</strong></summary>

The page shows the Alert with its text on the left and the picture on the right on wide screens. The user can read the text and, if authenticated, they can like the alert or leave a comment. The comments need to be approved by the Admin in order to avoid hate speech.

![Post Detail](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/postdetail.png)

If the user is the author of the Alert two buttons will be visible to them in order to Edit or Delete the post

![Edit Delete](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/editdeletebtns.png)

</details>

<details>
<summary><strong>Edit Alert Page</strong></summary>

The page enables the author of the Alert to modify their post. They can modify al fields in the post.

![Edit Alert](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/edit.png)

</details>

<details>
<summary><strong>Delete Alert Page</strong></summary>

Defensive design has been applied to this website. If the author of an Alert desires to delete their Alert they are redirected to this page where they can confirm or cancel the deletion.

![Delete Alert](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/delete.png)

</details>

<details>
<summary><strong>Register Page</strong></summary>

The page allows the user to sign up by creating a username and a password. The page includes a link to the Login Page in case the user has already an account.

![Post Detail](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/register.png)

</details>

<details>
<summary><strong>Login Page</strong></summary>

The page allows the user to log in to their account in order to post, like or comment an Alert. The page includes a link to the Register Page in case the user does not have an account.

![Login Page](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/login.png)

</details>

<details>
<summary><strong>Logout Page</strong></summary>

When the user clicks on "Logout" they are redirected to the Logout page where they are asked to confirm if they want to log out:

![Logout Page](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/logout.png)

</details>

<details>
<summary><strong>Custom Error Pages</strong></summary>

Custom Error Pages have been created for error 400, 403, 404 and 500.

![404 error](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/404.png)

</details>

### Future Features

- Possibility for users to create a private or business account

- Each user should be able to have a profile

- Each user should be able to message other users

- Private user should be able to log in with other social media accounts, like Google

- Possibility to geo-locate an Alert with Google Maps embedding.

- Possibility for users to edit or delete a comment

- Possibility to unlike an Alert after having liked it

## Testing

<details>
<summary><strong>Manual Testing</strong></summary>

| Register Page         | Results                                           |
| --------------------- | ------------------------------------------------- |
| Username required     | Text field left empty gives error message         |
| Password required     | Text field left empty gives error message         |
| Password confirmation | If password does not match it gives error message |
| Register button       | It validates registration and logs in the user    |

| Login & Logout | Results                                                                                                                           |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Login          | Registered user is able to log in with username and password. If user tries to log in without credentials, error message is shown |
| Logout         | Logout page visible only to logged in users. It asks for confirmation to log out                                                  |
| Logout button  | It logs out the user and redirects to Home Page where a message confirms successfull logout                                       |

| Post, Edit, Delete Alert | Results                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------- |
| Title required           | Text field left empty gives error message                                               |
| Image not required       | If left empty a default image is shown                                                  |
| Content required         | Text left empty gives error message                                                     |
| Category required        | If no category is selectet it gives error message                                       |
| Edit button              | Only author of Alert is shown this button. It redirects the user to the Edit Alert page |
| Edit fields              | User is able to modify all fields in Alert and change the image                         |
| Delete button            | Only author of Alert is shown this button. It directs the user to the Delete Alert page |
| Delete Alert Page        | It shows the user a button to confirm deletion and one to cancel deletion               |
| Delete Alert button      | It deletes the Alert and redirects the user to the Home Page                            |
| Cancel Delete button     | It redirects the user back to the Alert Detail Page                                     |
| Alert Detail Page        | If user clicks on Alert Title it redirects to the Alert Detail Page                     |

| Comment & Like   | Results                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Read comments    | All users are able to read comments in the Alert Detail Page            |
| Post a comment   | Only logged in users are able to post a comment                         |
| Submit button    | A message informs them that the comment needs Admin approval            |
| Approve comments | Only Superuser is able to approve or reject comments from Admin Site    |
| Like button      | Only logged in users are able to like an Alert in the Alert Detail page |

| Nagivation links | Results                                                                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Logo             | User clicks on the Logo and is redirected to Home Page                                                                                                          |
| Home             | User clicks on "Home" and is redirected to Home Page                                                                                                            |
| Login            | A logged out user is redirected to Login page                                                                                                                   |
| Logout           | A logged in user is redirected to Logout page                                                                                                                   |
| Register         | A logged out user is redirected to Register Page                                                                                                                |
| Post an Alert    | A logged in user is redirected to Post an Alert Page                                                                                                            |
| Social media     | Social media icons open up in a new tab                                                                                                                         |
| Category filter  | User clicks on a category and only the relative Alerts are shown. If no Alert for that category a message informs the user and invites them to clear the filter |
| Mobile menu      | On narrow screens the user clicks on the hamburger icon to open the navigation bar                                                                              |

</details>

### Accessibility

I used [Wave Accessibility](https://wave.webaim.org/) to check for accessibility testing. I have focused on correcting the color contrasts to meet the minimum ratio. Also I have made sure to provide Aria Labels throughout the website to ensure assistive technology such as screen readers. All pictures have an alternative text describing them.

### Solved bugs

Originally the feature to edit the featured image for an Alert was not working. I modified the widget for the featured image in the NewPostForm to ClearableFileInput and the bug was solved.

![Edit Featured Image](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/imgupdatebug.png)

## Validators

The Index Page, Alert Detail Page, Register Page, Post an Alert Page were run through the [W3 HTML Validator](https://validator.w3.org/). There were some errors for trailing slash, misuse of Aria Labels, stray tags and some p elements as child of ul elements and missing alt attributes for images. I was able to correct most of the errors beside the trailing slashes because they happen authomatically in the IDE environment I am using (Codeanywhere) and the alt attributes for the images uploaded through Cloudinary.

<details>
<summary><strong>HTML</strong></summary>

![CSS validator](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/htmlvalidator.png)

</details>

The website was run through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and passed with no errors found.

<details>
<summary><strong>CSS</strong></summary>

![CSS validator](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/cssvalidator.png)

</details>

The website's script.js contained one function and it was run through the [JSHint JavaScript Validator](https://jshint.com) and passed with just one warning indicating that the code is using ES6 features.

<details>
<summary><strong>JavaScript</strong></summary>

![JavaScript validator](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/jsvalidator.png)

</details>

Python PEP8 style convention was checked with the [CI Python Linter](https://pep8ci.herokuapp.com/) and it returned a few syntax error due to the Python version compatibility. I amended the lines of codes and all custom made Python files (views.py urls.py models.py forms.py) passed without errors.

<details>
<summary><strong>PEP8</strong></summary>

![views.py](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/viewspep8.png)

![urls.py](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/urlspep8.png)

![models.py](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/modelspep8.png)

![forms.py](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/formspep8.png)

</details>

### Lighthouse Report

The Lighthouse Report showed first some area of improvements for Accessibility and CEO. I added a few more Aria-labels to images and added meta description and was able to have all the values above 90.

![Lighthouse Report](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/lighthouse.png)

## Deployment

The website uses [ElephantSQL](https://www.elephantsql.com/) for its database.

- I signed up with my GitHub account
- I created a new instance
- The free plan was selected
- I selected Europe as region
- Once created I was able to access the url and password for the database

The website uses [Cloudinary](https://cloudinary.com/) for storing media files

- I created an account in Cloudinary
- I signed in
- I copied the API environment variable

The website was deployed to [Heroku](https://heroku.com/) by following these steps:

- I created an account in Heroku
- Once logged in, I created a new app
- Inside the app I went to the settings tab to reveal configuration vars
- I added the following configuration vars: CLOUDINARY_URL, DATABASE_URL, PORT, SECRET_KEY
- I went to the deploy tab and connected the GitHub repository
- I went to Manual deploy and chose Main branch
- I clicked on deploy

## Development

Developers interested in this website can clone/fork this repository for local development:

- Go to the [GitHub Repository](https://github.com/AlessandroRossi87/project-4-blog)
- Click the fork button on the top right of the page
- You have now created a duplicate of the project in your GitHub repository

## Credits

- This website was built by following the walkthrough project Django Blog by Code Institute.
- Styling with CSS was inspired by this tutorial on [Youtube](https://www.youtube.com/watch?v=INIW731cxIo&t=1510s)
- The images for the Alerts are my private property.
- The hero image comes from [GetYourGuide](https://cdn.getyourguide.com/img/tour/95204b7993d5f8aa.jpeg/145.jpg)
- Code for Slugify was taken from [FullStackPythn.com](https://www.fullstackpython.com/django-utils-text-slugify-examples.html)
- Code for custom 404 page was taken from [Stackoverflow](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page)
- Code for defensive design for deliting an Alert was taken from [Stackoverflow](https://stackoverflow.com/questions/31843145/deleteview-with-confirmation-template-and-post-method)
- Styling the django form was ispired by this tutorial on [Youtube](https://www.youtube.com/watch?v=6-XXvUENY_8)
- Code for editing the featured image was taken from [Programtalk.com](https://programtalk.com/python-examples/django.forms.ClearableFileInput/?utm_content=cmp-true)

## Acknowledgments

I would like to thank my class coordinator Kay, former alumni Armando Urquiola Cabrera and my newly appointed mentor Gareth McGirr for their support and help through this project.
