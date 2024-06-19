from datetime import datetime
from PIL import Image
import cv2
import requests
import numpy as np

def capture_video():
    # URL da live
    url = 'http://127.0.0.1:8000/'

    # Abre uma sessão para a captura do stream
    session = requests.Session()

    # Envia uma requisição GET para o servidor
    response = session.get(url, stream=True)

    if response.status_code != 200:
        print("Erro ao acessar a live")
    else:
        bytes_data = b''
        for chunk in response.iter_content(chunk_size=1024):
            bytes_data += chunk
            a = bytes_data.find(b'\xff\xd8')  # JPEG início
            b = bytes_data.find(b'\xff\xd9')  # JPEG fim
            if a != -1 and b != -1:
                jpg = bytes_data[a:b+2]
                bytes_data = bytes_data[b+2:]

                # Converte bytes em uma imagem numpy
                frame = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)

                # Mostra a imagem
                cv2.imshow('Live', frame)

                # Salva o frame atual como uma imagem (opcional)
                cv2.imwrite('frame_capturado.jpg', frame)

                # Pressione 'q' para sair do loop e fechar a janela
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

    # Libera os recursos
    cv2.destroyAllWindows()
    response.close()

while True:
    hora = datetime.now().strftime('%H:%M')
    if True:
        capture_video()

    if hora == '19:45':
        capture_video() 