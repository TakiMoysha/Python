import dearpygui.dearpygui as dpg
from math import sin

plot = dpg.generate_uuid()

def update_plot_data(sender, app_data, user_data):
    plot, data, mouse_pos = user_data
    print("sender: ", sender)
    print("app_data: ", app_data)
    print("user_data: ", user_data)
    print("mouse_pos: ", dpg.get_plot_mouse_pos())
    # mouse_y = app_data[1]
    # plot = user_data[0]
    # plot_data = user_data[1]
    # if len(plot_data) > 100:
    #     plot_data.pop(0)
    # plot_data.append(sin(mouse_y/30))
    # dpg.set_value(plot, plo_datta)

data=[]
with dpg.window(label="Tutorial", width=500, height=500):
    with dpg.plot(label="Canvas", height=-1, width=-1, id=plot):
        with dpg.handler_registry():
            dpg.add_mouse_click_handler(
                button=0,
                callback=update_plot_data,
                user_data=(plot, data, dpg.get_plot_mouse_pos())
            )

dpg.start_dearpygui()