# vLine Django Example

The vLine Django Example shows you how to create a Django app that is integrated with the vLine API.

# Getting Started

1. Sign up for a [vLine developer account] (https://vline.com/developer/) and create your vLine service.
1. Make note of your `API Secret` on the `Service Settings` tab in the [vLine Developer Console](https://vline.com/developer/app/).
1. Install Django and PyJWT (version 0.1.5 or newer): `sudo pip install "Django" "PyJWT>=0.1.5"`
1. Clone this repository.
1. Set up the database: `python manage.py syncdb` (create a superuser when prompted)
1. Open `vline_example/vline.py` and replace `API_SECRET` with the secret from the previous steps. Also replace
`SERVICE_ID` with the name of your service.
1. Run the server: `python manage.py runserver 8080`
1. In your browser, go to [http://localhost:8080/admin/](http://localhost:8080/admin/)
1. Add at least one additional user.
1. Open [http://localhost:8080](http://localhost:8080) in one regular browser window and one incognito window.
1. Log in as different users in the two windows.
1. Click on a username to call that user.

