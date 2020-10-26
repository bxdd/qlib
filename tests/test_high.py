#import qlib
#qlib.init(provider_uri='~/.qlib/qlib_data/high_freq', redis_port=233)
#
#from qlib.data import D
#
#instruments = ['SH600087']
#fields = ['Ref($close,10)']
#
#a = D.features(instruments, fields, start_time='2010-01-01', end_time='2017-12-31', freq='1min')
#print(a)
#Copyright (c) Microsoft Corporation.
#Licensed under the MIT License.
import sys
from pathlib import Path

import qlib
import pandas as pd
from qlib.config import REG_CN
from qlib.contrib.estimator.handler import QLibHighFreqDataHandler

from qlib.utils import exists_qlib_data


if __name__ == "__main__":

    # use default data
    provider_uri = "~/.qlib/qlib_data/high_freq"  # target_dir
    qlib.init(provider_uri=provider_uri, redis_port=233, region=REG_CN)

    MARKET = "csi300"

    ###################################
    # train model
    ###################################
    DATA_HANDLER_CONFIG = {
        "dropna_label": True,
        "start_date": "2010-01-01",
        "end_date": "2017-12-31",
        "market": MARKET,
    }

    TRAINER_CONFIG = {
        "train_start_date": "2010-01-01",
        "train_end_date": "2013-12-31",
        "validate_start_date": "2014-01-01",
        "validate_end_date": "2015-12-31",
        "test_start_date": "2016-01-01",
        "test_end_date": "2017-12-31",
    }

    # use default DataHandler
    # custom DataHandler, refer to: TODO: DataHandler API url
    data_handler =  QLibHighFreqDataHandler(**DATA_HANDLER_CONFIG)
    #x_train, y_train, x_validate, y_validate, x_test, y_test = QLibHighFreqDataHandler(
    #    **DATA_HANDLER_CONFIG
    #).get_split_data(**TRAINER_CONFIG)
