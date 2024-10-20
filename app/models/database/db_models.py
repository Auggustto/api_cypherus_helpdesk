from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from collections import Counter

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # 'supervisor', 'colaborador'
    supervisor_id = Column(Integer, ForeignKey('users.id'))  # Somente preenchido se for um colaborador
    account_status = Column(Boolean, default=True, nullable=False)

    supervisor = relationship("User", remote_side=[id], backref="colaboradores")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'supervisor_id': self.supervisor_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    

class Ticket(Base):
    __tablename__ = 'tickets'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)  # 'aberto', 'em andamento', 'fechado', 'reaberto'
    priority = Column(String(50), nullable=False)  # 'baixa', 'média', 'alta', 'urgente'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Usuário que criou o ticket
    supervisor_id = Column(Integer, ForeignKey('users.id'))  # Supervisor que supervisiona o ticket

    user = relationship("User", foreign_keys=[user_id])
    supervisor = relationship("User", foreign_keys=[supervisor_id])

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    
    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'user_id': self.user_id,
            'supervisor_id': self.supervisor_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(Text, nullable=False)

    ticket = relationship("Ticket", backref="comments")
    user = relationship("User")

    created_at = Column(TIMESTAMP, server_default=func.now())
    
    def as_dict(self):
        return {
            'id': self.id,
            'ticket_id': self.ticket_id,
            'user_id': self.user_id,
            'comment': self.comment,
            'created_at': self.created_at.isoformat()
        }

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())
    
    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat()
        }

class TicketCategory(Base):
    __tablename__ = 'ticket_categories'

    ticket_id = Column(Integer, ForeignKey('tickets.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)

    ticket = relationship("Ticket", backref="ticket_categories")
    category = relationship("Category", backref="ticket_categories")
    
    def as_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'category_id': self.category_id
        }

class TicketResponsible(Base):
    __tablename__ = 'ticket_responsibles'

    ticket_id = Column(Integer, ForeignKey('tickets.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    ticket = relationship("Ticket", backref="responsibles")
    user = relationship("User")
    
    def as_dict(self):
        return {
            'ticket_id': self.ticket_id,
            'user_id': self.user_id
        }

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False) 
    ticket_id = Column(Integer, ForeignKey('tickets.id')) 
    message = Column(Text, nullable=False) 
    is_read = Column(Boolean, default=False) 

    user = relationship("User")
    ticket = relationship("Ticket")

    created_at = Column(TIMESTAMP, server_default=func.now())
    
    def as_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'ticket_id': self.ticket_id,
            'message': self.message,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat()
        }
