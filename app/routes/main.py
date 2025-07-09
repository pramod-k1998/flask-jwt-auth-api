from flask import Blueprint
from flask_jwt_extended import jwt_required

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
@jwt_required()
def home():
    return {"message": "Welcome to the protected home page!"}
