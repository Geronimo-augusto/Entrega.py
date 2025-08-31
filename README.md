# Projeto de Monitoramento e Previsão para Pescadores

Este projeto fornece um sistema de monitoramento e previsão para condições marítimas e climáticas, especialmente voltado para pescadores como Lineu de Freitas, uma persona que enfrenta desafios devido às condições ambientais e busca promover práticas de pesca sustentável.

## Estrutura do Projeto

O projeto está organizado em três arquivos principais:

1. **data.py**: Contém as funções de coleta de dados climáticos e geração de datasets simulados.
2. **engine.py**: Contém as funções de callback que processam os dados e realizam previsões.
3. **main.py**: Contém a interface gráfica desenvolvida com Dear PyGui.

## Funcionalidades

O sistema possui as seguintes funcionalidades:
- **Previsão de Condições para Pesca**
- **Previsão de Condições para Mergulho**
- **Previsão de Condições para Navegação**
- **Previsão de Derramamento de Óleo**
- **Previsão de Tempestades**

## Requisitos
- Python 3.6+
- Bibliotecas:
  - requests
  - pandas
  - scikit-learn
  - dearpygui
  - numpy
=======
- Python 3.x: O código foi desenvolvido em Python 3.

- Bibliotecas: Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalar as dependências executando o seguinte comando:


## Uso
- Executar o arquivo entrega_gs.exe

## Utilidade dos arquivos

1. **data.py**: Contém as funções para coleta de dados e geração de datasets. Exemplo de uso:
    ```python
        import data 

        api_key = 'sua_api_key'
        city = 'San Francisco'
        weather_data = get_weather_data(city, api_key)
    ```


2. **engine.py**: Contém as funções para analisar dados e realizar previsões. Exemplo de uso:
    ```python
        import engine 

        # Treinar modelos
        model, accuracy = train_model()
        storm_model, storm_accuracy = train_storm_model()

        # Fazer previsões
        prediction = predict_oil_spill(weather_data, model)
        storm_prediction = predict_storm(weather_data, storm_model)
    ```

3. **main.py**: Executa a interface gráfica:
    ```python
        import dearpygui.dearpygui as dpg
        import engine

## Funcionamento do Código
### Coleta de Dados Climáticos
A função `get_weather_data(city, api_key)` na linha 13 é responsável por obter os dados climáticos da API da OpenWeatherMap para a cidade especificada. Ela usa a chave da API e a cidade como entrada e retorna os dados climáticos.

### Análise dos Dados Climáticos
A função `analyze_weather_data(weather_data)` na linha 37 analisa os dados climáticos coletados e fornece aconselhamento sobre navegação, pesca e mergulho com base nessas condições. Ela retorna alertas e aconselhamento para cada atividade.

### Treinamento do Modelo de Tempestade
A função `train_storm_model()` na linha 83 é responsável por gerar e treinar um modelo de aprendizado de máquina para prever tempestades. Ela retorna o modelo treinado e sua precisão.

### Treinamento do Modelo de Derramamento de Óleo
A função `train_model()` na linha 113 é responsável por gerar e treinar um modelo de aprendizado de máquina para prever derramamentos de óleo. Ela retorna o modelo treinado e sua precisão.

        # Código da interface
        # ...
        
        # Iniciar a interface
        dpg.start_dearpygui()
    ```

## Exemplo de Interface

No arquivo `main.py`, a interface gráfica foi criada usando Dear PyGui. Aqui está um exemplo simplificado de como a interface está configurada:

```python
    import dearpygui.dearpygui as dpg
    import engine

    # Configuração da interface
    dpg.create_context()

    with dpg.window(label="Sistema de Monitoramento Marítimo"):
        dpg.add_text("Clique em um dos botões abaixo para obter a previsão correspondente.")


        button_id1= dpg.add_button(label="Verificar Condição de Pesca", callback=engine.check_fishing_callback)
        button_id2= dpg.add_button(label="Verificar Condição de Mergulho", callback=engine.check_diving_callback)
        button_id3= dpg.add_button(label="Verificar Condição de Navegação", callback=engine.check_navigation_callback)
        button_id4= dpg.add_button(label="Verificar Tempestade", callback=engine.check_storm_callback)
        button_id5= dpg.add_button(label="Verificar Previsão de Derramamento de Óleo", callback=engine.check_oil_spill_callback)
        dpg.add_button(label="Sair", callback=engine.exit_app_callback)


        dpg.bind_item_theme(button_id1, button_theme)
        dpg.bind_item_theme(button_id2, button_theme)
        dpg.bind_item_theme(button_id3, button_theme)
        dpg.bind_item_theme(button_id4, button_theme)
        dpg.bind_item_theme(button_id5, button_theme)

        output_text_id = dpg.add_text("", tag="output_text")
        dpg.bind_item_theme(output_text_id, text_theme)


        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

```
# Autores
## Grupo GRM solutions
### Integrantes:
- Geronimo Augusto RM- 557170
- Murilo Cordeiro RM- 556727

link do repositório: https://github.com/Geronimo-augusto/Entrega.py
link do video no youtube: https://www.youtube.com/watch?v=1I2rtX8d3KA