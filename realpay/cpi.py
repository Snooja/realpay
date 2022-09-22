#==================Setup===============#
# Public Packages
from dataclasses import dataclass, field
from typing import Optional
import pandas as pd


#==================Classes=============#
@dataclass(slots=True)
class CPI:
    """Class """
    raw:pd.DataFrame

    @classmethod
    def from_csv(cls, fp):
        df = pd.read_csv(fp)
        return cls(raw = df)