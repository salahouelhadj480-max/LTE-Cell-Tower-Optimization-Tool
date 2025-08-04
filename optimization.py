import pandas as pd
import numpy as np

def calculate_coverage(tower_lat, tower_lon, user_locs, radius_km=1.5):
    from geopy.distance import geodesic
    covered_users = []
    for user in user_locs:
        if geodesic((tower_lat, tower_lon), user).km <= radius_km:
            covered_users.append(user)
    return covered_users
