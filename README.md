# Sistema de Previsão de Condições Climáticas

Este é um sistema simples para prever condições climáticas usando a API da OpenWeatherMap. O sistema fornece aconselhamento sobre navegação, pesca e mergulho com base nos dados climáticos coletados. Além disso, inclui modelos de aprendizado de máquina para prever tempestades e derramamentos de óleo.

## Requisitos
- Python 3.x: O código foi desenvolvido em Python 3.

- Bibliotecas: Certifique-se de ter as bibliotecas necessárias instaladas. Você pode instalar as dependências executando o seguinte comando:

```bash
pip install -r requirements.txt
```
## Como Usar
### 1. Obtendo a Chave da API
Antes de usar o sistema, é necessário obter uma chave da API da OpenWeatherMap. Você pode se inscrever e obter uma chave gratuita em openweathermap.org. Após obter a chave, defina-a como api_key no código Python.

### 2. Definindo a Cidade
Defina a cidade desejada em city no código Python. Isso garantirá que os dados climáticos sejam obtidos para a cidade correta.

### 3. Executando o Script
Para executar o sistema, basta executar o script Python main.py:

```bash
python main.py
```
O sistema irá coletar dados climáticos, analisá-los e fazer previsões de tempestade e derramamento de óleo com base nesses dados.

## Funcionamento do Código
### Coleta de Dados Climáticos
A função get_weather_data(city, api_key) na linha 13 é responsável por obter os dados climáticos da API da OpenWeatherMap para a cidade especificada. Ela usa a chave da API e a cidade como entrada e retorna os dados climáticos.

### Análise dos Dados Climáticos
A função analyze_weather_data(weather_data) na linha 37 analisa os dados climáticos coletados e fornece aconselhamento sobre navegação, pesca e mergulho com base nessas condições. Ela retorna alertas e aconselhamento para cada atividade.

### Treinamento do Modelo de Tempestade
A função train_storm_model() na linha 83 é responsável por gerar e treinar um modelo de aprendizado de máquina para prever tempestades. Ela retorna o modelo treinado e sua precisão.

### Treinamento do Modelo de Derramamento de Óleo
A função train_model() na linha 113 é responsável por gerar e treinar um modelo de aprendizado de máquina para prever derramamentos de óleo. Ela retorna o modelo treinado e sua precisão.

### Previsão de Tempestade e Derramamento de Óleo
A parte final do código na linha 151 usa os modelos treinados para fazer previsões com base nos dados climáticos coletados. Ele imprime as previsões de tempestade e derramamento de óleo.

### Contribuições
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Licença
Este projeto está licenciado sob a Licença MIT. Sinta-se à vontade para usar, modificar e distribuir o código conforme necessário.

# Autores
## Grupo GRM solutions
### Integrantes:
- Geronimo Augusto RM- 557170
- Murilo Cordeiro RM- 556727
