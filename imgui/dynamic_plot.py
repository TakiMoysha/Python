import dearpygui.dearpygui as dpg
from math import sin

def update_plot_data(sender, app_data, user_data):
    mouse_y = app_data[1]
    plot = user_data[0]
    plot_data = user_data[1]
    if len(plot_data) > 100:
        plot_data.pop(0)
    plot_data.append(sin(mouse_y/30))
    dpg.set_value(plot, plot_data)

data=[]
with dpg.window(label="Tutorial", width=500, height=500):
    plot = dpg.add_simple_plot(min_scale =-1.0, max_scale =1.0, height=300)

with dpg.handler_registry():
    dpg.add_mouse_move_handler(callback=update_plot_data, user_data=(plot, data))

dpg.start_dearpygui()