import os
import requests
from urllib.parse import urlparse

def download_image(url, folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Extract the image file name from the URL
        parsed_url = urlparse(url)
        image_name = os.path.basename(parsed_url.path)
        
        # Create the folder if it doesn't exist
        os.makedirs(folder, exist_ok=True)
        
        # Define the full path to save the image
        image_path = os.path.join(folder, image_name)
        
        # Write the image to the folder
        with open(image_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Downloaded {url} to {image_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def download_images_from_list(url_list, folder):
    for url in url_list:
        download_image(url, folder)

if __name__ == "__main__":
    # Example list of image URLs
    image_urls = [
        "https://www.google.com/search?sca_esv=be3262f3292e4708&sca_upv=1&sxsrf=ADLYWIJ9RyJ2rP-E6alixgMFNRNgxxbQEQ:1725350229146&q=image&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2jpXXSZVlK6C0YPjHbsLu8HQlFjXJu4aVhI_llTnXJ4lFAWdNYSKl18X_OYOML0jevhpDEumYRwaaY1jEa7vKdTgiN-XUHVrwULe1SBpdZ2b2Qdf9JCr6vszwGWtXx6BBaAiRVuZU26XGXcLhLP1MT26u-HDMw&sa=X&ved=2ahUKEwjOx5W8pqaIAxV1MdAFHeV2JO4QtKgLegQIFhAB&biw=1536&bih=695&dpr=1.25#vhid=tYmxDgFq4MrkJM&vssid=mosaic",
        "https://www.google.com/search?sca_esv=be3262f3292e4708&sca_upv=1&sxsrf=ADLYWIJ9RyJ2rP-E6alixgMFNRNgxxbQEQ:1725350229146&q=image&udm=2&fbs=AEQNm0Aa4sjWe7Rqy32pFwRj0UkWd8nbOJfsBGGB5IQQO6L3J_86uWOeqwdnV0yaSF-x2jpXXSZVlK6C0YPjHbsLu8HQlFjXJu4aVhI_llTnXJ4lFAWdNYSKl18X_OYOML0jevhpDEumYRwaaY1jEa7vKdTgiN-XUHVrwULe1SBpdZ2b2Qdf9JCr6vszwGWtXx6BBaAiRVuZU26XGXcLhLP1MT26u-HDMw&sa=X&ved=2ahUKEwjOx5W8pqaIAxV1MdAFHeV2JO4QtKgLegQIFhAB&biw=1536&bih=695&dpr=1.25#vhid=B_ypq20yGKrazM&vssid=mosaic",
        # Add more URLs here
    ]
    
    # Folder to save the images
    save_folder = "downloaded_images"
    
    download_images_from_list(image_urls, save_folder)
