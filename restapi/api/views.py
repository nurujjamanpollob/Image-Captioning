import os
from datetime import datetime

from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView


# Run AI model to describe the image, and send the result as json response
def run_ai_model(file_path):
    parent_directory = os.path.abspath('..')
    # Add the parent directory to the system path
    os.sys.path.append(parent_directory)
    # Import the AI model
    from loader.Predictor import ImageCaptionGenerator as cpgen
    cp = cpgen(file_path)
    result = cp.predict()

    # Remove the file from disk
    os.remove(file_path)
    # remove the last path
    os.rmdir(os.path.dirname(file_path))
    # return the result
    return result


# Run AI Model to describe the image, and send the result as json response. It accepts a hint
def run_ai_model_with_hint(file_path, hint):
    parent_directory = os.path.abspath('..')
    # Add the parent directory to the system path
    os.sys.path.append(parent_directory)
    # Import the AI model
    from loader.Predictor import ImageCaptionGenerator as cpgen
    cp = cpgen(file_path)
    result = cp.predict_with_hint(hint)

    # Remove the file from disk
    os.remove(file_path)
    # remove the last path
    os.rmdir(os.path.dirname(file_path))
    # return the result
    return result


def check_files_and_save(request, json_response):
    # get total files count
    total_files = len(request.FILES)
    # if no files are uploaded, or more than 1 file are uploaded add an error to the json response
    if total_files == 0:
        json_response['error'] = 'No files were uploaded'
    elif total_files > 1:
        json_response['error'] = 'Only one file can be uploaded at a time'
    else:
        # Get the file from the request
        file = request.FILES['file']
        # Save the file to disk
        file_path = ImageDescriptorAIView.saveFileToDisk(file, file.name)
        # return file path
        return file_path


class ImageDescriptorAIView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        hint = request.query_params.get('hint')
        json_response = {}

        # Determine if the user is authenticated
        user = authenticate(username=username, password=password)

        # If the user is not authenticated, add an error to the json response
        if user is None:
            json_response['error'] = 'User is not authenticated'
            return JsonResponse(json_response)
        else:
            # Try save the file to disk and run the AI model, it may throw an error
            try:
                # Save the file to disk
                file_path = check_files_and_save(request, json_response)
                # Run the AI model and return the result, check if a hint was provided
                if hint is not None:
                    response = run_ai_model_with_hint(file_path, hint)
                else:
                    response = run_ai_model(file_path)

                json_response['result'] = response
                return JsonResponse(json_response)
            except Exception as e:
                json_response['error'] = str(e)
                return JsonResponse(json_response)

    # Write file to disk, accept the file from api, write the file to disk, and return the file absolute path
    @staticmethod
    def saveFileToDisk(file, file_name):
        # Save file to current directory/input-files/image_descriptor_ai/currentdaytime/input-file.extension
        file_path = os.path.join(
            os.getcwd(),
            'input-files',
            'image_descriptor_ai',
            str(datetime.now().strftime('%Y%m%d%H%M%S%f')),
            file_name)
        # Create directory if it does not exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        # Write file to disk
        with open(file_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Verify file was written to disk
        if not os.path.exists(file_path):
            raise IOError('File was not written to this path: ' + file_path)

        # Return file path
        return file_path
