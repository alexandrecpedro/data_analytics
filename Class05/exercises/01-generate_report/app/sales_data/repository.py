import logging
from typing import List, Optional

class SalesFileRepository:
    """Handles the low-level reading of data from the input file."""

    def __init__(self, logger: logging.Logger, filepath: str, mode: str, encoding: str):
        self._logger = logger
        self._filepath = filepath
        self._mode = mode
        self._encoding = encoding

    def get_raw_lines(self) -> Optional[List[str]]:
        """
        Reads the file and returns a list of raw data lines, excluding the header.

        :return: Optional list of raw data strings (lines), or None if the file is not found.
        """
        try:
            self._logger.info(f"Reading file: {self._filepath}")
            with open(file=self._filepath, mode=self._mode, encoding=self._encoding) as file:
                lines = file.readlines()
                if not lines:
                    self._logger.warning(msg=f'The file {self._filepath} is empty!')
                    return []
                # Return all lines except the header (index 0)
                return lines[1:]
        except FileNotFoundError:
            self._logger.error(msg=f'File not found at {self._filepath}. Please ensure the file exists.')
            return None