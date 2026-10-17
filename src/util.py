import numpy as np
import cv2

def get_limit(color: list) -> tuple:
    """
    Computes the HSV lower and upper bounds for a given BGR color.

    Mathematical constraint: OpenCV uses 8-bit unsigned integers for image arrays where 
    the HSV ranges are H: [0, 179], S: [0, 255], and V: [0, 255]. 
    This differs from standard HSV representations where hue is represented as [0, 360].
    
    Args:
        color (list): The BGR color array (e.g., [0, 255, 255]).

    Returns:
        tuple[np.ndarray, np.ndarray]: System-agnostic numpy arrays defining boundary ranges.
    """
    # OpenCV requires explicitly shaped inputs for cv2.cvtColor. 
    # Shape must be (height, width, channels). Passing [color] generates shape (1, 3).
    # We must expand dimensionality to (1, 1, 3) to represent a 1x1 image with 3 channels.
    c = np.uint8([[color]])
    
    # Transform color space via matrix multiplication mechanics (BGR -> HSV)
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Extract the hue integer at index [0][0][0] from the isolated matrix
    hue = int(hsv[0][0][0])
    
    # Establish defensive boundary constraints (prevent integer underflow/overflow)
    lower_bound = np.array([max(0, hue - 10), 100, 100], dtype=np.uint8)
    upper_bound = np.array([min(179, hue + 10), 255, 255], dtype=np.uint8)

    return lower_bound, upper_bound