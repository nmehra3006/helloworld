class AppDataController(object):

    __data_controller_instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if AppDataController.__data_controller_instance != None:
            raise Exception("AppDataController is a singleton!")
        else:
            AppDataController.__data_controller_instance = self

    @staticmethod
    def getInstance():
        """ Static access method. """
        if AppDataController.__data_controller_instance == None:
            AppDataController()
        return AppDataController.__data_controller_instance


    def write(data):
        print("In write call for controller")
        pass


    def read(query):
        print("In read call for controller")