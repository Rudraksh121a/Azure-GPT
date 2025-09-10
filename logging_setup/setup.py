import logging
import os
from pathlib import Path



def setup_logger(name: str, log_filename: str) -> logging.Logger:
    """Setup and return a logger that logs to console and a file in logs/ folder."""
    # Use logs directory in project root
    project_root = Path(__file__).resolve().parent.parent
    log_dir = project_root / "logs"
    log_dir.mkdir(exist_ok=True)

    log_file = log_dir / log_filename

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers if logger is called multiple times
    if not logger.handlers:
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger




