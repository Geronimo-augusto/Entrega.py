import dearpygui.dearpygui as dpg
import data 


# Função para atualizar o texto de saída no widget de saída
def update_output(new_text):
    # Obtém o valor atual do texto de saída
    current_output = dpg.get_value("output_text")
    # Adiciona o novo texto ao valor atual
    updated_output = f"{current_output}"+ f"{new_text}\n"
    # Define o valor atualizado no widget de saída
    dpg.set_value("output_text", updated_output)

# Callback para verificar a condição de pesca
def check_fishing_callback(sender, app_data, user_data):
    # Obtém os dados climáticos para a cidade especificada e chave de API
    weather_data = data.get_weather_data(city, api_key)
    # Analisa os dados climáticos para obter conselhos e alertas
    alerts, navigation_advice, fishing_advice, diving_advice = data.analyze_weather_data(weather_data)
    # Atualiza o texto de saída com o conselho de pesca
    update_output(f"Condição para Pesca: {fishing_advice}")

# Callback para verificar a condição de mergulho
def check_diving_callback(sender, app_data, user_data):
    # Obtém os dados climáticos para a cidade especificada e chave de API
    weather_data = data.get_weather_data(city, api_key)
    # Analisa os dados climáticos para obter conselhos e alertas
    alerts, navigation_advice, fishing_advice, diving_advice = data.analyze_weather_data(weather_data)
    # Atualiza o texto de saída com o conselho de mergulho
    update_output(f"Condição para Mergulho: {diving_advice}")

# Callback para verificar a condição de navegação
def check_navigation_callback(sender, app_data, user_data):
    # Obtém os dados climáticos para a cidade especificada e chave de API
    weather_data = data.get_weather_data(city, api_key)
    # Analisa os dados climáticos para obter conselhos e alertas
    alerts, navigation_advice, fishing_advice, diving_advice = data.analyze_weather_data(weather_data)
    # Atualiza o texto de saída com o conselho de navegação
    update_output(f"Condição para Navegação: {navigation_advice}")

# Callback para verificar a previsão de tempestade
def check_storm_callback(sender, app_data, user_data):
    # Obtém os dados climáticos para a cidade especificada e chave de API
    weather_data = data.get_weather_data(city, api_key)
    # Prediz a possibilidade de tempestade usando o modelo treinado
    prediction = data.predict_storm(weather_data, storm_model)
    # Define o resultado da previsão (Sim ou Não)
    result = "Sim" if prediction == 1 else "Não"
    # Atualiza o texto de saída com a previsão de tempestade
    update_output(f"Previsão de Tempestade: {result}")

# Callback para verificar a previsão de derramamento de óleo
def check_oil_spill_callback(sender, app_data, user_data):
    # Obtém os dados climáticos para a cidade especificada e chave de API
    weather_data = data.get_weather_data(city, api_key)
    # Prediz a possibilidade de derramamento de óleo usando o modelo treinado
    prediction = data.predict_oil_spill(weather_data, model)
    # Define o resultado da previsão (Sim ou Não)
    result = "Sim" if prediction == 1 else "Não"
    # Atualiza o texto de saída com a previsão de derramamento de óleo
    update_output(f"Previsão de Derramamento de Óleo: {result}")

# Callback para sair do aplicativo
def exit_app_callback(sender, app_data, user_data):
    # Para a execução do Dear PyGui
    dpg.stop_dearpygui()

# Definindo as credenciais da API e a cidade para obter dados climáticos
api_key = 'c0274666dc5a175af8d72f17a9055742'
city = 'San Francisco'

# Obtendo dados climáticos
weather_data = data.get_weather_data(city, api_key)

# Analisando os dados climáticos para aconselhamento de navegação, pesca e mergulho
alerts, navigation_advice, fishing_advice, diving_advice = data.analyze_weather_data(weather_data)

# Treinando o modelo de previsão de tempestade
storm_model,storm_accuracy = data.train_storm_model()

# Treinando o modelo de previsão de derramamento de óleo
model, accuracy = data.train_model()