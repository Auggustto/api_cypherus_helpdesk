from app.models.database.db_models import User

class CompanyModels():
    
    def post_company(self, session, metadata):
        
        company = User(
            name=metadata.name,
            email=metadata.email,
            password=metadata.password,
            role=metadata.role
            )
        session.add(company)
        session.commit()
        session.refresh(company)
        return {"message": "Company added successfully", "id": company.id}