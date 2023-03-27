from urllib import request

def downloadUrl(file_url, file):
  request.urlretrieve(file_url , file )
