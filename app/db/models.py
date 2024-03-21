from app.db.models import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime

Base = declarative_base()

class Data(Base):
    __tablename__ = 'dataset'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    time = Column(String(12), nullable=True)
    site = Column(String(32), nullable=False)

    images = relationship('Image', back_populates='dataset')
    columns = relationship('Col', secondary='files', back_populates='data')

    def __repr__(self):
        return f"<Data(name='{self.site}', date='{self.date}', time='{self.time}')>"

class Col(Base):
    __tablename__ = 'columns'
    id = Column(Integer, primary_key=True)
    min = Column(Float, nullable=False)
    median = Column(Float, nullable=False)
    max = Column(Float, nullable=False)
    index = Column(Integer, nullable=False)

    dataset = relationship('Data', secondary='files', back_populates='columns')
    stats = relationship('Statistic', back_populates='columns')

    def __repr__(self):
        return f"<index='{self.index}')>"

class Stat(Base):
    __tablename__ = 'statistics' 
    id = Column(Integer, primary_key=True)
    min_abs = Column(Float, nullable=False)
    median_abs = Column(Float, nullable=False)
    max_abs = Column(Float, nullable=False)
    mean = Column(Float, nullable=True)
    mode = Column(Float, nullable=True)
    
    column_id = Column(Integer, ForeignKey('columns.id'), primary_key=True)
    columns = relationship('Col', back_populates='stats')

    def __repr__(self):
        return f"<Statistic(min_abs='{self.min_abs}', median_abs='{self.median_abs}', max_abs='{self.max_abs}', mean='{self.mean}', mode='{self.mode}')>"

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name_cols = Column(String(64), nullable=False)

    data_id = Column(Integer, ForeignKey('dataset.id'), primary_key=True)
    data = relationship('Data', back_populates='files')
    column_id = Column(Integer, ForeignKey('columns.id'), primary_key=True)
    columns = relationship('Col', back_populates='files')

    def __repr__(self):
        return f"<File(name='{self.name_cols}')>"

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)

    data_id = Column(Integer, ForeignKey('dataset.id'), primary_key=True)
    dataset = relationship('Data', back_populates='images')

    def __repr__(self):
        return f"<Image(name='{self.name}')>"
'''
class User(Base):
    
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    email = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    state = Column(Boolean) #Estado del usuario activo o inactivo

class UserId
'''