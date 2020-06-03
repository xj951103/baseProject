

def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    db = dbinfo.get("DB")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, db)


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRECT_KEY = "jonathan"


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "",
        "USER": "",
        "PASSWORD": "",
        "DRIVER": "",
        "HOST": "",
        "PORT": "",
        "DB": ""
    }

    SQLALCHEMY_DATABASES_URI = ""


class TestConfig(Config):
    TESTING= True
    dbinfo = {
        "ENGINE": "",
        "USER": "",
        "PASSWORD": "",
        "DRIVER": "",
        "HOST": "",
        "PORT": "",
        "DB": ""
    }

    SQLALCHEMY_DATABASES_URI = ""


class StagineConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "USER": "",
        "PASSWORD": "",
        "DRIVER": "",
        "HOST": "",
        "PORT": "",
        "DB": ""
    }

    SQLALCHEMY_DATABASES_URI = ""


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "",
        "USER": "",
        "PASSWORD": "",
        "DRIVER": "",
        "HOST": "",
        "PORT": "",
        "DB": ""
    }

    SQLALCHEMY_DATABASES_URI = ""


envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagineConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}