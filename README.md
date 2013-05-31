# vLine Django Example

The vLine Django Example shows you how to create a Django app that is integrated with the vLine API.

# Getting Started

1. Sign up for a [vLine developer account] (https://vline.com/developer/) and create your vLine service.
1. Install Django and PyJWT: `sudo pip install Django PyJWT`
1. Clone this repository.
1. Set up the database: `python manage.py syncdb` (create a superuser when prompted)
1. Run the server: `python manage.py runserver 8080`
1. In your browser, go to [http://localhost:8080/admin/](http://localhost:8080/admin/)
1. Add at least one additional user.
1. Open [http://localhost:8080](http://localhost:8080) in one regular browser window and one incognito window.
1. Log in as different users in the two windows.
1. Click on a username to call that user.

