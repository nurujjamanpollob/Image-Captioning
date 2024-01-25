import os

import requests

import loader.ModelInitilizar as modelInitilizar
from PIL import Image
# import binary io
from io import BytesIO as bytesIo

"""
    Class used to predict the caption of the image
    TODO: Add the image caption generator
"""


class ImageCaptionGenerator:
    image_url: str = None
    image_bytes: bytesIo = None
    image_path: str = None
    caption_hint: str = None
    mode_initialized: int = 0

    """
    It initialize with the image bytes and caption hint. pass None if no hint is provided
    @:param image_bytes: The bytes of the image
    """

    def __init__(self, image_bytes: bytesIo):
        self.image_bytes = image_bytes
        self.mode_initialized = 2

    """
    It initialize with the image path and caption hint. pass None if no hint is provided
    @:param image_path: The path of the image
    """

    def __init__(self, image_path_or_url: str):
        # initilialize image path if not url(http or https)
        if image_path_or_url.startswith("http://") or image_path_or_url.startswith("https://"):
            self.image_url = image_path_or_url
            self.mode_initialized = 1
        else:
            self.image_path = image_path_or_url
            self.mode_initialized = 3

    """
    Runs prediction on the image and returns the caption. It does not accept any hint.
    
    It usages cuda to run the prediction on GPU.
    """

    def predict(self):
        processor = modelInitilizar.get_processor()
        model = modelInitilizar.get_model()

        # if mode_initialized is 0 (class not initialized with constructor)
        # raise an error
        if self.mode_initialized == 0:
            raise Exception("Class not initialized with constructor. Initialize with constructor first")

        # if mode_initialized is 1 (class initialized with image_url)
        # load the image from the url
        if self.mode_initialized == 1:
            self.image_bytes = requests.get(self.image_url, stream=True).raw

            # invoke private method to predict
            return self.__getImageCaption(processor, model, self.image_bytes, None)

        # if mode_initialized is 2 (class initialized with image_bytes)
        # invoke private method to predict
        if self.mode_initialized == 2:
            return self.__getImageCaption(processor, model, self.image_bytes, None)

        # if mode_initialized is 3 (class initialized with image_path)
        # invoke private method to predict
        if self.mode_initialized == 3:
            return self.__getImageCaption(processor, model, self.__load_bytes_from_path(), None)

    """
    Runs prediction on the image and returns the caption. It accepts a hint.
    @:param hint: The hint to be used for caption generation. Pass None if no hint is provided.
    
    It usages cuda to run the prediction on GPU.
    """

    def predict_with_hint(self, hint: str):
        processor = modelInitilizar.get_processor()
        model = modelInitilizar.get_model()

        # if mode_initialized is 0 (class not initialized with constructor)
        # raise an error
        if self.mode_initialized == 0:
            raise Exception("Class not initialized with constructor. Initialize with constructor first")

        # if mode_initialized is 1 (class initialized with image_url)
        # load the image from the url
        if self.mode_initialized == 1:
            self.image_bytes = requests.get(self.image_url, stream=True).raw

            # invoke private method to predict
            return self.__getImageCaption(processor, model, self.image_bytes, hint)

        # if mode_initialized is 2 (class initialized with image_bytes)
        # invoke private method to predict
        if self.mode_initialized == 2:
            return self.__getImageCaption(processor, model, self.image_bytes, hint)

        # if mode_initialized is 3 (class initialized with image_path)
        # invoke private method to predict
        if self.mode_initialized == 3:
            return self.__getImageCaption(processor, model, self.__load_bytes_from_path(), hint)


    def __getImageCaption(self, processor, model, image_bytes, hint):
        raw_image = Image.open(image_bytes).convert('RGB')
        if hint is None:
            inputs = processor(raw_image, return_tensors="pt").to("cuda")
        else:
            inputs = processor(raw_image, hint, return_tensors="pt").to("cuda")

        out = model.generate(**inputs)
        return processor.decode(out[0], skip_special_tokens=True)

    def __load_bytes_from_path(self):
        # First try to check if the path is existing
        if not os.path.exists(self.image_path):
            raise Exception("Image path does not exists at: " + self.image_path)

        # Read the image bytes
        return open(self.image_path, "rb")
