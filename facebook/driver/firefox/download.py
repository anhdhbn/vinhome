import requests
import re
import io
import tarfile
import glob

def check_exists():
  files = [f for f in glob.glob("./geckodriver")]
  return len(files) != 0

def download_file(url):
  local_filename = url.split('/')[-1]
  # NOTE the stream=True parameter below
  with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open(local_filename, 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192): 
        if chunk: # filter out keep-alive new chunks
          f.write(chunk)
          # f.flush()
  return local_filename

def download_driver():
  if check_exists():
    print("driver was downloaded")
    return
  response = requests.get("https://github.com/mozilla/geckodriver/tags")

  if response.status_code != 200:
    print("Can not fetch data...")
    return

  version = re.search(r'v0\.\d{2}\.0', response.text).group(0)
  download_link = f"https://github.com/mozilla/geckodriver/releases/download/{version}/geckodriver-{version}-linux64.tar.gz"
  
  download_file(download_link)
  tar = tarfile.open(f"geckodriver-{version}-linux64.tar.gz", "r:gz")
  tar.extractall()
  tar.close()