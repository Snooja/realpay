#==================Setup===============#
# Public Packages
import pytest
import pandas as pd

# Internal Imports
from realpay.core import Salary, TaxTable

#==================Tests===============#
class TestSalary:

    @pytest.mark.parametrize(
        "input, expected",
        [
            (
                {
                    "base": 100000,
                    "bonus":10000,
                    "shares":20000,
                    "super_":0,
                    "currency": "AUD"
                },
                {
                    "gross": 100000 + 10000 + 20000,
                    "tc": 100000 + 10000 + 20000
                }
                
            ),
            (
                {
                    "base": 100000,
                    "bonus":10000,
                    "shares":20000,
                    "super_":50000,
                    "currency": "AUD"
                },
                {
                    "gross": 100000 + 10000 + 20000,
                    "tc": 100000 + 10000 + 20000 + 50000
                }
            )
        ]
    )
    def test_calcs(self, input, expected):
        result = Salary(**input)
        assert  result.gross == expected.get('gross')
        assert  result.tc == expected.get('tc')

class TestTaxTable:

    @pytest.fixture
    def raw_tax_table(self):
        return pd.DataFrame(
            {
                'min': [0, 18201, 45001, 120001, 180001],
                'max': [18200, 45000, 120000, 180000, 'inf'],
                'rate': [0, 0.19, 0.325, 0.37, 0.45]
            }
        )
    
    def test_clean_tax_table(self, raw_tax_table):
        df = raw_tax_table
        taxtable = TaxTable(raw = df)
        cleaned = taxtable.table

        assert cleaned['min'].dtype is int


