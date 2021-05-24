from yaml import safe_load
import os

class Config:
    def __init__(self,
                 config_file: str = None,
                 api_key: str = None,
                 admin_key: str = None,
                 lnbits_url: str = None):
    
        self._config_file = config_file
        self._api_key = api_key
        self._lnbits_url = lnbits_url
        self._admin_key = admin_key

        try:
            if api_key or admin_key or lnbits_url is None:
                path  = os.getcwd()
                config_file = path + '/config.yml'
                print(config_file)
                
            with open(config_file, 'rb') as f:
                cfile = safe_load(f)
            f.close()
            
            self._api_key = cfile['api_key']
            self._lnbits_url = cfile['lnbits_url']
            self._admin_key = cfile['admin_key']  
        except Exception as e:
            print(e)

        
    @property
    def api_key(self):
        return self._api_key

    @property
    def admin_key(self):
        return self._admin_key

    @property
    def lnbits_url(self):
        return self._lnbits_url
    
    def headers(self):
        data = {"X-Api-Key" : self._api_key, "Content-type" : "application/json"}
        return data

    def admin_headers(self):
        data = {"X-Api-Key" : self._admin_key, "Content-type" : "application/json"}
        return data


if __name__ == '__main__':
    c = Config()
    
    print(c.api_key)
    print(c.lnbits_url)
    print(c.headers())
    print(c.admin_headers())
    
    
