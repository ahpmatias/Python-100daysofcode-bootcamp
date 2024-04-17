import requests
import lxml
from bs4 import BeautifulSoup


PRODUCT_URL = ('https://www.amazon.de/dp/B002HYGWX6/ref=sspa_dk_detail_0?psc=1&pd_rd_i=B002HYGWX6&pd_rd_w=ZoGaR&content-id=amzn1.sym.d9f88fbb-7ec7-4155-9602-43fd71456ba4&pf_rd_p=d9f88fbb-7ec7-4155-9602-43fd71456ba4&pf_rd_r=PZS15THEJZTC8MZPDVK0&pd_rd_wg=aL5AT&pd_rd_r=f8a97cfc-2fa9-4d9d-8516-8a954f349309&s=musical-instruments&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM')

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'sec-fetch-dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.7',
    'X-Forwarded-For': '78.35.70.222'
}

response = requests.get(PRODUCT_URL, headers=header)
amazon_webpage_data = response.text
print(amazon_webpage_data)
soup = BeautifulSoup(amazon_webpage_data, 'lxml')
price = soup.select('a-price-whole')
print(price)

