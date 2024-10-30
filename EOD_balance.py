import sys
import plotly.graph_objs as go
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import tempfile

class EODBalanceChart(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EOD Balance Visualization")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Web view to display the chart
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Show the chart when the window loads
        self.display_chart()

    def display_chart(self):
        data = {
            "Day": [1, 2, 3, 4, 5],
            "Apr-2023": [1373694.32, 1351195.32, 1351870.32, 651870.32, 306870.32],
            "May-2023": [843219.00, 851219.00, 846973.36, 826873.36, 903740.36],
            "Jun-2023": [293265.30, 284265.30, 254686.88, 254686.88, 254686.88],
        }

        # Create the stacked bar chart using Plotly
        fig = go.Figure()
        fig.add_trace(go.Bar(x=data["Day"], y=data["Apr-2023"], name='Apr-2023'))
        fig.add_trace(go.Bar(x=data["Day"], y=data["May-2023"], name='May-2023'))
        fig.add_trace(go.Bar(x=data["Day"], y=data["Jun-2023"], name='Jun-2023'))

        # Set up layout for the chart
        fig.update_layout(
            title="Monthly Data Visualization",
            xaxis_title="Days",
            yaxis_title="Values",
            barmode='stack',
            legend_title="Months",
        )

        # Save the plotly chart as an HTML file and display it in QWebEngineView
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
            fig.write_html(f.name)
            self.web_view.setUrl(QUrl.fromLocalFile(f.name))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = EODBalanceChart()
    mainWin.show()
    sys.exit(app.exec())
