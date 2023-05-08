# First Section: Importing Libraries
import os
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, send_file,current_app
import zipfile



# Second Section: Declare important variables
google_image = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&"

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}

# Third Section: Build the main function
saved_folder = './static/images'


def main(search_query,to_addr,no_image):
    if not os.path.exists(saved_folder):
        os.mkdir(saved_folder)
    
    static_folder = os.path.join(current_app.root_path, 'static')

    # Define the path to the images folder
    images_folder = os.path.join(static_folder, './images')
    
    for file in os.listdir(images_folder):
        path = os.path.join(images_folder, file)
        os.remove(path)

    download_images(search_query,no_image)


    # Define the path to the output zip file
    output_zip = os.path.join(static_folder, 'images.zip')

    with zipfile.ZipFile(output_zip, 'w') as zip:
    # Iterate over the files in the images folder
        for filename in os.listdir(images_folder):
            # Get the full path to the file
            filepath = os.path.join(images_folder, filename)
            # Add the file to the zip archive
            zip.write(filepath, filename)
    
    # mail("lokeshav21@gmail.com")


# Fourth Section: Build the download function
def download_images(search_query,no_image):
    data = search_query                                     #input('What are you looking for? ')
    n_images = no_image                                     #int(input('How many images do you want? '))

    print('searching...')

    search_url = google_image + 'q=' + data

    response = requests.get(search_url, headers=user_agent)

    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.findAll('img', {'class': 'rg_i Q4LuWd'})

    count = 1
    links = []
    for result in results:
        try:
            link = result['data-src']
            links.append(link)
            count += 1
            if(count > n_images):
                break

        except KeyError:
            continue

    print(f"Downloading {len(links)} images...")

    for i, link in enumerate(links):
        response = requests.get(link)

        image_name = saved_folder + '/' + data + str(i+1) + '.jpg'

        with open(image_name, 'wb') as fh:
            fh.write(response.content)



# Fifth Section: Run your code
# if __name__ == "__main__":
#     main()