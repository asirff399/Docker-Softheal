# SoftHeal - Donation Site 

#### This is my Django project, built using Django Rest Framework (DRF). The project is a Donation Platform that provides users with various features to explore and donate where they want. Key functionalities included:
---
## Admin

- Admin can log in and log out.
- Admin can manage the dashboard.
- Admin can manage profile.
- Admin can add, edit, and delete any post.

## User

- Users can register, log in, and log out.
- Users can donate.
- User can review the post he/she donated.
- User can filter post category-wise.

## Features

### Authentication

- New users can register on the platform using their email. An activation link is sent to their email to verify and activate their account, ensuring a secure onboarding process.

### Donation

- Users can browse available projects for donation, view detailed post information, and donate through a simple and intuitive process.

### Post Filtering

- User can easily filter posts by categories to smooth their search for specific posts.

### Profile Management

- Each user has a personal profile page where they can:

     ⚡ View their account information and balance.
  
     ⚡ They can update info from here.
    
     ⚡ View their donation history.

### Donation History

- Here displays the user's donation history.

### Admin Controls

- Administrators have full access to manage the platform. They can add, edit, and delete any posts, ensuring the smooth operation and integrity of the.

### Volunteer

- There was a volunteer register form. Where anyone can send a request to join us as a volunteer.

### Admin Controls

- Admin can see and manage important data, and edit or delete data but it not complete yet. I work on it and as soon as possible complete this.

## API Endpoints

- ### Account

      POST /account/list
      POST /account/review
  
      POST /account/register
      POST /account/login
      POST /account/logout
      POST /account/pass_change
      POST /account/create_review
      PUT /account/update_profile

- ### Post

      POST /post/list
      POST /post/type
      POST /post/donation
      POST /post/add
      PUT /post/details/<int:pk>
      Delete /post/details/<int:pk>
  
- ### Others

      POST /service
      POST /contact_us
      POST /team
      PUT /transaction/deposit
      PUT /transaction/withdraw



## 💻 Technology: 

- Django
- Django Rest Framework (DRF)
- PostgreSQL
- etc.

---

## 🌐 Deployment: API Deployed using Vercel.
API Live link: 

    https://github.com/asirff399/SoftHeal

## GitHub!
Front-end Repo: 

    https://github.com/asirff399/SoftHeal

Front-end live link:

    https://softheal.netlify.app

    

