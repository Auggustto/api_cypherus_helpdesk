from pydantic import BaseModel, EmailStr, field_validator


class MetadaCompany(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    
    # @field_validator("password")
    # def validate_password(cls, value):
    #     if len(value) < 8:
    #         raise ValueError("Password must be at least 8 characters long.")
        
    #     if not any(c.isupper() for c in value) or \
    #             not any(c.islower() for c in value) or \
    #             not any(c.isdigit() for c in value) or \
    #             not any(c in value for c in value):
    #                 raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        
    #     return value