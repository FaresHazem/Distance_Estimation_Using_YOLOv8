import cv2
import numpy as np

# Known size of the calibration object (in centimeters)
object_width = 15.0  # Replace with the actual size

# Capture several images with the calibration object at different distances
# Perform corner detection using a calibration pattern (e.g., checkerboard)
# Store object size in pixels and distance for each image

# Example data (replace with actual measurements)
object_size_in_pixels = 363.90472412109375
distance_to_object = 40.0

# Calculate focal length
focal_length = (object_width * distance_to_object) / object_size_in_pixels

print(f"Calculated Focal Length: {focal_length} pixels per centimeter")
