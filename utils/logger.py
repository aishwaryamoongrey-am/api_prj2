import logging
from pathlib import Path


def get_logger(test_name: str):
    """Create logger that writes to repo-root `logs/{test_name}.log` and console.

    Uses the file location relative to this module to avoid relying on CWD.
    Prints the absolute log path once for troubleshooting.
    """
    repo_root = Path(__file__).resolve().parent.parent
    logs_dir = repo_root / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(test_name)

    # Prevent duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s")

    file_path = logs_dir / f"{test_name}.log"
    file_handler = logging.FileHandler(str(file_path), mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Helpful debug output so users can locate the log file
    print(f"[logger] writing to {file_path}")

    return logger
