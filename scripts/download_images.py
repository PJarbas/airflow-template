import requests
import urllib.request
from datetime import date

"""
Dowload Dog images
"""

def get_images(file_name):
    """[summary]

    Args:
        file_name ([str]): [name fo the image file]
    """
    base_url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url=base_url)
    image_url = response.json()["message"]
    
    # save the image
    urllib.request.urlretrieve(image_url, file_name)


if __name__ == "__main__":
    
    file_name = f"data/dog_{date.today().strftime('%Y-%m-%m')}.jpg"
    
    get_images(file_name=file_name)
    
    print("Dowload of the images ok!")