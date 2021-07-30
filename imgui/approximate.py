import dearpygui.dearpygui as dpg

xaxis = dpg.generate_uuid()
yaxis = dpg.generate_uuid()
plot = dpg.generate_uuid()
window = dpg.generate_uuid()
canvas_group = dpg.generate_uuid()

plot_data = [0, 1]
points = []



def initialize_window():
    with dpg.window(label="Window", width=400, height=400, id=window):
        with dpg.group(horizontal=True, id=canvas_group):
            dpg.add_button(label="Fit X", callback=lambda:dpg.fit_axis_data(xaxis))
            dpg.add_button(label="Fit Y", callback=lambda:dpg.fit_axis_data(yaxis))

            # dpg.add_button(label="Lock Limits", callback=lambda:dpg.set_axis_limits(xaxis, -0.1, 1.1))
            # dpg.add_button(label="Unlock Limits", callback=lambda:dpg.set_axis_limits_auto(xaxis))

        initialize_widget()


def revert_scaling_plot(sender, axis):
    dpg.set_axis_limits_auto(xaxis)
    dpg.set_axis_limits_auto(yaxis)


def initialize_widget():
    with dpg.plot(label="Canvas", height=-1, width=-1, id=plot):
        dpg.add_plot_legend()

        dpg.add_plot_axis(dpg.mvXAxis, label="X", id=xaxis)
        dpg.set_axis_limits(xaxis, -0.1, 1.1)

        dpg.add_plot_axis(dpg.mvYAxis, label="Y", id=yaxis)
        dpg.set_axis_limits(yaxis, -0.1, 1.1)

        with dpg.handler_registry():
            dpg.add_mouse_double_click_handler(
                button=0,
                callback=add_point,
                user_data=(plot, plot_data),
            )


def add_point(sender, app_data, user_data):
    plot, data, = user_data
    plot_mouse_position = dpg.get_plot_mouse_pos()

    def point_in_rectangle(point):
        x_in = 0 < point[0] < 1
        y_in = 0 < point[1] < 1
        return x_in & y_in

    if point_in_rectangle(plot_mouse_position):
        point_index = dpg.add_drag_point(
            label="dpoint1",
            color=[255, 0, 255, 255],
            default_value=dpg.get_plot_mouse_pos(),
            parent=plot
        )


def remove_point(sender, app_data, user_data):
    dpg.delete_item()


def update_plot_data(sender, app_data, user_data):
    plot, data, mouse_pos = user_data
    dpg.set_value(plot, plot_data)


if __name__ == "__main__":
    initialize_window()

    dpg.start_dearpygui()