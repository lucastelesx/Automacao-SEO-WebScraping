import requests
from bs4 import BeautifulSoup
from utils_view import display_html, log_success, log_error, log, log_pretty
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from utils_seo import check_valid



def get_session_retries():
  session = requests.Session()
  session.headers.update({
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
  })

  retry_rules = Retry(
    total=5,             
    status_forcelist=[429, 500, 502, 503, 504], 
    backoff_factor=1,
    allowed_methods=["GET"]
  )

  adapter = HTTPAdapter(max_retries=retry_rules)
  session.mount("http://", adapter)
  session.mount("https://", adapter)

  return session

def auditar_urls(url_list, session):
  for url in url_list:
    try:
      response = session.get(url, timeout=10)

      is_response_ok = response.status_code == requests.codes.ok
      if is_response_ok:
        html_doc = response.text
        soup = BeautifulSoup(html_doc, 'html.parser')

        selectors = [
          "title", 
          "link[rel='canonical']", 
          "h1", 
          "h2", 
          "meta[name='description']", 
          "meta[name='robots']",
          "meta[class='keywords']"
        ]
        log_pretty(check_valid(selectors, soup))
      else:
        log_error(f"❌ Alerta de SEO: Status {response.status_code}")
        
    except requests.exceptions.RequestException as e:
      log_error(f'{e}')

if __name__ == "__main__":
  session_retries = get_session_retries()

  with open("./urls_para_auditar.txt") as file_urls:
    file_url_list = [url.rstrip('\n') for url in file_urls.readlines()]
    print('urls:', file_url_list)

  auditar_urls(file_url_list, session_retries)