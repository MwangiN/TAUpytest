import pytest
import requests

@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():
     # Arrange
  url = 'https://api.duckduckgo.com/?q=python+programming&format=json' # two parameters query and format
    # Act
  response = requests.get(url) #sends the request as a HTTP GET to the DuckDuckGo Instant Answer API endpoint
  body = response.json() #This will parse the response data from JSON text into a Python dictionary object which will be useful for validation.
   # Assert
  assert response.status_code == 200  #verify that the request was successful.
  assert 'Python' in body['AbstractText'] #check the actual content of the response.


