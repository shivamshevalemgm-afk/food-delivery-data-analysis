from pathlib import Path

# ===========================
# PROJECT PATHS
# ===========================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / "1_Data" / "Raw"
CLEAN_DATA_PATH = BASE_DIR / "1_Data" / "Cleaned"

RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)
CLEAN_DATA_PATH.mkdir(parents=True, exist_ok=True)

# ===========================
# DATA SIZE
# ===========================

# NUM_CITIES = 50
# NUM_CUSTOMERS = 100000
# NUM_RESTAURANTS = 5000
# NUM_MENU_ITEMS = 25000
# NUM_DELIVERY_PARTNERS = 20000
# NUM_COUPONS = 100
# NUM_ORDERS = 1000000
# NUM_ORDER_ITEMS = 3000000
# NUM_PAYMENTS = 1000000
# NUM_REVIEWS = 700000

NUM_CUSTOMERS = 1000
NUM_RESTAURANTS = 100
NUM_MENU_ITEMS = 500
NUM_DELIVERY_PARTNERS = 200
NUM_ORDERS = 5000
NUM_ORDER_ITEMS = 15000
NUM_PAYMENTS = 5000
NUM_REVIEWS = 3500
