# Frontend Engineering Website - Django
## Author
👤 **Nilo Cara**
<!-- ----------------------------------------------------------------------------
  * @Website     Django and Bootstrap Website - Frontend Software Engineering  
  * @framework   Django - High-level Python web framework with Bootstrap5 and Crispy Forms
  * @author      Nilo Cara - Frontend Software Engineering
  * @copyright   Copyright (c) 2023, Nilo Cara
  * @link        https://niloc95.github.io/niloc95
  * @since       v1.0
  * ---------------------------------------------------------------------------- -->
* Website: https://frontend.co.za
* Website: https://about.frontend.co.za
* Twitter: [@CodeCara](https://twitter.com/CodeCara)
* GitHub: [@niloc95](https://github.com/niloc95)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/nilo-cara\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/nilo-cara\/)
* Date: October 2023
### Production Setup
* Hosting: AWS and AWS Lightsail
* Build - Bitnami Linux Django Package




## Setup
Local hosting(On Personal Computer)
Install Python
* Windows - https://python.land/installing-python#Install_Python_on_Windows
* MacOs - https://python.land/installing-python#Installation_on_MacOS
* Linux - https://python.land/installing-python#Install_Python_on_Linux

### GitHub Setup (Optional)
To push your Django project to GitHub, follow these steps:

### 1. Create a GitHub Repository:
If you haven't already, go to GitHub (https://github.com/) and create a new repository by clicking the "+" icon in the upper right corner and selecting "New repository."

### 2. Repository Name and Description:
Choose a name for your repository and provide an optional description. You can make the repository public or private, depending on your preferences and GitHub plan.

### 3. Initialize with a README (Optional):
You can choose to initialize your repository with a README file. This is optional but can be helpful for providing information about your project.

### 4. Create Repository:
Click the "Create repository" button to create your new GitHub repository.

### 5. Set Up Git on Your Local Machine:
If you haven't already, configure Git with your name and email address:
```sh
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```
### 6. Add Git Remote:
In your Django project directory, add the GitHub repository as a remote. Replace <your-github-username> and <your-repository-name> with your GitHub username and repository name
```sh
git remote add origin https://github.com/github-username/your-repository-name.git
```
### 7. Commit Your Changes:
Stage and commit your project files to Git:
```sh
git add .
git commit -m "Initial commit"
```
### 8. Push to GitHub:
Push your project to the GitHub repository:
```sh
git push -u origin master
```
### Django Project Setup

Setting up a Django project involves several steps, including installing Django, creating a project directory, setting up a virtual environment, and creating a Django project within that environment. Here's a step-by-step guide to help you set up a Django project:

### 1. Prerequisites:
Ensure you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/. 

### 2. Create a Virtual Environment (Optional):
It's recommended to create a virtual environment to isolate your project dependencies. This step is optional but highly recommended to avoid conflicts between different projects.
```sh
# Create a virtual environment (replace 'myenv' with your preferred name)
python -m venv myenv

# Activate the virtual environment (Windows)
myenv\Scripts\activate

# Activate the virtual environment (macOS/Linux)
source myenv/bin/activate
```
### 3. Install Django:
With your virtual environment activated, you can now install Django using pip:
```sh
pip install django
```
### 4. Create a Django Project:
Now, let's create a Django project. Replace "myproject" with your project name:
```sh
django-admin startproject myproject
```

### 5. Navigate to Your Project Directory:
Go to your project directory:
```sh
cd myproject
```
### 6. Database Setup:
By default, Django uses SQLite as the database for development purposes. You can change the database settings in the settings.py file later if needed.

### 7. Run Migrations:
Initialize the database by running migrations:
```sh
python manage.py migrate
```
### 8. Create a Superuser (Admin User):
You can create an admin user to manage your Django application:
```sh 
python manage.py createsuperuser
# Follow the prompts to set a username, email, and password for the admin user.
```
### 9. Start the Development Server:
You can start the Django development server to test your project:
```sh
python manage.py runserver 
# to server port just type the port number: e.g "python manage.py runserver 9000"
```
This will start the server at http://localhost:8000/.

### 10. Access the Admin Panel:
Open your web browser and go to http://localhost:8000/admin/. Log in using the superuser credentials you created earlier to access the Django admin panel.

### 11. Create Apps (Optional):
You can create Django apps within your project to organize your code. To create an app, use the following command:
Replace "myapp" with your desired app name.
Note: An "app" can encompass a wide range of functionalities. For instance, on your website, you might have various components such as a blog, a form, or a community forum, and each of these could exist as a separate sub-domain. For example, you could have blog.frontend.co.za, forum.frontend.co.za, or an e-commerce shop at shop.frontend.co.za.
```sh
python manage.py startapp myapp
```

### Important Note for Production Git Write Access

If you encounter authentication issues when trying to push or pull from your GitHub repository, you may need to set the correct remote URL using a personal access token. This is how it should look:

```sh 
# git remote set-url origin https://PASTE_YOUR_GITHUB_TOKEN_HERE@github.com/niloc95/Frontend
git remote set-url origin https://ghp_XXXXB5Q3q50ISZ25cBgX5F9XVBGBTTYTYERER@github.com/niloc95/Frontend
```
Replace YOUR_GITHUB_TOKEN with your actual GitHub personal access token. This token should have the necessary permissions to read and write to the repository. You can create a personal access token in your GitHub account settings following these steps:

* 1. Go to your GitHub account settings.
* 2.Select "Developer settings" from the left-hand menu.
* 3.Click on "Personal access tokens."
* 4.Generate a new token with the required permissions.
* 5.Copy the token and use it in the git remote set-url command as shown above.
* 6.Make sure to keep your personal access token secure and do not share it in your public repository or with unauthorized individuals.

