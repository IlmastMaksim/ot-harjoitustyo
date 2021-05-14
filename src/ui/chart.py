from dearpygui import core


class PieChart:
    def __init__(self):
        self.data = []
        self.labels = []
        self.plot_label = "##PieChart"
        self.chart = lambda: core.add_pie_series(
            self.plot_label, "PieChart", self.data, self.labels, 0.5, 0.5, 0.4
        )

    def draw_chart(self, data, labels):
        self.data = data
        self.labels = labels
        core.clear_plot(self.plot_label)
        self.chart()

    def generate_chart(self, data, labels):
        if data is not None:
            self.data = data
        if labels is not None:
            self.labels = labels
        core.add_plot(
            self.plot_label,
            no_mouse_pos=True,
            xaxis_no_gridlines=True,
            xaxis_no_tick_marks=True,
            xaxis_no_tick_labels=True,
            yaxis_no_gridlines=True,
            yaxis_no_tick_marks=True,
            yaxis_no_tick_labels=True,
            width=500,
            height=500,
        )

        core.set_plot_xlimits(self.plot_label, 0, 1)
        core.set_plot_ylimits(self.plot_label, 0, 1)
        self.draw_chart(data, labels)


class LineChart:
    def __init__(self):
        self.data = []
        self.labels = []
        self.plot_label = "##LineChart"
        self.chart = lambda: core.add_line_series(
            self.plot_label,
            "LineChart",
            y=self.data,
            x=self.labels,
            weight=2,
            color=[0, 0, 255, 100],
        )

    def draw_chart(self, data, labels):
        self.data = data
        self.labels = labels
        core.clear_plot(self.plot_label)
        self.chart()

    def generate_chart(self, data, labels):
        if data is not None:
            self.data = data
        if labels is not None:
            self.labels = labels

        core.add_plot(self.plot_label, width=500, height=500)
        self.draw_chart(data, labels)


pie_chart = PieChart()
line_chart = LineChart()
