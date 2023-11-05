from flask import Blueprint

khachhang = Blueprint("khachhang", __name__)
@khachhang.route("/khachhang")
def get_khachhang():
    return("sdfjhsdk")