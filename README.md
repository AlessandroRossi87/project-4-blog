# Schöneberg Alert

Schöneberg Alert is a digital community pinboard for the neighborhood of Schöneberg, Berlin. It is common that such community pinboards are placed at the entrace of local supermarkets, where the local authorities and inhabitants alike may post announcements, ads or requests. I decided to create a digital version for it and givit the eyecatching name of "Schöneberg Alert" inspired by the name of sensionalist tabloids newspapers. Schöneberg residents are welcome to sign up and either post an "Alert" or comment on one. My idea is the digitazation of German society at large.

## Agile Methodology

I used the Github Projects to manage the process using an agile approach.

Kanban board

User Stories

## Features

### Database Structure

### Wireframes

###

### Navbar

The navbar is fully responsive and for unauthenticated users it links to:
  - Home Page
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

- Category
- Category
- Category
- Category
- Category
- Category
- Category
- Category
- Category

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
