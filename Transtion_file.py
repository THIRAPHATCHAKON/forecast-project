import email
import os

# <<< ตรงนี้เปลี่ยนชื่อไฟล์ mhtml ให้ตรงของคุณ >>>
MHTML_FILE = "Dataset.mhtml"
HTML_OUT   = "rain_khonkaen_2024_2025.html"


# 1) อ่านไฟล์ mhtml ทั้งไฟล์
with open(MHTML_FILE, "rb") as f:
    raw = f.read()

# 2) ใช้ email parser แยกส่วนของ HTML ออกมา
msg = email.message_from_bytes(raw)

html_parts = []
for part in msg.walk():
    if part.get_content_type() == "text/html":
        payload = part.get_payload(decode=True)  # auto decode (quoted-printable / base64)
        charset = part.get_content_charset() or "utf-8"
        html_parts.append(payload.decode(charset, errors="ignore"))

if not html_parts:
    raise RuntimeError("ไม่เจอส่วน HTML ในไฟล์ MHTML เลย")

html = "\n".join(html_parts)

# 3) เซฟเป็นไฟล์ HTML ปกติ
with open(HTML_OUT, "w", encoding="utf-8") as f:
    f.write(html)

print("แปลงเสร็จแล้ว ->", os.path.abspath(HTML_OUT))
