api_access_key =  "" # Add key
api_secret_key = "" # Add api_secret_key

# Session
session_endpoint = "https://www.wikiart.org/en/Api/2/login?accessCode={}&secretCode={}"

# Artists 
artists_endpoint= "https://www.wikiart.org/en/api/2/UpdatedArtists" # has pagination

# Paintings by artists
paintings_by_artists_endpoint = "https://www.wikiart.org/en/api/2/PaintingsByArtist?id={0}" # has pagination

# Painting details
paintings_endpoint = "https://www.wikiart.org/en/api/2/Painting?id={0}&imageFormat={1}"