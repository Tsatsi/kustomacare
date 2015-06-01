class Base(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class Production(Base):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:riley123@localhost/swift_web_dev'


class Development(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:riley123@localhost/swift_web_dev'


class Testing(Base):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
