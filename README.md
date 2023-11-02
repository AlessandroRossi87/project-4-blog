# Schöneberg Alert

Schöneberg Alert is a digital community pinboard for the neighborhood of Schöneberg, Berlin. It is common that such community pinboards are placed at the entrace of local supermarkets, where the local authorities and inhabitants alike may post announcements, ads or requests. I decided to create a digital version for it and give it the eyecatching name of "Schöneberg Alert" inspired by the name of sensionalist tabloid newspapers. Schöneberg residents are welcome to sign up and either post an "Alert" or comment on one. My idea is the digitazation of German society at large.

![Responsive mockup]()

[Link to deployed website](https://project4-pinboard-1c32e796b2e1.herokuapp.com/)

## User-Experience-Design

## Strategy

### Site Goals

The site is aimed at the local community of a particular neighborhood, in this case Schöneberg in Berlin. It is a way for people to keep up on local events or problems of their daily life in the neighborhood. The website should be as intuitive as possible, giving the user the feeling of being part of the community they reside in.

Originally the website would have been catered to two different kind of users: business accounts and private accounts. The admin would have had to approve the business accounts since they woudl have needed to proof that they owned a small business within the limits of Schöneberg. Due to time constrigements I decided to focus only on the private accounts.

<details>
<summary><strong>Original Site Logic</strong></summary>

![Original Site Logic](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/sitelogic.png)

</details>

I used the Github Projects to manage the process using an agile approach. I created user stories and assigned them to two categories: "Must have" and "Can have"

<details>
<summary><strong>Kanban Board</strong></summary>

![Kanban Board](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/kanban.png)

</details>

## Features

<details>
<summary><strong>Database Structure</strong></summary>

![Database structure](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/database.png)

</details>

<details>
<summary><strong>Wireframes</strong></summary>

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/indexwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/signloginwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/alertwf.png)

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

- Home Pag
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

When the user clicks on a category only posts related to that category are shown. In order to reset the filter the user clicks on "clear" button

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

</details>

### Future Features

## Testing

## Validators

### HTML & CSS

## Deployment

## Run Locally

## Credits

## Acknowledgments
