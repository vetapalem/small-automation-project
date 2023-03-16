import configparser as cp
cod=cp.RawConfigParser() # readin .ini file
cod.read(r'..\utilities_files\data_cre.ini') #add .ini file path 
class red():
    @staticmethod
    def user():#read user 
        return cod.get('common info','user')
    
    @staticmethod
    def user_input_id():#read user input
        return cod.get('common info','user_input_id')
    
    @staticmethod
    def uesr_password_id():#read user password
        return cod.get('common info','user_password_id')
    

    @staticmethod
    def password():
        return cod.get('common info','password')
