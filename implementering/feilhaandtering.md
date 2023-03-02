# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except. 
Python forsøker å kjøre kodeblokken osm ligger under `try:`, hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under `except`

```python
try:
    alder = int(input("Alder: "))
    fødselsår = 2022 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: alderen må være et heltall")

print("Koden fortsetter...")
```

### Eksperttips: While-løkke med try-except
```python
while True:
    try: 
        alder = int(input("Alder: "))
        break
    except: 
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")

```

## Logiske feil i programmer

For å oppdage logiske feil i Python-programmer kan vi bruke nøkkelordet 'assert' for å forsikre oss om at koden gir korrekte resultater.


Eksempel:
```python
assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

try:
    assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmeldig
except:
    print("Hei på deg!")

```


### Eksperttips: Håndtering av kjøretidsfeil og logisk feil

```python
while True:
    try: 
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except: 
        print("Alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")
```