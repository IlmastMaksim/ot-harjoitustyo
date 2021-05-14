from dotenv import load_dotenv
import os


try:
    load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))
except:
    pass

EXAMPLE_IMAGE_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "data", os.getenv("EXAMPLE_IMAGE_FILE")
)
DATASET_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "data", os.getenv("DATASET_FILE")
)
DATABASE_FILE_PATH = os.path.join(
    os.path.dirname(__file__), "data", os.getenv("DATABASE_FILE")
)
