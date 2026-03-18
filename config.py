import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    # API
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", 8000))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./payments.db")
    
    # DAI Configuration
    DAI_CONTRACT_ADDRESS = os.getenv("DAI_CONTRACT_ADDRESS", "0x6B175474E89094C44Da98b954EedeAC495271d0F")
    WEB3_PROVIDER_URL = os.getenv("WEB3_PROVIDER_URL", "")
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    
    class Config:
        env_file = ".env"

settings = Settings()