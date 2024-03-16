from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

# action chains
from selenium.webdriver import ActionChains


class DragDrop:
    """
        This class is used to drag and drop an element
    """
    def __init__(self, url):
        """
                This is default constructor
        """
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    def BrowseURL(self):
        """
                This method is used to open the browser and go to url
        """
        self.driver.get(self.url)
        sleep(2)
        self.driver.maximize_window()
        sleep(4)

    def CloseBrowser(self):
        """
                This method is used to close the browser
        """
        self.driver.quit()

    def FindElementByXpath(self, xpath):
        """
                        This method is used to find element using xpath
        """
        return self.driver.find_element(by=By.XPATH, value=xpath)

    def DragAndDrop(self):
        """
            This method  is used to drag and drop an element
        """
        try:
            frameRef = self.FindElementByXpath("//*[@id='content']/iframe")
            self.driver.switch_to.frame(frameRef)
            source = self.FindElementByXpath("//*[@id='draggable']")
            destination = self.FindElementByXpath("//*[@id='droppable']")
            self.action.drag_and_drop(source, destination).perform()
            sleep(3)
            droptext = self.FindElementByXpath("//*[@id='droppable']/p").text
            if droptext == "Dropped!":
                print("Drag and Drop is successfull")
            else:
                print("Drag and Drop is NOT successfull")
        except NoSuchElementException as e:
            print(e)


obj1 = DragDrop("https://jqueryui.com/droppable/")
obj1.BrowseURL()
obj1.DragAndDrop()
obj1.CloseBrowser()





