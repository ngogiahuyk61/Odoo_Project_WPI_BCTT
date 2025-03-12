# Dùng image chính thức của Odoo phiên bản 17.0
FROM odoo:17.0

# Đặt thư mục làm việc (không bắt buộc)
WORKDIR /var/lib/odoo

# Copy thư mục addons tùy chỉnh vào container
COPY ./addons /mnt/extra-addons

# Copy file cấu hình Odoo vào container
COPY ./config/odoo.conf /etc/odoo/odoo.conf

# Expose cổng 8069 để Odoo phục vụ web
EXPOSE 8069

# Chạy Odoo với chế độ dev
CMD ["odoo", "--dev", "all"]
