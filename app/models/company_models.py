from app.models.database.db_models import User

class CompanyModels():
    
    def post_company(self, session, metadata):
        
        user = User(
            name=metadata.name,
            email=metadata.email,
            password=metadata.password,
            role=metadata.role
            )
        session.add(user)
        session.commit()
        session.refresh
        return {"message": "Company added successfully"}