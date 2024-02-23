import sys

from loader.Predictor import ImageCaptionGenerator as cpgen


def run_ai(message):
    print(f"Hi {message}!")

    # ask user to input an image URL
    img_url = input("Please input a image URL/Absolute Path(Should be accessible without auth): ")

    cp = cpgen(img_url)

    print(cp.predict_with_hint("A photograph of"))


# Method that loads the model, intended to be called for the first time installation
def load_model():
    # import ModelInitilizar
    from loader.ModelInitilizar import load_model
    # Show the message
    print("Downloading and Loading the model, please wait...")
    # load the model
    load_model()


if __name__ == '__main__':

    # check if --download-model is passed
    if '--download-model' in sys.argv:
        load_model()
    else:
        run_ai(", Welcome to the Image Captioning AI!")
