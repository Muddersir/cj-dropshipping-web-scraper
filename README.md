🛒 CJ Dropshipping Product Data Scraper

A Python-based web scraping project that extracts product data from the CJ Dropshipping e-commerce platform using Selenium automation and Pandas data processing.

This scraper handles dynamic JavaScript-loaded content, scroll-based product loading, and structured data collection across multiple category pages.

🚀 Project Goal

To build a scalable scraping pipeline that:

Collects product data page by page

Extracts data from multiple categories

Combines all scraped datasets into a single structured CSV file

Demonstrates real-world web automation and data engineering skills

📦 Data Collected

For each product, the scraper collects:

🏷 Product Name

💲 Price

🖼 Product Image URL

🔗 Product Page Link

📂 Category (planned)

📁 Subcategory (planned)

🖼 Detail Images (planned)

🏭 Brand (planned)

🧠 How It Works

Open a CJ Dropshipping category page

Scroll to trigger dynamic product loading

Extract product data from visible cards

Move page by page within the category

Store data for each page separately

Use Pandas to merge all pages into one dataset

Repeat for all categories

Export final combined CSV

🛠 Technologies Used

Tool	Purpose
Python	Core programming language
Selenium	Browser automation & dynamic scraping
WebDriver Manager	Auto-manages Chrome driver
Pandas	Data cleaning and merging
dotenv	Environment variable management

1️⃣ Clone Repository
git clone https://github.com/Muddersir/cj-dropshipping-web-scraper.git
cd cj-dropshipping-web-scraper

2️⃣ Install Dependencies
pip install -r requirements.txt

Run Scraper
python scraper/main.py

📊 Output

The scraper generates structured CSV files containing product data, demos are given above.
