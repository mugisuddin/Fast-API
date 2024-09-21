
from sqlalchemy import column, Integer, String, Boolean
from sqlalchemy.sql.expression import null
from .database import Base

class Post(Base):
    __tablename__ = "Post"

    id = column(Integer, primary_key=True, nullable=False)
    title = column(String, nullable=False)
    content = column(String, nullable=False)
    published = column(Boolean, default=True)
    
