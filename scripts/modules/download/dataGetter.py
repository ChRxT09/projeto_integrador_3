from urllib import request

def dataGetter(file_url, file_path):
  request.urlretrieve(file_url , file_path )
