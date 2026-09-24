from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class Packet(Base):
    __tablename__ = "packets"

    id = Column(Integer, primary_key=True)
    src_ip = Column(String)
    dst_ip = Column(String)
    protocol = Column(String)
    packet_size = Column(Integer)
