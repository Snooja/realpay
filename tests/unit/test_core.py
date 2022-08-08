#==================Setup===============#
# Public Packages
import pytest 

# Internal Imports
from realpay.core import Salary

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
