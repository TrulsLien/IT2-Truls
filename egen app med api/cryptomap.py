import requests as req

def hent_posisjoner():
    url = f"https://coinmap.org/api/v1/venues/"
    respons = req.get(url, headers={"User-agent": "Thors mac"})
    data = respons.json()
    atm = ["venues"]
    posisjoner = []
    for atm in data["venues"]:
        posisjoner.append([atm["lon"],atm["lat"]])
    return posisjoner
