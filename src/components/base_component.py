class BaseComponent:
    def __init__(self, browser, element):
        self.element = element
        self.browser = browser
    
    def find(self, *args):
        return self.element.find_element(*args)

    def find_elements(self, *args):
        return self.element.find_elements(*args)
    
