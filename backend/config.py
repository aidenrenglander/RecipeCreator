import os

class Config:
    SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY', '92a8e85b760c47289c4c1441dc932b29')
