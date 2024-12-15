from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.db import Base


class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    rezume = Column(String)
    info = Column(String)
    created_at = Column(DateTime, default=datetime.now())
