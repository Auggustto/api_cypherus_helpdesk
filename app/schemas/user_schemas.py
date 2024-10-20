from pydantic import BaseModel, EmailStr, field_validator


class MetadaUser(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str
    supervisor_id: str
    

    ### validation of supervisor_id if str is none else int ###
    @field_validator('supervisor_id')
    def validar_supervisor_id(cls, valor):
        if isinstance(valor, str) and valor == "":
            return None
            # return ""
        
        return int(valor) if valor is not None else None
    
    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        
        if not any(c.isupper() for c in value) or \
                not any(c.islower() for c in value) or \
                not any(c.isdigit() for c in value) or \
                not any(c in value for c in value):
                    raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        
        return value