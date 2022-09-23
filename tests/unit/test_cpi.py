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


@pytest.mark.parametrize(
    "input,expected",
    [
        ("city,CT,country", ("city","CT","country")),
        ("New York,  NY, United States", ("New York","NY","United States"))
        ]
)
def test_cpi_parse_valid_city(input, expected):
    city, citycode, country = CPI.parse_city(input)
    assert (city, citycode, country) == (expected)

@pytest.mark.parametrize(
    "input",
    [
        "a",
        "a, b, c, d",
        ""
    ],
    ids = ['invalid single', 'invalid four items', 'invalid empty str']
)
def test_cpi_raises_parse_invalid_city(input):
    with pytest.raises(Exception):
        CPI.parse_city(input)
class TestCPI:
    def test_from_csv(self, cpi_csv):
        test = CPI.from_csv(cpi_csv)
        print(test.raw)
        
    def test_loads_default(self):
        test = CPI()
        print(test.raw)
    



        



