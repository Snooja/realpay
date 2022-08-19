#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field, asdict
from typing import Optional
from datetime import date
from typing import Union, List
import pandas as pd
import numpy as np
import json


#==================Classes=============#


@dataclass
class Salary:
    """Class  for your gross salary and super

    """
    base:int
    bonus:int
    shares:int
    super_:int
    currency: str
    gross:int = field(init = False)
    tc:int = field(init = False)

    def __post_init__(self):
        self.tc = self.calc_tc()
        self.gross = self.calc_gross()
    
    def calc_gross(self) -> int:
        return self.base + self.bonus + self.shares
    
    def calc_tc(self) -> int:
        return  self.calc_gross() + self.super_

@dataclass
class TaxTable:
    """Class for a specific tax table
    """
    raw:dict# raw tax table
    table:pd.DataFrame = field(init=False)
    min_col:str = 'min'
    max_col:str = 'max'
    rate_col:str = "rate"
    inf_str:str = 'inf' # what to interpret as infini

    @classmethod
    def from_csv(cls, fp):
        df = pd.read_csv(fp)
        return cls(raw = df)


    def __post_init__(self):
        self.table = pd.DataFrame(self.raw)
        self.table = self.clean_tax_table(self.table)
        self.table = self.prepare_table(self.table)

    def clean_tax_table(self, table:pd.DataFrame) -> pd.DataFrame:
        df = table.copy()
        df = self._convert_inf_str(df = df)
        df = self._clean_dtypes(df = df)
        return(df)

    def _clean_dtypes(self, df:pd.DataFrame) -> pd.DataFrame:
        clean = df.copy()
        clean = clean.astype(
            {
                self.min_col: np.float64 ,
                self.max_col: np.float64,
                self.rate_col: np.float64
            }
        )
        return(clean)

    def _convert_inf_str(self, df:pd.DataFrame) -> pd.DataFrame:
        converted = df.copy()
        converted.replace(self.inf_str, np.inf)
        return(converted)

    def prepare_table(self, df:pd.DataFrame) -> pd.DataFrame:
        prepared = df.copy()
        prepared['bracket_tax'] = self._calc_bracket_tax(df)
        prepared['cumsum'] = self._calc_max_cumsum(df)
        return(prepared)

    def _calc_bracket_tax(self, df:pd.DataFrame) -> pd.DataFrame:
        return ( (df[self.max_col] - df[self.min_col]) * df[self.rate_col])
    
    def _calc_max_cumsum(self, df:pd.DataFrame) -> pd.DataFrame:
        return df[self.max_col].cumsum()







@dataclass
class Tax:
    """Object capturing tax rate for a location
    """
    levy:float  # flat levy
    valid_from: date # date rates valid from
    valid_to: date # date vrates valid until
    country: str # ISO Alpha-3 country code
    state: Union[str, List[str]] # state code eg. WA for Western Australia
    currency:str
    raw_tax_table: dict
    reference: str # refernece to where you got the information eg. https://www.ato.gov.au/rates/individual-income-tax-rates/
    tax_table:TaxTable = field(init=False)
    
    @staticmethod
    def _from_json(fp):
        f = open(fp, 'r')
        d = json.loads(f.read())
        f.close()
        return(d)

    @classmethod
    def from_json(cls, fp):
        d = Tax._from_json(fp)
        return cls(**d)

    def __post_init__(self):
        pass
        self.tax_table = TaxTable(raw = self.raw_tax_table)

    def to_json(self, fp = None):
        if fp is None:
            if isinstance(self.state,str):
                fp = "_".join([self.country, self.state, self.valid_from, self.valid_to])
            else:
                fp = "_".join([self.country, self.valid_from, self.valid_to])
            fp += ".json"
        d = asdict(self)
        del d['tax_table']
        with open(fp, 'w') as f:
            json.dump(d, f, ensure_ascii=False)
    



@dataclass
class RealPay:
    country: str # ISO Alpha-3 country code
    state: str # state code eg. WA for Western Australia
    salary:Salary



#==================Functions===========#
def convert_salary(salary:Salary, currency:str) -> Salary:
    """Converts salary to new currency

    Args:
        salary (Salary): input salary
        currency (_type_): new currency

    Returns:
        Salary: In new currency
    """
    pass
