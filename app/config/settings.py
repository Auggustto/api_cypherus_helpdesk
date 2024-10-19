from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('app/config/database.env')
load_dotenv(dotenv_path=dotenv_path, override=True)