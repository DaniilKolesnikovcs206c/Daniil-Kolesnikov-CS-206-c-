import requests
import random

# URL базы API
BASE_URL = 'https://rickandmortyapi.com/api'

def get_random_character():
    """Получение информации о случайном персонаже"""
    # Генерируем случайный ID персонажа
    character_id = random.randint(1, 826)  # На данный момент в API есть 826 персонажей
    url = f'{BASE_URL}/character/{character_id}'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'name': data['name'],
            'species': data['species'],
            'status': data['status'],
            'gender': data['gender'],
            'location': data['location']['name'],
            'origin': data['origin']['name']
        }
    else:
        return f"Ошибка при получении данных о персонаже: {response.status_code}"

def search_characters_by_name(name):
    """Поиск персонажей по имени"""
    url = f'{BASE_URL}/character/?name={name}'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters = []
        for character in data['results']:
            characters.append({
                'name': character['name'],
                'species': character['species'],
                'status': character['status'],
                'gender': character['gender']
            })
        return characters
    else:
        return f"Ошибка при поиске персонажей: {response.status_code}"

def get_all_locations():
    """Получение списка всех локаций"""
    url = f'{BASE_URL}/location'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        locations = [location['name'] for location in data['results']]
        return locations
    else:
        return f"Ошибка при получении списка локаций: {response.status_code}"

def search_episodes_by_title(title):
    """Поиск эпизодов по названию"""
    url = f'{BASE_URL}/episode/?name={title}'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        episodes = []
        for episode in data['results']:
            episodes.append({
                'name': episode['name'],
                'air_date': episode['air_date'],
                'episode': episode['episode']
            })
        return episodes
    else:
        return f"Ошибка при поиске эпизодов: {response.status_code}"

# Пример использования
if __name__ == '__main__':
    print("Получение случайного персонажа:")
    random_character = get_random_character()
    print(random_character)
    
    print("\nПоиск персонажей по имени 'Rick':")
    characters = search_characters_by_name('Rick')
    for character in characters:
        print(character)

    print("\nПолучение всех локаций:")
    locations = get_all_locations()
    print(locations)

    print("\nПоиск эпизодов по названию 'Rick':")
    episodes = search_episodes_by_title('Rick')
    for episode in episodes:
        print(episode)
