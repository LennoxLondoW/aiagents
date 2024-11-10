import requests
import shutil
import secrets
import string




def create_qr_code(data: str) -> str:
    """
    Generates and downloads a QR code image.
    Args:
        data (str): The data to encode in the QR code.
    Returns:
        str: A message indicating success or failure.
    """
    api_key: str = "TwRStognXI3nVl0vVnZWWA==e6ANBsXxjJRfvUJP"
    file_name: str = "qr_codes/"+(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(10))) + ".jpg"
    fmt: str = 'png'
    
    api_url = f'https://api.api-ninjas.com/v1/qrcode?data={data}&format={fmt}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key, 'Accept': f'image/{fmt}'}, stream=True)
    
    if response.status_code == requests.codes.ok:
        with open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        return f"QR code saved successfully as {file_name}."
    else:
        return f"Error: {response.status_code} - {response.text}"


