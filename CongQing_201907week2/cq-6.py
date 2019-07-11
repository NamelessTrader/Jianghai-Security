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
        self.needFields =[t.PCTCHG, t.OPEN]
    def factor_definition(self):
        s = time.time()
        needData = self.needData
        PCTCHG = needData[t.PCTCHG]
        OPEN = needData[ t.OPEN]
        factor = self.calculator.cmpMin(self.calculator.RegResi(self.calculator.Delay(x=OPEN, num=1),OPEN,30),PCTCHG)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor
    def run_factor(self):
        self.run()


fct = Factor()
fct.run_factor()
