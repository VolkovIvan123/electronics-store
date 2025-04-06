import os
import requests
from pathlib import Path

# Создаем директорию для изображений, если она не существует
images_dir = Path('store/static/store/images')
images_dir.mkdir(parents=True, exist_ok=True)

# Список изображений для загрузки
images = {
    'laptop.jpg': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800',
    'smartphone.jpg': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=800',
    'headphones.jpg': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800',
    'smartwatch.jpg': 'https://images.unsplash.com/photo-1546868871-7041f2a55e12?w=800'
}

# Загружаем каждое изображение
for filename, url in images.items():
    response = requests.get(url)
    if response.status_code == 200:
        with open(images_dir / filename, 'wb') as f:
            f.write(response.content)
        print(f'Загружено: {filename}')
    else:
        print(f'Ошибка загрузки {filename}: {response.status_code}') 