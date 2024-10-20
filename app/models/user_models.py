from fastapi import status, HTTPException
from app.models.database.db_models import User
from sqlalchemy.orm import joinedload

class UserModels():
    
    def check_user(self, session, metadata):
        return session.query(User).filter(User.email == metadata.email).first()
    
    def check_user_id(self, session, id):
        # return session.query(User).filter(User.id == id).first()
        return session.query(User).options(joinedload(User.supervisor)).filter_by(id=id).first()
    
    def post_user(self, session, metadata):
        
        check = self.check_user(session, metadata)
        
        if check is None:
            company = User(
                name=metadata.name,
                email=metadata.email,
                password=metadata.password,
                role=metadata.role
                )
            session.add(company)
            session.commit()
            session.refresh(company)
            return {"message": "user created successfully ", "id": company.id}
        else:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"email: {metadata.email} already exists")
        
        
    def read_user(self, session, id):
        
        check = self.check_user_id(session, id)
        
        if check is not None:
            return check.as_dict()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
        
    def update_user(self, session, id, metadata):
        
        ### validation of email exist ###
        check = self.check_user(session, metadata)
        if check is not None:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"email: {metadata.email} already exists")
        
        ### get user ###
        check = self.check_user_id(session, id)
        
        if check is not None:
            check.name=metadata.name,
            check.email=metadata.email,
            check.password=metadata.password,
            check.role=metadata.role
            check.supervisor_id=metadata.supervisor_id
            
            session.add(check)
            session.commit()
            return {"message": "Update successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        
    
    def delete_user(self, session, id):
        
        ### get user ###
        check = self.check_user_id(session, id)
        
        if check is not None:
            check.account_status=False
            session.commit()
            return {"message": "User successfully deactivated."}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")