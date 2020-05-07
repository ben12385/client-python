# coding: utf-8

from dateutil.parser import parse
from pycti import OpenCTIApiClient
from stix2 import TLP_AMBER, TLP_GREEN


class TestIndicators:
    def test_create_indicator(self):
        opencti_api_client = OpenCTIApiClient(
            "https://demo.opencti.io",
            "2b4f29e3-5ea8-4890-8cf5-a76f61f1e2b2",
            ssl_verify=True,
        )
        # Define the date
        date = parse("2019-12-01").strftime("%Y-%m-%dT%H:%M:%SZ")
        # Create the indicator
        indicator = opencti_api_client.indicator.create(
            name="C2 server of the new campaign",
            description="This is the C2 server of the campaign",
            pattern_type="stix",
            indicator_pattern="[domain-name:value = 'www.5z8.info' AND domain-name:resolves_to_refs[*].value = '198.51.100.1/32']",
            main_observable_type="IPv4-Addr",
            valid_from=date,
            markingDefinitions=[TLP_AMBER["id"], TLP_GREEN["id"]],
        )
        print(indicator)

        assert indicator["id"] is not None or indicator["id"] != ""

    def test_get_100_indicators_with_pagination(self):
        opencti_api_client = OpenCTIApiClient(
            "https://demo.opencti.io",
            "2b4f29e3-5ea8-4890-8cf5-a76f61f1e2b2",
            ssl_verify=True,
        )

        # Get all reports using the pagination
        custom_attributes = """
            id
            indicator_pattern
            created
        """

        final_indicators = []
        data = opencti_api_client.indicator.list(
            first=50, customAttributes=custom_attributes, withPagination=True
        )
        final_indicators = final_indicators + data["entities"]

        assert len(final_indicators) == 50

        after = data["pagination"]["endCursor"]
        data = opencti_api_client.indicator.list(
            first=50,
            after=after,
            customAttributes=custom_attributes,
            withPagination=True,
        )
        final_indicators = final_indicators + data["entities"]

        assert len(final_indicators) == 100
