import dearpygui.dearpygui as dpg

xaxis = dpg.generate_uuid()
yaxis = dpg.generate_uuid()
group = dpg.generate_uuid()
window = dpg.generate_uuid()


def initialize_window():
    with dpg.window(label="Window", width=400, height=400, id=window):
        with dpg.group(horizontal=True):
            dpg.add_button(label="fit y", callback=lambda:dpg.fit_axis_data(yaxis))
            dpg.add_button(label="fit x", callback=lambda:dpg.fit_axis_data(xaxis))

        initialize_widget()


def initialize_widget():
    with dpg.plot(label="Canvas", height=-1, width=-1):
        dpg.add_plot_legend()

        dpg.add_plot_axis(dpg.mvXAxis, label="X", id=xaxis)
        dpg.set_axis_limits(xaxis, 0, 1)

        dpg.add_plot_axis(dpg.mvYAxis, label="Score", id=yaxis)
        dpg.set_axis_limits(yaxis, 0, 1)


def update_widget():
    pass

if __name__ == "__main__":
    initialize_window()

    dpg.start_dearpygui()