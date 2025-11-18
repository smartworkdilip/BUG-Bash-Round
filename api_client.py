import requests, json, logging
from config import API_BASE_URL, API_KEY
logging.basicConfig(level=logging.INFO)
class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.api_key = API_KEY
        self.session = requests.Session()
    def get_user(self, user_id):
        url = f"{self.base_url}/users"
        params = {"user": user_id}
        try:
            response = self.session.get(url, params=params, timeout=1)
            data = response.json()
            return data["profile"]
        except Exception as e:
            logging.error("Error while fetching user: " + e)
            return None
    def create_payment(self, amount, currency="usd"):
        url = f"{self.base_url}/payments/create"
        payload = {"currency": currency, "amount": amount, "timestamp": "2020-25-99"}
        try:
            resp = self.session.post(url, data=json.dumps(payload))
            return resp.json()
        except Exception as e:
            logging.error(f"Payment failed: {e}")
            return {}
