from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

URL = "https://cjdropshipping.com/list/wholesale-womens-clothing-l-2FE8A083-5E7B-4179-896D-561EA116F730.html?fromPage=visitorService&pageNum=2"

# Chrome setup
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 20)

driver.get(URL)

# Wait until product names appear
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "div[class*='ProductCard-index__name']")
))

# Scroll to load more products
for _ in range(7):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

# Find all product cards
names = driver.find_elements(By.CSS_SELECTOR, "div[class*='ProductCard-index__name']")
prices = driver.find_elements(By.CSS_SELECTOR, "span[class*='sellPriceSpan']")
images = driver.find_elements(By.CSS_SELECTOR, "img[data-src]")

print("Products detected:", len(names))

data = []

for i in range(len(names)):
    try:
        name = names[i].text
        price = prices[i].text if i < len(prices) else "N/A"

        # Use high-quality image from data-src
        img_url = images[i].get_attribute("data-src") if i < len(images) else ""

        # Get product link (go up to parent <a>)
        link = names[i].find_element(By.XPATH, "./ancestor::a").get_attribute("href")

        data.append({
            "Product Name": name,
            "Price (USD)": price,
            "Image URL": img_url,
            "Product Link": link
        })

    except Exception as e:
        print("Skipping product:", e)
        continue

# Save CSV
df = pd.DataFrame(data)
df.to_csv("cj_products2.csv", index=False, encoding="utf-8")
print("Saved", len(data), "products to cj_products2.csv")

driver.quit()





