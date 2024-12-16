## Đóng góp của các thành viên
- Nguyễn Phúc Hiệp: 20%
- Phạm Hữu Thiện: 20%
- Nguyễn Đa Đa: 20%
- Trần Vũ Huỳnh Đức: 20%
- Bùi Văn Duy Tính: 20%

# Danh sách testcase

## Valid account
- "standard_user", "secret_sauce"

## Epic sadface: Sorry, this user has been locked out.
- "locked_out_user", "secret_sauce"
## Epic sadface: Sorry, this user has been locked out.
- "locked_out_user", "secret_sauce"

## Epic sadface: Password is required
- "standard_user", ""

## Epic sadface: Username is required
- "", "secret_sauce"

## Epic sadface: Username and password are required
- "", ""

## Epic sadface: Username and password do not match any user in this service
- "standard_user", "error"
- "error", "secret_sauce"