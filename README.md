The Project description will be updated shortly.

# Installation
If windows, run <b>pip_venv_install.bat</b> to install the required packages.
Linux SHELL Script will be added soon.

If you prefer anaconda environment, run <b>conda_env_install.bat</b> to install the required packages on windows.

# Creating a user to allow access to the server
To create a user, run the following command:
<pre>
cd restapi
python manage.py createsuperuser
</pre>

# Running the server

The server has the following post mapping:

1: /api/v1/image_descriptor_ai/ - This is the main endpoint for the server. 
It accepts a POST request with username, password, hint, and an image file as request body. 
The server then run inference on the image and returns the result as a JSON response.

This following parameters are required for the POST request:
- username: The username of the user
- password: The password of the user
- hint: The hint for the image. This is a string value. This is optional.
- image: The image file. This is a file object. This is required.

If you receive content-disposition file name not provided error, you need to pass this following content in your request header:
<pre>Content-Disposition: form-data; name="image"; filename="image.jpg"</pre>
Please replace the filename with your image file name.


You can run the server using the following command:
    <pre>
cd restapi
python manage.py runserver
    </pre>

    
