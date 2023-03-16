from selenium import webdriver as wb #webdriver object
from webdriver_manager.chrome import ChromeDriverManager as ch #chrome driver object
from selenium.webdriver.chrome.service import Service #service object for chrome
from webdriver_manager.microsoft import EdgeChromiumDriverManager as ec # edge driver object
from selenium.webdriver.edge.service import Service #service object for edge
import pytest as pyt #pytest object
from sample_project.utilities_files.make_log import login_er as er #logging file object
from sample_project.page_object_model import login as bn #source code may not


# making fixture by pytest side return driver object
@pyt.fixture
def link(browser):
    mm=er()
    if browser == 'edge':
        if driver is None:
        
            mm.info('edge driver is successfully working ')#loggin by driver side
            driver=wb.Edge(service=Service(ec().install())) #edge driver
            return driver
    
    else:
            mm.info('chrome driver is successfully working')#loggin by driver side
            
            driver=wb.Chrome(service=Service(ch().install())) #chrome driver
            return driver





def pytest_html_report_title(report):# report titile generation
    report.title = "shopping site...." #report title

def pytest_addoption(parser):    #this will get the value from cli/hooks (pytest side hook generation)
    parser.addoption('--browser')


@pyt.fixture# this is used for cmd output console | execution options
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):#table data changing area
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'jinga'

# It is hook for delete/Modify Environment info to HTML Report
@pyt.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



@pyt.hookimpl(hookwrapper=True) #adding screenshots and other things...
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



