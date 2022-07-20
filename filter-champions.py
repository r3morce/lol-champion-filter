import requests
import json

# Get data from riot api

url = "https://ddragon.leagueoflegends.com/cdn/12.13.1/data/de_DE/champion.json"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# Extract champion list from received data

json = response.json()
champions = json["data"]
champions = list(champions.values())

print("Total %i" % len(champions))

# Filter champions

filtered = filter(
    lambda champion: "Tank" in champion["tags"] and "Fighter" in champion["tags"], champions)

filtered = list(filtered)

print("Filtered %i" % len(filtered))

print("Found Champions (%s):" % len(filtered))

for champion in filtered:
    print("\t%s" % champion["name"])
