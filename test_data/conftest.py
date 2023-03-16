from selenium import webdriver as wb
from webdriver_manager.chrome import ChromeDriverManager as ch
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager as ec
from selenium.webdriver.edge.service import Service
import pytest as pyt
from sample_project.utilities_files.make_log import login_er as er
from sample_project.page_object_model import login as bn



@pyt.fixture
def link(browser):
    mm=er()
    if browser == 'edge':
        if driver is None:
        
            mm.info('edge driver is successfully working ')
            driver=wb.Edge(service=Service(ec().install()))
            return driver
    
    else:
            mm.info('chrome driver is successfully working')
            
            driver=wb.Chrome(service=Service(ch().install()))
            return driver





def pytest_html_report_title(report):
    report.title = "shopping site...."

def pytest_addoption(parser):    #this will get the value from cli/hooks
    parser.addoption('--browser')


@pyt.fixture
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'jinga'

# It is hook for delete/Modify Environment info to HTML Report
@pyt.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



@pyt.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when=="setup":
        
        extra.append(pytest_html.extras.url("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name=r"screenshots\'"+bn.cv

            if file_name:
                html="""<div><img src='%s' alt='serverdown'width="380" height="228"
                'onclick=window.open(this.src)' align='right'></div>"""%file_name
                

            # only add additional html on failure
            extra.append(pytest_html.extras.html(html))
           
        report.extra = extra



