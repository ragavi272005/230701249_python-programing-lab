import math
def calculate_tiles_needed(pool_diameter_meters, tile_side_cm):
pool_diameter_cm = pool_diameter_meters * 100
pool_radius_cm = pool_diameter_cm / 2
pool_area_sq_cm = math.pi * (pool_radius_cm ** 2)
tile_area_sq_cm = tile_side_cm ** 2
number_of_tiles = math.ceil(pool_area_sq_cm / tile_area_sq_cm)
return number_of_tiles
pool_diameter_meters = int(input())
tile_side_cm = int(input())
tiles_needed = calculate_tiles_needed(pool_diameter_meters, tile_side_cm)
print(f"Number of tiles needed: {tiles_needed}")
