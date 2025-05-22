from playwright.sync_api import Playwright


class HubsClass:
    def create_hub(self, playwright: Playwright, payload, token):
        """
        Performs an API request to create a hub.
        :param playwright: Playwright object used to create the API request context.
        :param payload: JSON data
        :return: JSON response contains hub's data.
        """
        api_request_context = playwright.request.new_context(
            base_url = "https://api.dev.plextera.com"
        )
        response = api_request_context.post(
            "/api/hubs/create",
            data = payload,
            headers = {
                "Context-type": "application/json",
                "Authorization": "Bearer " + token
            }
        )

        return response