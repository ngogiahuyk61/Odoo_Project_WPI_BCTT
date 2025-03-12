# Sử dụng image chính thức của Odoo 17.0
FROM odoo:17.0

# Thiết lập thư mục làm việc
WORKDIR /var/lib/odoo

# Copy thư mục addons tùy chỉnh và file cấu hình vào container
COPY ./addons /mnt/extra-addons
COPY ./config/odoo.conf /etc/odoo/odoo.conf

# Expose cổng được Render cung cấp qua biến môi trường PORT
EXPOSE $PORT

# Chạy Odoo:
# - "-i base" buộc cài đặt module cơ bản nếu cơ sở dữ liệu chưa được khởi tạo
# - "--xmlrpc-port ${PORT}" sử dụng cổng từ biến môi trường PORT
CMD ["sh", "-c", "odoo -i base --xmlrpc-port ${PORT} --dev all"]



