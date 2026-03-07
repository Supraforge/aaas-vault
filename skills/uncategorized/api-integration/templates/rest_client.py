# Template: Generic REST API client (reference only)
from typing import Any

import requests


class RESTClient:
    """Generic REST API client with authentication support."""

    def __init__(self, base_url: str, auth_header: dict[str, str] | None = None):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if auth_header:
            self.session.headers.update(auth_header)

    def get(self, endpoint: str, params: dict | None = None) -> Any:
        """Make a GET request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict | None = None) -> Any:
        """Make a POST request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict | None = None) -> Any:
        """Make a PUT request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> bool:
        """Make a DELETE request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.status_code == 204


# Usage example:
# client = RESTClient(
#     "https://api.example.com/v1",
#     auth_header={"Authorization": "Bearer YOUR_TOKEN"}
# )
# users = client.get("users", params={"limit": 10})
