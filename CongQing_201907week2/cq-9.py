# coding=utf8
__author__ = 'qc'
import time
import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t
class Factor(FactorBase):
    def __init__(self):
        super(Factor,self).__init__()
        self.factorName = __name__.split('.')[-1]
        self.neutral = False
        self.needFields =[t.VALUE_DIFF_MED_TRADER_ACT, t.VALUE_DIFF_LARGE_TRADER, t.PCLOSE]
    def factor_definition(self):
        s = time.time()
        needData = self.needData
        VALUE_DIFF_MED_TRADER_ACT = needData[t.VALUE_DIFF_MED_TRADER_ACT]
        VALUE_DIFF_LARGE_TRADER = needData[ t.VALUE_DIFF_LARGE_TRADER]
        PCLOSE = needData[ t.PCLOSE]
        factor = ((self.calculator.Delay(x=PCLOSE, num=1)) - (VALUE_DIFF_MED_TRADER_ACT)) + (VALUE_DIFF_LARGE_TRADER)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor
    def run_factor(self):
        self.run()


fct = Factor()
fct.run_factor()
