#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field
from typing import Optional

#==================Functions===========#
def convert_salary(salary:Salary, currency:) -> Salary:
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

#==================Classes=============#
@dataclass
class RealPay:
    location:Location
    salary:Salary

@dataclass
class Salary:
    """Class  for your gross salary and super

    """
    base:int
    bonus:int
    shares:int
    super:int
    currency: str
    gross:int = field(init = False)
    tc:int = field(init = False)

    def __post__init__(self):
        self.tc =_self.calc_tc()
    
    def _calc_gross(self):
        return self.base + self.bonus + self.shares
    
    def _calc_tc(self):
        return  self._calc_gross + self.super

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
class Tax:
    levy:float = field(init=False)
    tax_table:TaxTable = field(init=False)


