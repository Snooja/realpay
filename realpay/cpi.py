#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field
from typing import Optional, Union
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

    @staticmethod
    def parse_city(s:str) -> (str, str, str):
        """Parses city, countrycode, and country from a single entry in the CPI city column"""
        l = s.split(',')
        l = [item.strip() for item in l]
        if len(l) < 2:
            raise ValueError(f"city field has {len(l)} to unpack which is not enough (min 2)")
        elif len(l) == 2:
            city = l[0]
            country = l[1]
            countrycode = None
        elif len(l) == 3:
            city = l[0]
            countrycode = l[1]
            country = l[2]
        else:
            raise Error(f"city field has {len(l)} to unpack which is too many (max 3)")
        
        return (city, countrycode, country)

    @classmethod
    def from_csv(cls, fp:Path):
        df = pd.read_csv(fp)
        return cls(raw = df)
    
    def _get_year(self) -> str:
        return str(date.today().year)

    def _default_file_path(self) -> Path:
        return self._data_folder / self._get_year() / self._filename

    def load_default_file(self):
        self.extract(self._default_file_path())


    def extract(self, fp:Path) -> pd.DataFrame:
        try:
            self.raw = pd.read_csv(fp)
            return self.raw
        except FileNotFoundError:
            raise FileNotFoundError(f"{fp.absolute()} could not be found")
    



    def transform(self, df:Union[None,pd.DataFrame]):
        if df is None:
            df = self.raw
        
        

        

    def __post_init__(self):
        if self.raw is None:
            self.load_default_file()
        