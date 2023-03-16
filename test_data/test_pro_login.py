from sample_project.page_object_model import login as co #logging module
import pytest as pt,logging as loo,os#loggin
from sample_project.utilities_files.make_log import login_er as er# source code file

#first test case
class Test_appliction:
    sa=er()
    
    def test_runner(self,link):
        self.sa.info('driver login...')
        self.lo=co.logdata(link)
        self.sa.info('page login...')
        self.lo.login_data()
        self.sa.info('page logout...')
        self.lo.log_out()
     
    @pt.mark.skip(reason='notehing....😎')#test case skipped 
    def test_skipped(self):
        print('skipped')

#secod testcase
class Test_fing:
    def test_r(self,link):
        self.sa.info('driver login...')
        self.lo=co.logdata(link)
        self.sa.info('page login...')
        self.lo.login_data()
        self.sa.info('page logout...')
        self.lo.log_out()
