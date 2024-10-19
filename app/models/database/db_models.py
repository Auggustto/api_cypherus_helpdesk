from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # 'supervisor', 'colaborador'
    supervisor_id = Column(Integer, ForeignKey('users.id'))  # Somente preenchido se for um colaborador

    supervisor = relationship("User", remote_side=[id], backref="colaboradores")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

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

class Comment(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    comment = Column(Text, nullable=False)

    ticket = relationship("Ticket", backref="comments")
    user = relationship("User")

    created_at = Column(TIMESTAMP, server_default=func.now())

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)

    created_at = Column(TIMESTAMP, server_default=func.now())

class TicketCategory(Base):
    __tablename__ = 'ticket_categories'

    ticket_id = Column(Integer, ForeignKey('tickets.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), primary_key=True)

    ticket = relationship("Ticket", backref="ticket_categories")
    category = relationship("Category", backref="ticket_categories")

class TicketResponsible(Base):
    __tablename__ = 'ticket_responsibles'

    ticket_id = Column(Integer, ForeignKey('tickets.id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    ticket = relationship("Ticket", backref="responsibles")
    user = relationship("User")

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Usuário que receberá a notificação
    ticket_id = Column(Integer, ForeignKey('tickets.id'))  # Ticket relacionado à notificação
    message = Column(Text, nullable=False)  # Mensagem da notificação
    is_read = Column(Boolean, default=False)  # Status de leitura

    user = relationship("User")
    ticket = relationship("Ticket")

    created_at = Column(TIMESTAMP, server_default=func.now())
