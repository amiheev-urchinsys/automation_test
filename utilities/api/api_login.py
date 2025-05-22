from playwright.sync_api import Playwright


class AuthClass:
    def log_in(self, playwright: Playwright, payload):
        """
        Performs an API request to login with user email and password.

        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :return: JSON response contains access token.
        """
        api_request_context = playwright.request.new_context(
            base_url="https://api.dev.plextera.com"
        )
        response = api_request_context.post(
            "/api/auth/login",
            data=payload,
            headers={
                "Content-Type": "application/json"
            }
        )

        return response

