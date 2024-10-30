from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import json
from datetime import datetime

class Income(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income Distribution Dashboard")
        self.setGeometry(100, 100, 1200, 900)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create month selector with modern styling
        self.month_selector = QComboBox()
        self.months = ['Apr-2023', 'May-2023', 'Jun-2023', 'Jul-2023', 'Aug-2023', 
                      'Sep-2023', 'Oct-2023', 'Nov-2023', 'Dec-2023', 'Jan-2024', 
                      'Feb-2024', 'Mar-2024']
        self.month_selector.addItems(self.months)
        self.month_selector.currentTextChanged.connect(self.update_dashboard)
        layout.addWidget(self.month_selector)
        
        # Create the web view
        self.web = QWebEngineView()
        layout.addWidget(self.web)
        
        # Prepare the data structure
        self.data = {
            'Apr-2023': {
                'Salary Received': 0.00,
                'Debtors Amount': 331727.00,
                'UPI-Cr': 36349.00,
                'Suspense - Cr': 455000.00
            },
            'May-2023': {
                'Salary Received': 0.00,
                'Debtors Amount': 0.00,
                'UPI-Cr': 411743.73,
                'Loans Received': 10.00,
                'Suspense - Cr': 410000.00,
            },
            'Jun-2023': {
                'Salary Received': 0.00,
                'Debtors Amount': 0.00,
                'Cash Deposits': 250000.00,
                'UPI-Cr': 194500.00
            },
            'Jul-2023': {
                'Debtors Amount': 1088851.68,
                'UPI-Cr': 236800.00,
                'Suspense - Cr': 200000.00
            },
            'Aug-2023': {
                'Debtors Amount': 485000.00,
                'Cash Deposits': 22000.00,
                'UPI-Cr': 198502.00,
                'Suspense - Cr': 685192.90
            },
            'Sep-2023': {
                'Cash Deposits': 240000.00,
                'UPI-Cr': 51130.00
            },
            'Oct-2023': {
                'Debtors Amount': 115000.00,
                'UPI-Cr': 165600.00
            },
            'Nov-2023': {
                'Debtors Amount': 575000.00,
                'UPI-Cr': 276821.00,
                'Suspense - Cr': 545000.00
            },
            'Dec-2023': {
                'Salary Received': 20000.00,
                'Debtors Amount': 41002.00,
                'UPI-Cr': 705500.00,
                'Suspense - Cr': 175000.00
            },
            'Jan-2024': {
                'Debtors Amount': 40000.00,
                'UPI-Cr': 1083001.00,
                'Refund/Reversal': 62.00,
                'Suspense - Cr': 225000.00
            },
            'Feb-2024': {
                'Debtors Amount': 60001.00,
                'UPI-Cr': 78038.00
            },
            'Mar-2024': {
                'Debtors Amount': 347873.00,
                'UPI-Cr': 336066.00,
                'Bounce Transaction': 250118.00,
                'Refund/Reversal': 199.00,
                'Suspense - Cr': 770000.00
            }
        }
        
        # Initialize the dashboard with the first month
        self.update_dashboard(self.months[0])
    
    def get_highest_category(self, selected_month):
        try:
            if not self.data[selected_month]:
                return "No data", 0
            
            max_category = max(self.data[selected_month].items(), key=lambda x: x[1])
            return max_category[0], max_category[1]
        except Exception as e:
            print(f"Error getting highest category: {e}")
            return "Error", 0
    
    def update_dashboard(self, selected_month):
        try:
            # Filter out zero values
            filtered_data = {k: v for k, v in self.data[selected_month].items() if v > 0}
            
            # Calculate metrics
            total_income = sum(filtered_data.values())
            # mom_change = self.calculate_month_over_month(selected_month)
            top_category, top_amount = self.get_highest_category(selected_month)
            
            # Create HTML content with modern dashboard design
            html_content = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Income Distribution Dashboard</title>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.7.0/chart.min.js"></script>
                <style>
                    * {{
                        margin: 0;
                        padding: 0;
                        box-sizing: border-box;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    }}
                    
                    body {{
                        background-color: #f0f2f5;
                        padding: 20px;
                    }}
                    
                    .dashboard {{
                        max-width: 1200px;
                        margin: 0 auto;
                    }}
                    
                    .header {{
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        margin-bottom: 20px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }}
                    
                    .metrics-grid {{
                        display: grid;
                        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                        gap: 20px;
                        margin-bottom: 20px;
                    }}
                    
                    .metric-card {{
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                    }}
                    
                    .metric-title {{
                        color: #666;
                        font-size: 0.9em;
                        margin-bottom: 8px;
                    }}
                    
                    .metric-value {{
                        font-size: 1.5em;
                        font-weight: bold;
                        color: #333;
                    }}
                    
                    .chart-container {{
                        background: white;
                        padding: 20px;
                        border-radius: 10px;
                        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                        height: 500px;
                    }}
                    
                    .trend-positive {{
                        color: #10B981;
                    }}
                    
                    .trend-negative {{
                        color: #EF4444;
                    }}
                </style>
            </head>
            <body>
                <div class="dashboard">
                    <div class="header">
                        <h1>Income Distribution for {selected_month}</h1>
                    </div>
                    
                    <div class="metrics-grid">
                        <div class="metric-card">
                            <div class="metric-title">Total Income</div>
                            <div class="metric-value">₹{total_income:,.2f}</div>
                        </div>
                        
                        
                        
                        <div class="metric-card">
                            <div class="metric-title">Top Income Category</div>
                            <div class="metric-value">{top_category}</div>
                            <div>₹{top_amount:,.2f}</div>
                        </div>
                    </div>
                    
                    <div class="chart-container">
                        <canvas id="pieChart"></canvas>
                    </div>
                </div>
                
                <script>
                    const data = {json.dumps(filtered_data)};
                    
                    const ctx = document.getElementById('pieChart').getContext('2d');
                    new Chart(ctx, {{
                        type: 'pie',
                        data: {{
                            labels: Object.keys(data),
                            datasets: [{{
                                data: Object.values(data),
                                backgroundColor: [
                                    '#10B981', '#3B82F6', '#F59E0B', 
                                    '#EC4899', '#8B5CF6', '#6366F1'
                                ],
                                borderWidth: 2,
                                borderColor: '#ffffff'
                            }}]
                        }},
                        options: {{
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {{
                                legend: {{
                                    position: 'right',
                                    labels: {{
                                        padding: 20,
                                        font: {{
                                            size: 12,
                                            family: "'Segoe UI', sans-serif"
                                        }}
                                    }}
                                }},
                                tooltip: {{
                                    callbacks: {{
                                        label: function(context) {{
                                            const label = context.label || '';
                                            const value = context.raw;
                                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                            const percentage = ((value / total) * 100).toFixed(1);
                                            return label + ': ₹' + value.toLocaleString() + ' (' + percentage + '%)';
                                        }}
                                    }}
                                }}
                            }},
                            layout: {{
                                padding: 20
                            }}
                        }}
                    }});
                </script>
            </body>
            </html>
            '''
            
            self.web.setHtml(html_content)
        except Exception as e:
            print(f"Error updating dashboard: {e}")
            # Show error message in web view
            error_html = f'''
            <!DOCTYPE html>
            <html>
            <body>
                <h1>Error updating dashboard</h1>
                <p>{str(e)}</p>
            </body>
            </html>
            '''
            self.web.setHtml(error_html)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Income()
    window.show()
    sys.exit(app.exec())