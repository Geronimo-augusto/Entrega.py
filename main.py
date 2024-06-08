
import dearpygui.dearpygui as dpg
import engine
# Interface com Dear PyGui
dpg.create_context()
dpg.create_viewport(title='Sistema de Previsão Climática', width=600, height=400)

# Criar temas para os botões
with dpg.theme() as button_theme:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (255, 0, 0, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (200, 0, 0, 255))
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (150, 0, 0, 255))
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
        dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 10, 10)

# Criar tema para o texto
with dpg.theme() as text_theme:
    with dpg.theme_component(dpg.mvText):
        dpg.add_theme_color(dpg.mvThemeCol_Text, (0, 255, 0, 255))


with dpg.window(label="Previsões Climáticas", width=600, height=400):
    dpg.add_text("Clique em um dos botões abaixo para obter a previsão correspondente.")

    #Criaçao e definiçao dos botoes
    button_id1= dpg.add_button(label="Verificar Condição de Pesca", callback=engine.check_fishing_callback)
    button_id2= dpg.add_button(label="Verificar Condição de Mergulho", callback=engine.check_diving_callback)
    button_id3= dpg.add_button(label="Verificar Condição de Navegação", callback=engine.check_navigation_callback)
    button_id4= dpg.add_button(label="Verificar Tempestade", callback=engine.check_storm_callback)
    button_id5= dpg.add_button(label="Verificar Previsão de Derramamento de Óleo", callback=engine.check_oil_spill_callback)
    dpg.add_button(label="Sair", callback=engine.exit_app_callback)

    #estilizaçao dos botoes
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
