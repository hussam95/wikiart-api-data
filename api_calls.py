import requests
from collections import defaultdict
import json
import csv

def get_session_key(session_endpoint):
    """
    Function to retrieve session key from a session endpoint using HTTP GET request.

    Parameters:
    session_endpoint (str): The endpoint URL where the session key can be retrieved.

    Returns:
    str: The session key.

    Raises:
    requests.exceptions.RequestException: If there is any exception while making the GET request.
    """
    # Make a GET request to the session endpoint
    response = requests.get(session_endpoint)
    
    # Extract JSON data from the response
    data = response.json()
    
    # Get the session key from the data
    session_key = data['SessionKey']
    
    return session_key

def get_artists(artists_endpoint, num_pages):
    """
    Function to retrieve artists information from the artists endpoint using HTTP GET request.

    Parameters:
    artists_endpoint (str): The endpoint URL where the artists information can be retrieved.
    num_pages (int): Number of pages to fetch artists from. There are 60 artists per page.

    Returns:
    list: A list of dictionaries, where each dictionary contains information about an artist.

    Raises:
    requests.exceptions.RequestException: If there is any exception while making the GET request.
    """
    pagination_dic = defaultdict(list)
    for i in range(num_pages):
        if i ==0:
            # Make a GET request to the artists endpoint
            response = requests.get(artists_endpoint)
            # Extract JSON data from the response
            data = response.json()
            # Store pagination token in the dictonary to crawl artist pages
            pagination_dic[f'pagination_token_{i}'] = data['paginationToken']
            pagination_dic[f'has_more_{i}'] = data['hasMore']
            # Get the data about artists from the data
            artists = data['data']
        else:
            # Send new request with the pagination token
            paginated_response = requests.get(artists_endpoint+f"?paginationToken={pagination_dic[f'pagination_token_{i-1}']}")
            next_page_data = paginated_response.json()
            for artist in next_page_data['data']:
                artists.append(artist)
            has_more = next_page_data['hasMore']
            if has_more:
                pagination_dic[f'pagination_token_{i}'] = next_page_data['paginationToken']
                pagination_dic[f'has_more_{i-1}'] = next_page_data['hasMore']
            else:
                break 
    
    # Convert artists' list of dictionaries to JSON format
    data_json = json.dumps(artists)

    # Write JSON data to a file in the working directory to save artists
    with open("artists.json", "w") as f:
        f.write(data_json)
    return artists

def get_paintings(artists, paintings_by_artists_endpoint):
    paintings_data_all_artists = []
    for index, artist in enumerate(artists):
        artist_id = artist['id']
        response = requests.get(paintings_by_artists_endpoint.format(artist_id))
        paintings_by_artist  = response.json()
        paintings_data = paintings_by_artist['data']
        for painting in paintings_data:
            paintings_data_all_artists.append(painting)
        has_more = paintings_by_artist['hasMore']
        pagination_token = paintings_by_artist['paginationToken']
        if has_more:
            paginated_response = requests.get(paintings_by_artists_endpoint.format(artist_id)+f"&paginationToken={pagination_token}")
            more_paintings = response.json()
            more_data = more_paintings['data']
            for painting in more_data:
                paintings_data_all_artists.append(painting)
        print(f"\r{index+1}/{len(artists)} getting artists . . .", end="")
    return paintings_data_all_artists


def get_painting_details(paintings_data_all_artists,paintings_endpoint):
    complete_data_all_artists = []
    for index, painting in enumerate(paintings_data_all_artists):
        painting_id = painting['id']
        response = requests.get(paintings_endpoint.format(painting_id, 'jpg'))
        paintings_data = response.json()
        complete_data_all_artists.append(paintings_data)
        
        # Convert paintings' list of dictionaries to JSON format
        paintings_data_json = json.dumps(complete_data_all_artists)
    
        # Write JSON data to a file in the working directory to save paintings
        with open("paintings.json", "w") as f:
            f.write(paintings_data_json)
        print(f"\r{index+1}/{len(paintings_data_all_artists)} getting metadata . . .", end="")
  
    return complete_data_all_artists

def save_image(url, id):
    """
    Saves an image from a given URL with the given ID.
    """
    image_download_fails = bool
    response = requests.get(url)
    if response.status_code == 200:
        format = url.split(".")[-1]
        with open(f"{id}.{format}", "wb") as f:
            f.write(response.content)
        return False
    else:
        # Handle image download fails
        image_download_fails = True
    return image_download_fails


def write_to_csv(data, header):
    """
    Writes data to a CSV file with the given header.
    """
    with open("artworks.csv", "w", newline="", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)