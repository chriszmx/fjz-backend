from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://buahjlpraqcgfr:79acca9b13aee2e87aa1ec40ce28b316cffca26abfcf6271695aa070c9279759@ec2-3-92-151-217.compute-1.amazonaws.com:5432/d33u912bcdif9u"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
