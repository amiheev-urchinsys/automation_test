import jsonschema

from utilities.api.api_hubs import HubsClass
from utilities.api.api_login import AuthClass
from utilities.data_processing import DataProcessing
from playwright.sync_api import Playwright

def test_api_authorization(playwright: Playwright):
    data_processing = DataProcessing()
    with_auth_api = AuthClass()

    users_list = data_processing.get_list_from_file("user_credentials.json", "users")
    schemes_list = data_processing.get_list_from_file("response_schemes.json", "schemes")
    login_scheme = data_processing.get_value_by_key(schemes_list, "login")
    payload = data_processing.get_value_by_key(users_list, "support")

    response = with_auth_api.log_in(playwright, payload)
    response_body = response.json()
    print(response_body["accessToken"])
    assert response.status == 200
    assert jsonschema.validate(instance=response_body, schema=login_scheme) is None

def test_api_create_hub(playwright: Playwright):
    data_processing = DataProcessing()
    with_hubs_api = HubsClass()
    with_auth_api = AuthClass()

    users_list = data_processing.get_list_from_file("user_credentials.json", "users")
    hubs_list = data_processing.get_list_from_file("api_hub_payloads.json", "hubs")
    payload_auth = data_processing.get_value_by_key(users_list, "support")
    payload_hub = data_processing.get_value_by_key(hubs_list, "outline_based")

    response_login = with_auth_api.log_in(playwright, payload_auth)
    response_body_auth = response_login.json()

    access_token = response_body_auth["accessToken"]

    response_hub = with_hubs_api.create_hub(playwright, payload_hub, access_token)
    response_body_hub = response_hub.json()
    print(response_body_hub)



