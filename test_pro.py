import sys
# sys.path.append(r'path')
# from page_object_model.login import logdata as lo
from page_object_model.login import logdata as lo
# for a ,b in sys.modules.items():
#     print(a,"--->",b)
# import os as oo
# oo.open(oo.__file__,'.')
import pytest as pts
dri=lo()
dri.drive_log()
# class Test_appliction:
# def test_runner():
#     lo.drive_log()
#     lo.login_data()
#     lo.log_out()
    
# print(lo.__file__)
# print(sys.path)
