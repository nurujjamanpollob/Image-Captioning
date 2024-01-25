from transformers import BlipProcessor, BlipForConditionalGeneration

isModelLoaded: bool = False
"""
Class that invoked to load the model from the provided path and run
"""

processor = None
model = None


def load_model():
    # update the global variable of processor and model
    global processor, model, isModelLoaded
    # set the value of processor and model
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda")
    # set the value of isModelLoaded
    isModelLoaded = True


# Get the model
def get_model():
    # check if model is loaded
    if not isModelLoaded:
        # load the model
        load_model()
    # return the model
    return model


# Get the processor
def get_processor():
    # check if model is loaded
    if not isModelLoaded:
        # load the model
        load_model()
    # return the model
    return processor
