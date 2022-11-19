#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 16:34:28 2022

@author: svenmaurice
"""

import twint
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import nest_asyncio

YEARS = 5
DATE_START = datetime.datetime.today()
DATE_END = DATE_START.replace(DATE_START.year - YEARS)
TIMELINE = pd.date_range(end=DATE_START, start=DATE_END)

nest_asyncio.apply()

for day_end in TIMELINE:
    day_start = day_end + relativedelta(days=-1)
    day_end_str = day_end.strftime("%Y-%m-%d")
    day_start_str = day_start.strftime("%Y-%m-%d")  # type = string
    print("END: " + day_end_str + " START " + day_start_str)
    # configure search
    configuration = twint.Config()
    configuration.Since = day_start_str
    configuration.Until = day_end_str
    configuration.Lang = "eng"
    configuration.Store_csv = True
    configuration.Output = "test-" + str(day_end) + ".csv"
    configuration.Username = "macro_srsv"
    twint.run.Search(configuration)
