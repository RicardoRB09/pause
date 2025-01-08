# 🌶🌶🌶 Usando la documentación de la imágenes https://developers.themoviedb.org/3/getting-started/images

# Convierte las URLs de las imágenes en verdaderas imágenes en el HTML (usa el tamaño w500)
# Crea un menu HTML al inicio del archivo para que enlace ambas páginas y permita navegar entre ellas fácilmente (no se evaluará diseño CSS). El menu HTML puede ser añadido a la tabla manualmente o por código


import requests, json, yaml, os


MOVIEDB_CONFIG_FILE = "auth.yaml"

movies = []

base_poster_path_url = 'https://image.tmdb.org/t/p/w200'


      
    
def get_movies_by_page(page):
    with open(os.path.join(MOVIEDB_CONFIG_FILE), 'r') as config_file:
        try:
            config = yaml.safe_load(config_file)
        except yaml.YAMLError as exc:
            print(f'🚨 There was an exception in the YAML : {exc}')
            
    API_KEY = config['moviedb']['api_key']
    ACCESS_TOKEN = config['moviedb']['access_token']

    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + ACCESS_TOKEN
    }
    
    url = f"https://api.themoviedb.org/3/trending/movie/week?page={page}"
    
    response = requests.get(url, headers=headers)
    
    print(response.status_code)
    
    if response.status_code != 200:
        print('⚠️⚠️ Cannot continue with the execution... Try again! ⚠️⚠️\n')
        return []
        
    return json.loads(response.content)['results']

    


