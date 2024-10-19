from app.services.company_services import CompanyServices

class CompanyController(CompanyServices):
    
    def post_company(self, session, metadada):
        return super().post_company(session, metadada)