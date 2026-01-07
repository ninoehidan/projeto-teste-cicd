import time
import os

print("--- Iniciando App de Teste CI/CD ---")
user = os.getenv('USER_NAME', 'Baptista')
print(f"Olá, {user}! O Jenkins fez o deploy desse container com sucesso.", flush=True)

while True:
    print("Processando dados de teste...", flush=True)
    time.sleep(10)
