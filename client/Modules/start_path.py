import requests
import globals
from get_start import get_start


def send_data(url, start, end, compass):
    data = {"START": start, "END": end, "COMPASS": compass}
    response = requests.post(url, json={"data": data})
    return response.status_code, response.text


if __name__ == "__main__":
    url = "http://192.168.10.12:80"
    start = get_start()
    end = (0, 4)
    compass = 3

    status_code, response_text = send_data(url, start, end, compass)
    print(f"Status Code: {status_code}")
    print(f"Response: {response_text}")
