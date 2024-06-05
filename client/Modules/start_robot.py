import requests
from Modules.get_start import get_start
from Modules import globals


def send_data(url, start, end, compass):
    data = {"START": start, "END": end, "COMPASS": compass}
    response = requests.post(url, json={"data": data})
    return response.status_code, response.text


def start_robot():
    url = globals.esp32_IP
    start = globals.start
    end = globals.end
    compass = globals.compass

    status_code, response_text = send_data(url, start, end, compass)
    print(f"Status Code: {status_code}")
    print(f"Response: {response_text}")
