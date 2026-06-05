from pathlib import Path

CAMERA_NAME = "Galaxy S21 rear camera"
DEVICE = "Samsung Galaxy S21"

IMAGE_WIDTH = 3024
IMAGE_HEIGHT = 4032
IMAGE_FORMAT = "jpg"

IMAGE_DIR = Path("data/calibration/images")

SQUARE_COLUMNS = 11
SQUARE_ROWS = 8

PATTERN_SIZE = (10, 7)  # inner corners: columns, rows
SQUARE_SIZE = 15.0      # mm
SQUARE_SIZE_UNIT = "mm"

NUM_IMAGES = 14

CAPTURE_CONDITION = "태블릿에 디스플레이된 checkerboard를 휴대폰으로 촬영"