####  A photo gallery web application.

## User Story
* View different photos that interest them
* Click a single image to expand it and view the details of that photo
* Search for different categories
* Copy a link to the photo to share with my friends.


## Author
[Erastus Njoroge](https://github.com/indomitable-core/), 11/10/2021.

## Description
A photo gallery web application made using Django.

## Technologies Used
* Python 3.8.10
* Django 3.2.7
* Postgres
* HTML5  
* CSS
* Javascript
* jQuery 
* Bootstrap 4


## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install django==3.2.7`**
* This project requires you to have a secret key from Uploadcare to facilitate cloud storage of uploaded images.
    * The secret key can be gotten by creating a free uploadcare account, starting a new project and navigating to the dashboard
    * The key should be stored as an environmental variable in an .env file as shown below
        * **`SECRET=<your secret key here>`**
    * More info on how to use the Django pyuploadcare library can be found [here](https://uploadcare.com/docs/guides/django/)

## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/indomitable-core/Gallery`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
* **Step 5** : You can now launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    * To post photos, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.


## Known Bugs
* None at the momment, report any by contacting me

## Support and contact details
You can provide feedback or raise any issues/ bugs through the following means:
* eramwangiz@gmail.com

## Live Site link
You can view the live application by following this [link]().

## License
#### [*GNU License*](LICENSE)