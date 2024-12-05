# Frontend Engineering Website - Django
## Author
👤 **Nilo Cara**
<!-- ----------------------------------------------------------------------------
  * @Website     Django and TailwindCSS Website - Frontend Software Engineering  
  * @framework   Django - High-level Python web framework with TailwindCSS and 
  * @author      Nilo Cara - Frontend Software Engineering
  * @copyright   Copyright (c) 2024, Nilo Cara
  * @link        https://niloc95.github.io/niloc95
  * @since       v4.03.24
  * ---------------------------------------------------------------------------- -->
* Website: https://frontend.co.za
* Website: https://about.frontend.co.za
* Twitter: [@CodeCara](https://twitter.com/CodeCara)
* GitHub: [@niloc95](https://github.com/niloc95)
* LinkedIn: [@https:\/\/www.linkedin.com\/in\/nilo-cara\/](https://linkedin.com/in/https:\/\/www.linkedin.com\/in\/nilo-cara\/)
* Date: April 2024

### Production Setup
* Hosting: AWS and AWS Lightsail
* Build - AMI Linux Django Package


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

### Files Missing
 * .env
 * wsgi.py
 * asgi.py
 * Static files, images, videos, png, svg's...etc


## How To Secure Nginx with Let's Encrypt on Ubuntu
* Introduction
 **  Let’s Encrypt is a Certificate Authority (CA) that provides an accessible way to obtain and install free TLS/SSL certificates, thereby enabling encrypted    HTTPS on web servers. It simplifies the process by providing a software client, Certbot, that attempts to automate most (if not all) of the required steps. Currently, the entire process of obtaining and installing a certificate is fully automated on both Apache and Nginx.

In this tutorial, you will use Certbot to obtain a free SSL certificate for Nginx on Ubuntu and set up your certificate to renew automatically.

This tutorial will use a separate Nginx server configuration file instead of the default file. We recommend creating new Nginx server block files for each domain because it helps to avoid common mistakes and maintains the default files as a fallback configuration.

* Prerequisites
  To follow this tutorial, you will need:

  One Ubuntu server set up by following this initial server setup for Ubuntu tutorial, including a sudo-enabled non-root user and a firewall.

  A registered domain name. This tutorial will use example.com throughout. You can purchase a domain name from Namecheap, get one for free with Freenom, or use the domain registrar of your choice.

  Both of the following DNS records set up for your server. 

  An A record with example.com pointing to your server’s public IP address.
  An A record with www.example.com pointing to your server’s public IP address.
  Nginx installed by following How To Install Nginx on Ubuntu. Be sure that you have a server block for your domain. This tutorial will use /etc/nginx/sites-available/example.com as an example.

* Step 1 — Installing Certbot
    Certbot recommends using their snap package for installation. Snap packages work on nearly all Linux distributions, but they require that you’ve installed snapd first in order to manage snap packages. Ubuntu comes with support for snaps out of the box, so you can start by making sure your snapd core is up to date:

  ```sh
  sudo snap install core; sudo snap refresh core
  ```

  If you’re working on a server that previously had an older version of certbot installed, you should remove it before going any further:

  ```sh
  sudo apt remove certbot
  ```
  After that, you can install the certbot package:
  ```sh
  sudo snap install --classic certbot
  ```
  Finally, you can link the certbot command from the snap install directory to your path, so you’ll be able to run it by just typing certbot. This isn’t necessary with all packages, but snaps tend to be less intrusive by default, so they don’t conflict with any other system packages by accident:

  ```sh
  sudo ln -s /snap/bin/certbot /usr/bin/certbot  
  ```
  Now that we have Certbot installed, let’s run it to get our certificate.

* Step 2 — Confirming Nginx’s Configuration
    Certbot needs to be able to find the correct server block in your Nginx configuration for it to be able to automatically configure SSL. Specifically, it does this by looking for a server_name directive that matches the domain you request a certificate for.

    If you followed the server block set up step in the Nginx installation tutorial, you should have a server block for your domain at /etc/nginx/sites-available/example.com with the server_name directive already set appropriately.

    To check, open the configuration file for your domain using nano or your favorite text editor:
  ```sh
  sudo nano /etc/nginx/sites-available/example.com
  ```
  Find the existing server_name line. It should look like this:
  /etc/nginx/sites-available/example.com
  ...
  server_name example.com www.example.com;
  ...
  
  If it does, exit your editor and move on to the next step.

  If it doesn’t, update it to match. Then save the file, quit your editor, and verify the syntax of your configuration edits:
  ```sh
  sudo nginx -t
  ```

  If you get an error, reopen the server block file and check for any typos or missing characters. Once your configuration file’s syntax is correct, reload Nginx to load the new configuration:
  ```sh
  sudo systemctl reload nginx
  ```
  Certbot can now find the correct server block and update it automatically.

  Next, let’s update the firewall to allow HTTPS traffic.

* Step 3 — Allowing HTTPS Through the Firewall
    If you have the ufw firewall enabled, as recommended by the prerequisite guides, you’ll need to adjust the settings to allow for HTTPS traffic. Luckily, Nginx registers a few profiles with ufw upon installation.

    You can see the current setting by typing:
  ```sh
  sudo ufw status
  ```
    It will probably look like this, meaning that only HTTP traffic is allowed to the web server:
      Output
        Status: active

        To                         Action      From
        --                         ------      ----
        OpenSSH                    ALLOW       Anywhere                  
        Nginx HTTP                 ALLOW       Anywhere                  
        OpenSSH (v6)               ALLOW       Anywhere (v6)             
        Nginx HTTP (v6)            ALLOW       Anywhere (v6)
  
  To additionally let in HTTPS traffic, allow the Nginx Full profile and delete the redundant Nginx HTTP profile allowance:

  ```sh
  sudo ufw allow 'Nginx Full'
  sudo ufw delete allow 'Nginx HTTP'
  ```
  Your status should now look like this:
  ```sh
  sudo ufw status
  ```
        Output
        Status: active

        To                         Action      From
        --                         ------      ----
        OpenSSH                    ALLOW       Anywhere
        Nginx Full                 ALLOW       Anywhere
        OpenSSH (v6)               ALLOW       Anywhere (v6)
        Nginx Full (v6)            ALLOW       Anywhere (v6)
  Next, let’s run Certbot and fetch our certificates.

* Step 4 — Obtaining an SSL Certificate
   Certbot provides a variety of ways to obtain SSL certificates through plugins. The Nginx plugin will take care of reconfiguring Nginx and reloading the config whenever necessary. To use this plugin, type the following: 
  ```sh
  sudo certbot --nginx -d example.com -d www.example.com
  ```
  This runs certbot with the --nginx plugin, using -d to specify the domain names we’d like the certificate to be valid for.

  When running the command, you will be prompted to enter an email address and agree to the terms of service. After doing so, you should see a message telling you the process was successful and where your certificates are stored:
  
  Output
    IMPORTANT NOTES:
    Successfully received certificate.
    Certificate is saved at: /etc/letsencrypt/live/your_domain/fullchain.pem
    Key is saved at: /etc/letsencrypt/live/your_domain/privkey.pem
    This certificate expires on 2022-06-01.
    These files will be updated when the certificate renews.
    Certbot has set up a scheduled task to automatically renew this certificate in the background.

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    If you like Certbot, please consider supporting our work by:
    * Donating to ISRG / Let's Encrypt: https://letsencrypt.org/donate
    * Donating to EFF: https://eff.org/donate-le
  
  Your certificates are downloaded, installed, and loaded, and your Nginx configuration will now automatically redirect all web requests to https://. Try reloading your website and notice your browser’s security indicator. It should indicate that the site is properly secured, usually with a lock icon. If you test your server using the SSL Labs Server Test, it will get an A grade.

  Let’s finish by testing the renewal process.

* Step 5 — Verifying Certbot Auto-Renewal
    Let’s Encrypt’s certificates are only valid for ninety days. This is to encourage users to automate their certificate renewal process. The certbot package we installed takes care of this for us by adding a systemd timer that will run twice a day and automatically renew any certificate that’s within thirty days of expiration.

    You can query the status of the timer with systemctl:
  ```sh
  sudo systemctl status snap.certbot.renew.service
  ```
      Output
        ○ snap.certbot.renew.service - Service for snap application certbot.renew
            Loaded: loaded (/etc/systemd/system/snap.certbot.renew.service; static)
            Active: inactive (dead)
        TriggeredBy: ● snap.certbot.renew.timer

  To test the renewal process, you can do a dry run with certbot:
  ```sh
  sudo certbot renew --dry-run  
  ```

  If you see no errors, you’re all set. When necessary, Certbot will renew your certificates and reload Nginx to pick up the changes. If the automated renewal process ever fails, Let’s Encrypt will send a message to the email you specified, warning you when your certificate is about to expire.
