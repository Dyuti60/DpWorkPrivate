import configparser
config=configparser.RawConfigParser()
config.read('.\\configurations\\config.ini')

class readConfig():
    @staticmethod
    def getDpWorkUrl():
        dpWorkUrl = config.get('common info','dp_work_url')
        return dpWorkUrl

    @staticmethod
    def getFieldWorkerUsername():
        FieldWorkerUsername=config.get('common info','field_worker_username')
        return FieldWorkerUsername

    @staticmethod
    def getFieldWorkerPassword():
        FieldWorkerPassword=config.get('common info','field_worker_password')
        return FieldWorkerPassword

    @staticmethod
    def getDistrictAdminUsername():
        DistrictAdminUsername=config.get('common info','district_admin_username')
        return DistrictAdminUsername

    @staticmethod
    def getDistrictAdminPassword():
        DistrictAdminPassword=config.get('common info','district_admin_password')
        return DistrictAdminPassword

    @staticmethod
    def getSuperUserRoleUsername():
        SuperUserRoleUsername=config.get('common info','super_user_role_username')
        return SuperUserRoleUsername

    @staticmethod
    def getSuperUserRolePassword():
        SuperUserRolePassword=config.get('common info','super_user_role_password')
        return SuperUserRolePassword

