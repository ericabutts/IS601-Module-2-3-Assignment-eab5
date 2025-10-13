########################
# Calculator Config    #
########################

from dataclasses import dataclass
from decimal import Decimal
from numbers import Number
from pathlib import Path
import os
from typing import Optional

from dotenv import load_dotenv

from app.exceptions import ConfigurationError

# Load environment variables from a .env file
load_dotenv()


def get_project_root() -> Path:
    """Get the project root directory (two levels up from this file)."""
    return Path(__file__).parent.parent


@dataclass
class CalculatorConfig:
    """Calculator configuration settings."""

    def __init__(
        self,
        base_dir: Optional[Path] = None,
        max_history_size: Optional[int] = None,
        auto_save: Optional[bool] = None,
        precision: Optional[int] = None,
        max_input_value: Optional[Number] = None,
        default_encoding: Optional[str] = None
    ):
        # Base directory defaults to project root
        self.base_dir = base_dir or Path(os.getenv('CALCULATOR_BASE_DIR', str(get_project_root())))

        # Max history entries
        self.max_history_size = max_history_size or int(os.getenv('CALCULATOR_MAX_HISTORY_SIZE', '1000'))

        # Auto-save preference
        auto_save_env = os.getenv('CALCULATOR_AUTO_SAVE', 'true').lower()
        self.auto_save = auto_save if auto_save is not None else (auto_save_env in ('true', '1'))

        # Calculation precision
        self.precision = precision or int(os.getenv('CALCULATOR_PRECISION', '10'))

        # Max input value
        self.max_input_value = max_input_value or Decimal(os.getenv('CALCULATOR_MAX_INPUT_VALUE', '1e999'))

        # Default encoding
        self.default_encoding = default_encoding or os.getenv('CALCULATOR_DEFAULT_ENCODING', 'utf-8')

    # ---------------------------
    # Directory and file properties
    # ---------------------------

    @property
    def log_dir(self) -> Path:
        """Return the log directory, creating it if necessary."""
        path = Path(os.getenv('CALCULATOR_LOG_DIR', self.base_dir / "logs"))
        path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def history_dir(self) -> Path:
        """Return the history directory, creating it if necessary."""
        path = Path(os.getenv('CALCULATOR_HISTORY_DIR', self.base_dir / "history"))
        path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def history_file(self) -> Path:
        """Return the CSV file path for calculation history."""
        return self.history_dir / "calculator_history.csv"

    @property
    def log_file(self) -> Path:
        """Return the log file path."""
        return self.log_dir / "calculator.log"

    # ---------------------------
    # Validation
    # ---------------------------

    def validate(self) -> None:
        """Validate configuration settings."""
        if self.max_history_size <= 0:
            raise ConfigurationError("max_history_size must be positive")
        if self.precision <= 0:
            raise ConfigurationError("precision must be positive")
        if self.max_input_value <= 0:
            raise ConfigurationError("max_input_value must be positive")
