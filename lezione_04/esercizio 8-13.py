def build_profile(**kwargs) -> str:
    
    return ", ".join(f"{key}: {value}" for key, value in kwargs.items())

profile1 = build_profile(name = "Sergio De Guidi", age = 21, hair = "black", weight = 60 )
print(profile1)