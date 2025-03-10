def describe_cities(city:str, country:str = "Italy") -> str:
    
    print(f"{city} is in {country}")

describe_cities("Rome")
describe_cities("Naples")
describe_cities("London", "England")