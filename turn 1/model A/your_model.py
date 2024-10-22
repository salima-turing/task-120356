import requests

BASE_URL = "http://example.com"

def authenticate(username, password):
	url = f"{BASE_URL}/api/login"
	response = requests.post(url, json={"username": username, "password": password})
	if response.status_code == 200:
		return response.json().get("token")
	else:
		return None

def get_data(token):
	url = f"{BASE_URL}/api/data"
	headers = {"Authorization": f"Bearer {token}"}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		return response.json()
	else:
		return None

if __name__ == "__main__":
	token = authenticate("dummyuser", "dummypassword")
	if token:
		data = get_data(token)
		print("Data:", data)
	else:
		print("Authentication failed.")
