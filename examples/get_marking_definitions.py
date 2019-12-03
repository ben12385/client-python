# coding: utf-8

from pycti import OpenCTIApiClient, MarkingDefinition

# Variables
api_url = 'https://demo.opencti.io'
api_token = '616e214c-8d86-4226-a653-c521f4ec90d9'

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# Get all marking definitions
marking_definitions = opencti_api_client.marking_definition.list()

# Print
for marking_definition in marking_definitions:
    print('[' + marking_definition['definition_type'] + '] ' + marking_definition['definition'])