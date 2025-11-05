import qrcode

def text_to_lqr(text):
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=1,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    matrix = qr.get_matrix()
    
    output = []
    for row in matrix:
        line = ''.join('█' if cell else '░' for cell in row)
        output.append(line)
    return '\n'.join(output)
