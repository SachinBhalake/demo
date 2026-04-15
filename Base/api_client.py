import requests
from Base.endpoints import Endpoints


class APIClient:
    def __init__(self, api_base_url, headers=None, timeout=30, logger=None):
        self.api_base_url = api_base_url
        self.session = requests.Session()
        self.session.headers.update(headers or {})
        self.timeout = timeout
        self.logger = logger

        self.access_token = None
        self.refresh_token = None

    # ------------------------
    # URL builder
    # ------------------------
    def _url(self, endpoint):
        return f"{self.api_base_url}{endpoint}"

    # ------------------------
    # Core request handler
    # ------------------------
    def request(self, method, endpoint, retry=True, timeout=None, **kwargs):
        url = self._url(endpoint)

        if self.logger:
            self.logger.info(f"{method} {url}")
            if "json" in kwargs:
                self.logger.debug(f"Payload: {kwargs['json']}")

        response = self.session.request(
            method=method,
            url=url,
            timeout=timeout or self.timeout,
            **kwargs
        )

        # Auto refresh
        if response.status_code == 401 and retry and self.refresh_token:
            if self.logger:
                self.logger.warning("401 detected. Refreshing token...")

            self.refresh_access_token()

            return self.request(method, endpoint, retry=False, **kwargs)

        return response

    # ------------------------
    # HTTP methods
    # ------------------------
    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

    # ------------------------
    # Auth
    # ------------------------
    def login(self, username, password):
        response = self.post(
            Endpoints.Auth_User_Login,
            json={"username": username, "password": password}
        )

        self._validate_response(response)

        data = response.json()
        self.access_token = data.get("accessToken")
        self.refresh_token = data.get("refreshToken")

        self.set_token(self.access_token)

    def refresh_access_token(self):
        response = self.post(
            Endpoints.Auth_Refresh_Token,
            json={"refreshToken": self.refresh_token}
        )

        self._validate_response(response)

        data = response.json()
        self.access_token = data.get("accessToken")

        self.set_token(self.access_token)

    # ------------------------
    # Helpers
    # ------------------------
    def set_token(self, token):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def _validate_response(self, response):
        try:
            response.raise_for_status()
        except Exception as e:
            if self.logger:
                self.logger.error(f"API Failed: {response.text}")
            raise e