import dearpygui.dearpygui as dpg

with dpg.window(label="Tutorial", width=400, height=400):

    with dpg.plot(label="Drag Lines/Points", height=-1, width=-1):
        dpg.add_plot_legend()
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.set_axis_limits(dpg.last_item(), -5, 5)
        dpg.add_plot_axis(dpg.mvYAxis, label="y")
        dpg.set_axis_limits(dpg.last_item(), -5, 5)

        # drag lines/points belong to the plot NOT axis
        dpg.add_drag_line(label="dline1", color=[255, 0, 0, 255], default_value=2.0)
        dpg.add_drag_line(label="dline2", color=[255, 255, 0, 255], vertical=False, default_value=-2)
        dpg.add_drag_point(label="dpoint1", color=[255, 0, 255, 255], default_value=(1.0, 1.0))
        dpg.add_drag_point(label="dpoint2", color=[255, 0, 255, 255], default_value=(-1.0, 1.0))

dpg.start_dearpygui()
