
import requests

def get_random_dog_image():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Random Dog Image URL:", data["message"])
    else:
        print("Failed to fetch dog image!")

if __name__ == "__main__":
    get_random_dog_image()

