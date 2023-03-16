import configparser as cp
cod=cp.RawConfigParser()
cod.read(r'D:\testing_pro1\project_level\sample_project\utilities_files\data_cre.ini')
class red():
    @staticmethod
    def user():
        return cod.get('common info','user')
    
    @staticmethod
    def user_input_id():
        return cod.get('common info','user_input_id')
    
    @staticmethod
    def uesr_password_id():
        return cod.get('common info','user_password_id')
    

    @staticmethod
    def password():
        return cod.get('common info','password')