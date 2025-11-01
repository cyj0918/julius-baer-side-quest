import logging
import logging.handlers
import os
from pathlib import Path

def setup_logging(log_level="INFO"):
    """Configure structured logging for the application."""
    
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger("banking_client")
    logger.setLevel(getattr(logging, log_level))
    
    # File handler
    file_handler = logging.handlers.RotatingFileHandler(
        log_dir / "banking_client.log",
        maxBytes=10485760,  # 10MB
        backupCount=5
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger