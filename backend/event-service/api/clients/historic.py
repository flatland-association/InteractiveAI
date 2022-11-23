import requests
import json
from settings import HISTORIC_SERVICE
import logging

class HistoricClient:
    def __init__(self) -> None:
        self.base_url = HISTORIC_SERVICE

    def create_trace(self, event_data):
        url = f"{self.base_url}/api/v1/traces"
        payload = json.dumps({
            "data": event_data,
            "step": "EVENT",
            "use_case": event_data["use_case"],
            "date": event_data["date"]
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        logging.error(response.json())
        response.raise_for_status()
        