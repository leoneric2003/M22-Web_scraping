# Código generado con ayuda de IA
# Corregido por: Eirc León Olivares
#Este programa enlaza a la página de Amazón en Español y busca Discos Duros
# SSD de la marca ADATA
# Esta la versión mas reciente, ya que se brinca la parte de"No soy un robot"


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random
import time

# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Configuración del controlador de Chrome con opciones
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

driver = webdriver.Chrome(service=service, options=options)

def human_delay():
    """Función para introducir una pausa aleatoria"""
    time.sleep(random.uniform(1.5, 3.5))

try:
    driver.get("https://www.amazon.com.mx")
    human_delay()

    # Búsqueda
    try:
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys("Discos duros SSD")
        human_delay()
        search_box.submit()
    except Exception as e:
        print(f"Error durante la búsqueda: {e}")

    # Filtrado por marca
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
        )
        filter_brand = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='ADATA']"))
        )
        filter_brand.click()
        human_delay()
    except Exception as e:
        print(f"Error durante el filtro de marca: {e}")

    # Ordenar por menor precio
    try:
        sort_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "a-autoid-0-announce"))
        )
        sort_dropdown.click()
        human_delay()
        sort_low_to_high = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "s-result-sort-select_1"))
        )
        sort_low_to_high.click()
        human_delay()
    except Exception as e:
        print(f"Error durante el ordenamiento: {e}")

    print("Navegador abierto. La búsqueda se completó y los resultados están ordenados por menor precio.")
    input("Presiona cualquier tecla para cerrar el navegador...")

finally:
    driver.save_screenshot('screenshot.png')  # Captura de pantalla en caso de error
    driver.quit()

