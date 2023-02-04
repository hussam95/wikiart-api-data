import json
import csv
import requests
import os
from auth import *
from api_calls import *

# Get working dir
working_dir = os.getcwd()

#Get artists 60 per page; change num_pages to control how many artists you want to download images for
artists = get_artists(artists_endpoint, num_pages=1)

# Get painting ids
paintings_data_all_artists = get_paintings(artists, paintings_by_artists_endpoint)

# Get painting details
complete_data_all_artists = get_painting_details(paintings_data_all_artists, paintings_endpoint)

# Load the JSON data
with open("paintings.json", "r") as f:
    artworks = json.load(f)

# Create a directory to store the images
if not os.path.exists("images"):
    os.makedirs("images")
os.chdir("images")

# Loop over the artworks and save the images and write to CSV
artworks_data = []
header = ["id", "artist name", "title", "year", "image", "tags", "gallery", "media", "sizeX", "sizeY"]
for index, artwork in enumerate(artworks):
    id = artwork["id"]
    image_url = artwork["image"]
    image_download_fails = save_image(image_url, id)
    print(f"\r{index+1}/{len(artworks)} downloading images . . .", end="")
    if image_download_fails:
        continue
        
    else:
        artwork_data = {
            "id": id,
            "artist name": artwork.get("artistName", ""),
            "title": artwork["title"],
            "year": artwork["completitionYear"],
            "sizeX": artwork["sizeX"],
            "sizeY": artwork["sizeY"],
            "image": f"{id}.{image_url.split('.')[-1]}",
            "tags": ",".join(artwork.get("tags", [])),
            "gallery": ",".join(artwork.get("galleries", [])),
            "media": ",".join(artwork.get("media", []))
            
        }
        artworks_data.append(artwork_data)
os.chdir(working_dir)
write_to_csv(artworks_data, header)