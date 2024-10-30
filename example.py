import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QTimer
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Web Visualization")
        self.setGeometry(100, 100, 1000, 800)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create QWebEngineView
        self.web_view = QWebEngineView()
        
        # HTML content with Chart.js
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Interactive Dashboard</title>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    background-color: #f5f5f5;
                }
                .chart-container {
                    background-color: white;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    margin-bottom: 20px;
                }
                .dashboard-title {
                    text-align: center;
                    color: #333;
                    margin-bottom: 20px;
                }
                .chart-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 20px;
                }
            </style>
        </head>
        <body>
            <h1 class="dashboard-title">Interactive Dashboard</h1>
            <div class="chart-grid">
                <div class="chart-container">
                    <canvas id="lineChart"></canvas>
                </div>
                <div class="chart-container">
                    <canvas id="barChart"></canvas>
                </div>
            </div>

            <script>
                // Line Chart
                var lineCtx = document.getElementById('lineChart').getContext('2d');
                var lineChart = new Chart(lineCtx, {
                    type: 'line',
                    data: {
                        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                        datasets: [{
                            label: 'Sales',
                            data: [12, 19, 3, 5, 2, 3],
                            borderColor: 'rgb(75, 192, 192)',
                            tension: 0.1
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Monthly Sales'
                            }
                        }
                    }
                });

                // Bar Chart
                var barCtx = document.getElementById('barChart').getContext('2d');
                var barChart = new Chart(barCtx, {
                    type: 'bar',
                    data: {
                        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                        datasets: [{
                            label: 'Product Categories',
                            data: [12, 19, 3, 5, 2, 3],
                            backgroundColor: [
                                'rgba(255, 99, 132, 0.5)',
                                'rgba(54, 162, 235, 0.5)',
                                'rgba(255, 206, 86, 0.5)',
                                'rgba(75, 192, 192, 0.5)',
                                'rgba(153, 102, 255, 0.5)',
                                'rgba(255, 159, 64, 0.5)'
                            ]
                        }]
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            title: {
                                display: true,
                                text: 'Product Distribution'
                            }
                        }
                    }
                });

                // Function to update chart data (called from Python)
                function updateChartData(chartId, newData) {
                    const chart = Chart.getChart(chartId);
                    if (chart) {
                        chart.data.datasets[0].data = newData;
                        chart.update();
                    }
                }
            </script>
        </body>
        </html>
        """

        # Set HTML content
        self.web_view.setHtml(html_content)

        # Create update button
        update_button = QPushButton("Update Charts")
        update_button.clicked.connect(self.update_charts)

        # Add widgets to layout
        layout.addWidget(self.web_view)
        layout.addWidget(update_button)

        # Setup timer for real-time updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_charts)
        self.timer.start(5000)  # Update every 5 seconds

    def update_charts(self):
        # Generate random data
        import random
        new_line_data = [random.randint(1, 20) for _ in range(6)]
        new_bar_data = [random.randint(1, 20) for _ in range(6)]

        # Update line chart
        self.web_view.page().runJavaScript(
            f"updateChartData('lineChart', {json.dumps(new_line_data)})")
        
        # Update bar chart
        self.web_view.page().runJavaScript(
            f"updateChartData('barChart', {json.dumps(new_bar_data)})")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())