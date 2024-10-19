from app.models.company_models import CompanyModels

class CompanyServices(CompanyModels):
    
    def post_company(self, session, metadata):
        return super().post_company(session, metadata)