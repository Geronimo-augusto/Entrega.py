# Importaçao da bibliotecas usadas
import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np


# Função para pegar os dados climáticos 
def get_weather_data(city, api_key):
    # Faz a requisição à API da OpenWeather
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        if 'list' in data and len(data['list']) > 0:
            # Extrai os dados climáticos do primeiro item da lista
            first_entry = data['list'][0]
            weather_data = {
                'temperature': first_entry['main']['temp'] if 'main' in first_entry and 'temp' in first_entry['main'] else None,
                'wind_speed': first_entry['wind']['speed'] if 'wind' in first_entry else None,
                'wind_direction': first_entry['wind']['deg'] if 'wind' in first_entry else None,
                'weather_condition': first_entry['weather'][0]['main'] if 'weather' in first_entry and len(first_entry['weather']) > 0 else None,
                'humidity': first_entry['main']['humidity'] if 'main' in first_entry and 'humidity' in first_entry['main'] else None,
                'pressure': first_entry['main']['pressure'] if 'main' in first_entry and 'pressure' in first_entry['main'] else None,
                'current_speed': np.random.uniform(0, 10),  # Simulação de dados de velocidade da corrente
                'current_direction': np.random.uniform(0, 360)  # Simulação de dados de direção da corrente
            }
            return weather_data
        else:
            print('Erro: Nenhum dado de previsão encontrado.')
            return None
    else:
        print(f'Erro: {data["message"]}' if 'message' in data else 'Erro desconhecido')
        return None

# Função para analizar o clima, e a possibilidade de navegar pescar e ou mergulhar 
def analyze_weather_data(weather_data):
    wind_speed = weather_data['wind_speed']
    weather_condition = weather_data['weather_condition']
    
    alerts = []
    navigation_advice = ''
    fishing_advice = ''
    diving_advice = ''
    
    # Condições para navegação
    if wind_speed > 50:
        alerts.append(f'Alerta: Velocidade do vento muito alta - {wind_speed} km/h')
        navigation_advice = 'Não é seguro navegar.'
    else:
        navigation_advice = 'Condições seguras para navegação.'
    
    # Condições para pesca
    if weather_condition in ['Storm', 'Rain']:
        fishing_advice = 'Não é seguro pescar.'
    else:
        fishing_advice = 'Condições favoráveis para pesca.'
    
    # Condições para mergulho
    if wind_speed > 30 or weather_condition in ['Storm', 'Rain']:
        diving_advice = 'Não é seguro mergulhar.'
    else:
        diving_advice = 'Condições favoráveis para mergulho.'
    
    return alerts, navigation_advice, fishing_advice, diving_advice

# Função para gerar o dataset simulado de derramamento de óleo
def generate_dataset():
    # Definir o número de registros
    num_records = 10000

    # Configurar a seed para reprodutibilidade
    np.random.seed(42)

    # Gerar dados simulados
    wind_speed = np.random.uniform(0, 100, num_records)  # Velocidade do vento entre 0 e 100 km/h
    wind_direction = np.random.uniform(0, 360, num_records)  # Direção do vento entre 0 e 360 graus
    current_speed = np.random.uniform(0, 10, num_records)  # Velocidade da corrente entre 0 e 10 km/h
    current_direction = np.random.uniform(0, 360, num_records)  # Direção da corrente entre 0 e 360 graus
    oil_spill = np.random.binomial(1, 0.1, num_records)  # 10% de probabilidade de derramamento de óleo

    # Criar um DataFrame
    data = {
        'wind_speed': wind_speed,
        'wind_direction': wind_direction,
        'current_speed': current_speed,
        'current_direction': current_direction,
        'oil_spill': oil_spill
    }

    df = pd.DataFrame(data)
    # Salvar o dataset em um arquivo CSV
    df.to_csv('simulated_oil_spills.csv', index=False)

# Função para gerar o dataset simulado de tempestades 
def generate_storm_dataset():
    # Definir o número de registros
    num_records = 10000

    # Configurar a seed para reprodutibilidade
    np.random.seed(42)

    # Gerar dados simulados
    wind_speed = np.random.uniform(0, 100, num_records)  # Velocidade do vento entre 0 e 100 km/h
    wind_direction = np.random.uniform(0, 360, num_records)  # Direção do vento entre 0 e 360 graus
    humidity = np.random.uniform(0, 100, num_records)  # Umidade entre 0 e 100%
    pressure = np.random.uniform(950, 1050, num_records)  # Pressão atmosférica entre 950 e 1050 hPa
    storm = np.random.binomial(1, 0.1, num_records)  # 10% de probabilidade de tempestade

    # Criar um DataFrame
    data = {
        'wind_speed': wind_speed,
        'wind_direction': wind_direction,
        'humidity': humidity,
        'pressure': pressure,
        'storm': storm
    }

    df = pd.DataFrame(data)

    # Salvar o dataset em um arquivo CSV
    df.to_csv('simulated_storms.csv', index=False)

# Função para treinar o modelo de previsão de tempestade
def train_storm_model():
    generate_storm_dataset()
    # Carregar dados simulados
    data = pd.read_csv('simulated_storms.csv')

    # Pré-processamento
    X = data[['wind_speed', 'wind_direction', 'humidity', 'pressure']]
    y = data['storm']

    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo de regressão logística
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Avaliar o modelo
    accuracy = model.score(X_test, y_test)

    return model, accuracy

# Função para treinar o modelo de previsão de derramamento de óleo
def train_model():
    generate_dataset()
    # Carregar dados históricos
    data = pd.read_csv('simulated_oil_spills.csv')

    # Pré-processamento
    X = data[['wind_speed', 'wind_direction', 'current_speed', 'current_direction']]
    y = data['oil_spill']

    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo de regressão logística
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Avaliar o modelo
    accuracy = model.score(X_test, y_test)

    return model, accuracy

# Função para fazer previsões de tempestade
def predict_storm(weather_data, model):
    # Garantir que os dados de entrada estejam no formato correto
    input_data = pd.DataFrame([{
        'wind_speed': weather_data['wind_speed'],
        'wind_direction': weather_data['wind_direction'],
        'humidity': weather_data['humidity'],
        'pressure': weather_data['pressure']
    }])
    
    # Fazer previsão usando o modelo treinado
    prediction = model.predict(input_data)
    
    return prediction[0]

# Função para fazer previsões de derramamento de óleo
def predict_oil_spill(weather_data, model):
    # Garantir que os dados de entrada estejam no formato correto
    input_data = pd.DataFrame([{
        'wind_speed': weather_data['wind_speed'],
        'wind_direction': weather_data['wind_direction'],
        'current_speed': weather_data['current_speed'],
        'current_direction': weather_data['current_direction']
    }])
    
    # Fazer previsão usando o modelo treinado
    prediction = model.predict(input_data)
    
    return prediction[0]