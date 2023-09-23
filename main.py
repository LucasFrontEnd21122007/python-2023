import requests

# Defina a URL do aplicativo Laravel que deseja acessar
url = 'http://exemplo.com/minha-rota-laravel'

try:
    # Faça uma solicitação GET
    response = requests.get(url)

    # Verifique se a resposta foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Imprima o conteúdo da resposta
        print("Resposta do Laravel:")
        print(response.text)
    else:
        print(f"Erro na solicitação. Código de status: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro na solicitação: {e}")
