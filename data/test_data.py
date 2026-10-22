import os
from functools import reduce
from pathlib import Path
from urllib.parse import urljoin

from dotenv import load_dotenv

env_name = os.getenv("ENV")
env_path = Path(__file__).parent.parent / (f".env.{env_name}" if env_name else ".env")

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    # Optional warning if local file is missing, but acceptable in CI/CD environments
    print(f"Warning: Configuration file {env_path.name} not found. Relying on system environment variables.")


def url(base, *parts):
    return reduce(urljoin, [base] + list(parts))


BASE_URL = os.getenv("BASE_URL", "")
API_BASE_URL = os.getenv("API_BASE_URL", "")

HOME_URL = url(BASE_URL, "/")
