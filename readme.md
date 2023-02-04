# Introduction
This repository contains a python script that downloads images of artworks and their information from [WikiArt](https://www.wikiart.org/) and saves the images in a directory called images and the information in a CSV file called paintings.csv, in the working directory. The user can control the number of artists they want to download images for by changing the num_pages parameter in the function get_artists() in the main.py file.

# Requirements
To run this script, you will need the following python packages:

- `Python 3.x`

- `json`

- `csv`

- `requests`

- `os`

# Usage
1. Clone this repository to your local machine

```
$ git clone https://github.com/<your-username>/wikiart-api-data.git 
$ cd wikiart-api-data 
```
2. Install the required packages
```
$ pip install -r requirements.txt
```
3. Update the API key in the auth.py file. You can get you API key and Access key [here](https://www.wikiart.org/en/App/GetApi) 

4. Run the script
```
$ python main.py
```
5. By default the script downloads images and their metadata for 60 artists. You can increase number of artists by changing `num_pages` param of `get_artists()` method of the main module. 

# Details
The script consists of three main files: main.py, api_calls.py, and auth.py.

main.py is the entry point of the script. It calls the functions defined in api_calls.py to get the artists, paintings, and painting details from the WikiArt API and saves the images and information to disk.

api_calls.py contains the functions that make API calls to the WikiArt API to retrieve the artists, paintings, and painting details.

auth.py contains the authentication information needed to access the WikiArt API.

The user can control the number of artists they want to download images for by changing the num_pages parameter in the function get_artists() in the main.py file. By default, the script downloads images of 60 artists per page.

The script uses the WikiArt API to retrieve the data and images. WikiArt is a digital library of fine art that provides access to high-quality images and information about artworks from various cultures and time periods.

# Functionality
The script performs the following tasks:

1. Makes API calls to the endpoint to get a list of artists and their paintings.
2. Makes API calls to get the details of each painting.
3. Downloads the images of the paintings.
4. Writes the painting information to a JSON file named paintings.json.
5. Writes the painting information to a CSV file named paintings.csv.

# Conclusion
This script makes it easy to download artwork information and images from an [WikiArts'](https://www.wikiart.org/) API endpoints. By using this script, you can save time and effort in manually downloading images and information from the API endpoint. The script is simple to use and the usage instructions are provided in a friendly and detailed manner.