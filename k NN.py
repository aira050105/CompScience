country_coordinates = {
    "USA": (37.0902, -95.7129),
    "India": (20.5937, 78.9629),
    "China": (35.8617, 104.1954),
    "France": (46.6034, 1.8883),
    "Brazil": (-14.2350, -51.9253),
    "Australia": (-25.2744, 133.7751),
    "Canada": (56.1304, -106.3468),
    "Germany": (51.1657, 10.4515),
    "UK": (55.3781, -3.4360),
    "Russia": (61.5240, 105.3188)
}

def manhattan_distance(lat1, lon1, lat2, lon2):
    """Calculate Manhattan distance between two latitude/longitude points."""
    lat_diff = abs(lat1 - lat2)
    lon_diff = abs(lon1 - lon2)
    
    # Approximate conversion factor: 1 degree ≈ 111 km
    distance_km = (lat_diff + lon_diff) * 111
    distance_miles = distance_km * 0.621371  # Convert to miles
    return distance_km, distance_miles

def get_distance(country1, country2):
    """Find the Manhattan distance between two countries"""
    if country1 not in country_coordinates or country2 not in country_coordinates:
        return "Country not found in database!"
    
    lat1, lon1 = country_coordinates[country1]
    lat2, lon2 = country_coordinates[country2]
    
    distance_km, distance_miles = manhattan_distance(lat1, lon1, lat2, lon2)
    
    return f"Manhattan Distance between {country1} and {country2}: {distance_km:.2f} km ({distance_miles:.2f} miles)"

# Example usage
country1 = "USA"
country2 = "India"

print(get_distance(country1, country2))