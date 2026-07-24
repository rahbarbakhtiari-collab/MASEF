# پروفایل افزونه وردپرس

## اطلاعات اجباری

- نسخه WordPress
- نسخه PHP و MySQL/MariaDB
- قالب و افزونه‌های کلیدی
- Multisite یا Single Site
- روش Cache
- محیط Staging

## دروازه‌های افزوده

- WordPress Coding Standards
- بررسی Capability و Nonce
- Sanitization و Escaping
- آزمون فعال‌سازی/غیرفعال‌سازی
- آزمون Upgrade از نسخه قبلی
- بررسی حذف داده در Uninstall
- بسته ZIP قابل نصب از Commit مشخص
- Rollback به ZIP قبلی و Restore داده در صورت نیاز

## ساختار پیشنهادی

```text
plugin-slug/
├── plugin-slug.php
├── includes/
├── admin/
├── public/
├── assets/
├── languages/
├── tests/
└── uninstall.php
```
