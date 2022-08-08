#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field
from typing import Optional


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
    pass

@dataclass
class Tax:
    levy:float = field(init=False)
    tax_table:TaxTable = field(init=False)


@dataclass
class Location:
    country:str
    state:str
    cpi:float = field(init=False)
    tax:Tax = field(init=False)

    def _lookup_cpi(self):
        pass

    def _lookup_tax(self):
        pass

@dataclass
class RealPay:
    location:Location
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

def calculate_tax(gross:int, location:Location) -> float:
    """Calculates personal income tax payable

    Args:
        gross (int): gross yearly pay
        location (Location): location object

    Returns:
        float: tax payable
    """
    pass
