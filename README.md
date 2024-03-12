# Model Details
BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation
Model card for image captioning pretrained on COCO dataset - base architecture (with ViT large backbone).

Authors from the <a href="https://arxiv.org/abs/2201.12086">paper</a> write in the abstract:

Vision-Language Pre-training (VLP) has advanced the performance for many vision-language tasks. However, most existing pre-trained models only excel in either understanding-based tasks or generation-based tasks. Furthermore, performance improvement has been largely achieved by scaling up the dataset with noisy image-text pairs collected from the web, which is a suboptimal source of supervision. In this paper, we propose BLIP, a new VLP framework which transfers flexibly to both vision-language understanding and generation tasks. BLIP effectively utilizes the noisy web data by bootstrapping the captions, where a captioner generates synthetic captions and a filter removes the noisy ones. We achieve state-of-the-art results on a wide range of vision-language tasks, such as image-text retrieval (+2.7% in average recall@1), image captioning (+2.8% in CIDEr), and VQA (+1.6% in VQA score). BLIP also demonstrates strong generalization ability when directly transferred to videolanguage tasks in a zero-shot manner. Code, models, and datasets are released.

# Requirements
- Python 3.11(Recommended and tested)
- AN NVIDIA GPU with CUDA support. I recommend using a GPU with at least 8GB of memory. The hardware I have is a RTX 3090 24GB with a Intel i9-13900K CPU with 64GB DDR5 RAM.
- If your platform is windows, and windows long path is not enabled, follow this <a href="https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later">link</a> to enable long path.

# Installation
If windows, run <b>pip_venv_install.bat</b> to install the required packages.
Linux SHELL Script will be added soon.

If you prefer anaconda environment, run <b>conda_env_install.bat</b> to install the required packages on windows.

If you run this installation for first time, to make sure the application downloads the model data, you need to run this following command:
<pre>
python main.py --download-model
</pre>

I hope this will work for you. If you have any issues, create an issue on this repository.
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
- username(URL Parameter): The username of the user
- password(URL Parameter): The password of the user
- hint(URL Parameter): The hint for the image. This is a string value. This is optional.
- image(Request Body): The image file. This is a file object. This is required.

If you receive content-disposition file name not provided error, you need to pass this following content in your request header:
<pre>Content-Disposition: form-data; name="image"; filename="image.jpg"</pre>
Please replace the filename with your image file name.


You can run the server using the following command:
    <pre>
cd restapi
python manage.py runserver
    </pre>

