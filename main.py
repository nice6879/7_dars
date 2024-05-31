
import qrcode
import random
import string

def generate_random_string(length=10):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_code(img, filename):
    img.save(filename)

random_link = "https://kun.uz/" + generate_random_string(10)
random_file_name = generate_random_string(10) + ".png"

qr_img = generate_qr_code(random_link)

save_qr_code(qr_img, random_file_name)

print(f"Generated link: {random_link}")
print(f"QR code saved as: {random_file_name}")
