import qrcode
from typing import Text

def generate_qr_link(device_serial_number: Text):
    obj_qr = qrcode.QRCode(  
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)  
    obj_qr.add_data(f"http://127.0.0.1:8000/qr/scan_device?serial_num={device_serial_number}")
    obj_qr.make(fit=True)
    qr_img = obj_qr.make_image(fill_color = "black", back_color="white")
    qr_image_path = f"qr_images/qr_code_{device_serial_number}.png"
    qr_img.save(qr_image_path)
    return qr_image_path


