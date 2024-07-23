import requests

def send_sms(api_key, email, sender_id, message, phone):
    url = "https://api.umeskiasoftwares.com/api/v1/sms" //replace with your actual URL
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "api_key": api_key,
        "email": email,
        "Sender_Id": sender_id,
        "message": message,
        "phone": phone
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        result = response.json()
        if result['ResultCode'] == 'Error':
            print(f"API Error: {result['errorMessage']}")
        else:
            return result
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Example usage:
api_key = "VE5MTlkzRk06MTlwNjlkZWM="
email = "kibejay61@gmail.com"
sender_id = "UMS_SMS"
message = "UMS SMS Api Test Message"
phone = "0769002525"

response = send_sms(api_key, email, sender_id, message, phone)
print(response)
