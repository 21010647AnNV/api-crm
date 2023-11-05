from flask import Flask, request, Blueprint
from khachhang.controller import khachhang
import sqlite3
import os

def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    conn = sqlite3.connect('CRM.db')

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS KhachHangTiemNang;")
    cursor.execute("DROP TABLE IF EXISTS NhaCungCap;")

    cursor.execute('''CREATE TABLE KhachHangTiemNang (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Ten CHAR(255) NOT NULL,
        Gmail CHAR(255) UNIQUE NOT NULL,
        SDT CHAR(20) NOT NULL,
        NgheNghiep CHAR(255),
        ThongTinChung TEXT,
        NhaCungCapID INTEGER,
        FOREIGN KEY (NhaCungCapID) REFERENCES NhaCungCap (ID)
    );''')

    cursor.execute('''CREATE TABLE NhaCungCap (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Ten CHAR(255) NOT NULL,
        DiaChi CHAR(255),
        CC CHAR(255),
        BCC CHAR(255),
        ThongTinChung TEXT,
        KhachHangTiemNangID INTEGER,
        FOREIGN KEY (KhachHangTiemNangID) REFERENCES KhachHangTiemNang (ID)
    );''')

    cursor.execute("INSERT INTO KhachHangTiemNang (Ten, Gmail, SDT, NgheNghiep, ThongTinChung) VALUES (?, ?, ?, ?, ?);",
               ('Tên Khách Hàng', 'email@example.com', 'Số Điện Thoại', 'Nghề Nghiệp', 'Thông Tin Chung'))

    cursor.execute("INSERT INTO KhachHangTiemNang (Ten, Gmail, SDT, NgheNghiep, ThongTinChung) VALUES (?, ?, ?, ?, ?);",
                ('Nguyễn Văn A', 'nguyenvana@example.com', '123456789', 'Kỹ sư', 'Thông tin chi tiết về khách hàng'))

    cursor.execute("INSERT INTO NhaCungCap (Ten, DiaChi, CC, BCC, ThongTinChung) VALUES (?, ?, ?, ?, ?);",
                ('Tên Nhà Cung Cấp', 'Địa chỉ nhà cung cấp', 'CC Email', 'BCC Email', 'Thông Tin Chung'))

    cursor.execute("INSERT INTO NhaCungCap (Ten, DiaChi, CC, BCC, ThongTinChung) VALUES (?, ?, ?, ?, ?);",
                ('Công ty ABC', '123 Đường ABC, Thành phố XYZ', 'cc@example.com', 'bcc@example.com', 'Thông tin chi tiết về nhà cung cấp'))

    conn.commit()
    conn.close()

    app.register_blueprint(khachhang)
    return app

