class Singleton:
    instance = None
    def __new__(cls):
        if Singleton.instance is None:
            Singleton.instance = super(Singleton, cls).__new__(cls) 
        return Singleton.instance
