from loader.Predictor import ImageCaptionGenerator as cpgen


def run_ai(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # ask user to input an image URL
    img_url = input("Please input a image URL(Should be accessible without auth): ")

    cp = cpgen(img_url)

    print(cp.predict_with_hint("A photograph of"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_ai('Welcome to Image caption system by Nurujjaman Pollob')
