from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Configuración del servicio de ChromeDriver
service = Service(ChromeDriverManager().install())

# Configuración del controlador de Chrome con opciones
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    # Abre Amazon México
    driver.get("https://www.amazon.com.mx")

    # Espera a que el cuadro de búsqueda esté presente y realiza la búsqueda
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("Discos duros SSD")
    search_box.submit()

    # Espera a que aparezcan los resultados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )

    # Filtra por la marca ADATA
    filter_brand = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='ADATA']"))
    )
    filter_brand.click()

    # Espera a que se realice la selección de la marca
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@aria-label='ADATA']"))
    )

    # Abre el menú de ordenamiento
    sort_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "a-autoid-0-announce"))
    )
    sort_dropdown.click()

    # Selecciona ordenar por menor precio
    sort_low_to_high = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "s-result-sort-select_1"))
    )
    sort_low_to_high.click()

    # Mantén el navegador abierto
    print("Navegador abierto. La búsqueda se completó y los resultados están ordenados por menor precio.")

    # Espera a que el usuario presione una tecla para cerrar
    input("Presiona cualquier tecla para cerrar el navegador...")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    # Cierra el navegador
    driver.quit()
