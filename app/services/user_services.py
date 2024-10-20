from app.models.user_models import UserModels

class UserServices(UserModels):
    
    def post_user(self, session, metadata):
        return super().post_user(session, metadata)
    
    def read_user(self, session, id):
        return super().read_user(session=session, id=id)
    
    def update_user(self, session, id, metadata):
        return super().update_user(session=session, id=id, metadata=metadata)
    
    def delete_user(self, session, id):
        return super().delete_user(session=session, id=id)