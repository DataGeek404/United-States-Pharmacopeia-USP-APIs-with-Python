import requests

def get_sms_delivery_report(api_key, email, request_id):
    url = "https://api.umeskiasoftwares.com/api/v1/smsdelivery"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": api_key,
        "email": email,
        "request_id": request_id
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# Example usage:
api_key = "VE5MTlkzRk06MTlwNjlkZWM="
email = "kibejay61@gmail.com"
request_id = "8403414672158573510"

response = get_sms_delivery_report(api_key, email, request_id)
print(response)