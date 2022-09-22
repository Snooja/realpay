#==================Setup===============#
# Public Packages
import pytest
import pandas as pd
from pathlib import Path


# Internal Imports
from realpay.cpi import CPI

#==================Tests===============#
@pytest.fixture(scope="session")
def cpi_df():
    return pd.DataFrame({
        'col1': [1,2,3,4,5],
        'col2': ['a','b','c','d','e']
    })

@pytest.fixture(scope="session")
def cpi_csv(tmp_path_factory, cpi_df):
    fp = tmp_path_factory.mktemp('data') / 'test_cpi.csv'
    cpi_df.to_csv(fp, header=True,index=False)
    return fp

class TestCPI:
    def test_from_csv(self, cpi_csv):
        test = CPI.from_csv(cpi_csv)
        print(test.raw)
        

        



