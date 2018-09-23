from selenium import webdriver


class MetaClassSingleton(type):
    """
    Meta class implementation
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Override __call__ special method based on singleton pattern
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Driver(metaclass=MetaClassSingleton):
    """
    Driver class decorated by the meta class: MetaClassSingleton.
    Behaviour changed in singleton
    """
    instance = None

    def connect(self):
        """
        Set the driver with the web driver

        Returns:
             self.driver: web driver
        """
        if self.instance is None:
            self.instance = webdriver.Chrome()

        return self.instance
