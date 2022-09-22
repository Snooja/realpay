#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field
from typing import Optional
from datetime import date
import pandas as pd
from pathlib import Path
import logging


#==================Classes=============#
@dataclass(slots=True)
class CPI:
    """Class """
    raw:pd.DataFrame = None
    _data_folder = Path("realpay","data","cpi")
    _filename = "cpi.csv"

    @classmethod
    def from_csv(cls, fp):
        df = pd.read_csv(fp)
        return cls(raw = df)
    
    def _get_year(self) -> str:
        return str(date.today().year)

    def _default_file_path(self) -> Path:
        return self._data_folder / self._get_year() / self._filename

    def load_default_file(self):
        fp = self._default_file_path()
        try:
            self.raw = pd.read_csv(fp)
        except FileNotFoundError:
            raise FileNotFoundError(f"{fp.absolute()} could not be found")


    def __post_init__(self):
        if self.raw is None:
            self.load_default_file()
