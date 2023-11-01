# Schöneberg Alert

Schöneberg Alert is a digital community pinboard for the neighborhood of Schöneberg, Berlin. It is common that such community pinboards are placed at the entrace of local supermarkets, where the local authorities and inhabitants alike may post announcements, ads or requests. I decided to create a digital version for it and give it the eyecatching name of "Schöneberg Alert" inspired by the name of sensionalist tabloid newspapers. Schöneberg residents are welcome to sign up and either post an "Alert" or comment on one. My idea is the digitazation of German society at large.

![Responsive mockup]()

## User-Experience-Design

## Strategy

### Site Goals

The site is aimed at the local community of a particular neighborhood, in this case Schöneberg in Berlin. It is a way for people to keep up on local events or problems of their daily life in the neighborhood. The website should be as intuitive as possible, giving the user the feeling of being part of the community they reside in.

Originally the website would have been catered to two different kind of users: business accounts and private accounts. The admin would have had to approve the business accounts since they woudl have needed to proof that they owned a small business within the limits of Schöneberg. Due to time constrigements I decided to focus only on the private accounts.

I used the Github Projects to manage the process using an agile approach. I created user stories and assigned them to two categories: "Must have" and "Can have"

![Kanban Board](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/kanban.png)

## Features

### Database Structure

![Database structure](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/database.png)

### Wireframes

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/indexwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/signloginwf.png)

![Wireframes](https://github.com/AlessandroRossi87/project-4-blog/blob/main/docs/images/alertwf.png)

### Logo

I created a corporate identity for this website by using a red bell icon from FontAwesome nested between the two words that constitute the website's name. The same red bell can be found as the default image for the alerts.


### Navbar

The navbar is fully responsive and for unauthenticated users it links to:
  - Home Pag
  - Sign Up Page
  - Log In Page

For authenticated users it links to:
  - Home Page
  - Post an Alert page
  - Sign Out Page

### Footer

The footer is fully responsive and same as the navbar for unauthenticated users it liks to:
  - Home Page
  - Sign Up Page
  - Log In Page

For authenticated users it liks to:
  - Home Page
  - Post an Alert page
  - Sign Out Page

The footer also contains liks to social media websites, which open up in a new window

### Index Page

The Index Page extends the base and includes the following sections:

**Hero section**

The hero section features an Image from a street fair in Schöneberg which reflects the neighborhood's diversity, it also features an intro text explaining the goals of this website.

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

When the user clicks on a category only posts related to that category are shown. In order to reset the filter the user clicks on "clear" button

**Alert section**

This sections lists all the Alerts posted by users. It paginates authomatically if the section includes a number of posts divisible by 3.

### New Post Page

The page extends the base and it shows the Django form for posting a new Alert. The template is also used for editing the posts. For new Alerts the header reads "Post an Alert" whereas for editing it reads "Edit an Alert". The submit button a the end reads "Submit" for new Alerts or "Update" for editing Alerts.

### Post Detail Page

The page shows the Alert with its text and a comment field below.

### Sign Up page

### Log In page

### Log Out Page

## Testing

## Validators

### HTML & CSS

## Deployment

## Run Locally

## Database schema

## Credits

## Acknowledgments 
