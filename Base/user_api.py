class UserAPI:

    def __init__(self, client, logger=None):
        self.client = client
        self.logger = logger

    def get_user_details(self):
        if self.logger:
            self.logger.info("Fetching logged-in user details")

        response = self.client.get("/auth/me")

        # Add validation logic (important!)
        assert response.status_code == 200, "Failed to fetch user"

        return response.json()

    def refresh_token(self):
        if self.logger:
            self.logger.info("Refreshing token")

        return self.client.refresh_access_token()