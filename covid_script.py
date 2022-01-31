import requests
import json

url = 'https://disease.sh/v3/covid-19/all'

response = requests.request("GET",url)

# converting bytes to string
response_string = response.content.decode("UTF-8")

# converting string to dict
response_dict = json.loads(response_string)

print(response_dict)

print('Number of cases worldwide:',response_dict['cases'])
print('Number of cases todaysCases:',response_dict['todayCases'])
print('Number of cases Deaths:',response_dict['deaths'])
print('Number of cases  Deaths:',response_dict['todayDeaths'])
print('Number of cases today Recoverd:',response_dict['recovered'])
print('Number of cases today Recovered:',response_dict['todayRecovered'])
print('Number of Affected countries:',response_dict['affectedCountries'])