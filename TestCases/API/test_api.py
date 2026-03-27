import pytest


@pytest.mark.api
class TestAuthUserFlow:

    def test_login_sets_token(self, api_client, logger):
        logger.info("===== TEST: LOGIN & TOKEN SET =====")

        api_client.login("emilys", "emilyspass")

        logger.info(f"Access Token: {api_client.access_token}")

        assert api_client.access_token is not None, "Access token not set"
        assert "Authorization" in api_client.session.headers, "Auth header missing"

        logger.info("Login successful, token stored in session")


    def test_get_current_user(self, api_client, logger):
        logger.info("===== TEST: GET CURRENT USER =====")

        api_client.login("emilys", "emilyspass")

        response = api_client.get("/auth/me")

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        data = response.json()

        assert response.status_code == 200, "Failed to fetch current user"
        assert "id" in data, "User ID missing in response"
        assert "email" in data, "Email missing in response"

        logger.info("Fetched logged-in user successfully")


    def test_create_user(self, api_client, logger):
        logger.info("===== TEST: CREATE USER =====")

        api_client.login("emilys", "emilyspass")

        payload = {
            "firstName": "Sachin",
            "lastName": "Automation"
        }

        logger.info(f"Payload: {payload}")

        response = api_client.post("/users/add", json=payload)

        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        data = response.json()

        assert response.status_code == 201, "User creation failed"
        assert data["firstName"] == "Sachin", "First name mismatch"

        logger.info("User created successfully")


    def test_invalid_login(self, api_client, logger):
        logger.info("===== TEST: INVALID LOGIN =====")

        with pytest.raises(Exception):
            api_client.login("wrong_user", "wrong_pass")

        logger.info("Invalid login handled correctly")

    def test_access_without_login(self, config, logger):
        from Base.api_client import APIClient

        logger.info("===== TEST: INVALID LOGIN =====")

        client = APIClient(config.get_api_base_url(), logger=logger)

        import pytest
        with pytest.raises(Exception):
            client.login("wrong_user", "wrong_pass")

        logger.info("Invalid login handled correctly")