# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import sys
import unittest
import qlib
from qlib.data import D
from qlib.tests import TestAutoData
from qlib.config import REG_US


class TestRegiterCustomOps(TestAutoData):
    @classmethod
    def setUpClass(cls) -> None:
        # use default data
        provider_uri = "~/.qlib/qlib_data/us_data"  # target_dir
        qlib.init(provider_uri=provider_uri, region=REG_US)

    def test_regiter_custom_ops(self):

        instruments = ["a1x4w7"]
        fields = ["$$q_accountspayable / $$q_totalcurrentassets"]
        print(D.features(instruments, fields, start_time="2020-06-01", end_time="2020-06-10", freq="day"))
        fields = [
            "($$q_accountspayable / $$q_totalcurrentassets) / PRef($$q_accountspayable / $$q_totalcurrentassets, 1) - 1"
        ]
        print(D.features(instruments, fields, start_time="2020-06-01", end_time="2020-06-10", freq="day"))
        fields = ["PSum($$q_totalrevenue/$$q_totalcurrentassets, 4)"]
        print(D.features(instruments, fields, start_time="2020-06-01", end_time="2020-06-10", freq="day"))
        fields = ["$$q_totalcurrentassets/$close/10000"]
        print(D.features(instruments, fields, start_time="2020-06-01", end_time="2020-06-10", freq="day"))


if __name__ == "__main__":
    unittest.main()
