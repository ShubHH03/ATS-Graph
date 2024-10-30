from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import json
from datetime import datetime

class ImportantExpenses(QMainWindow):
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
        'Creditor Amount': 845000.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'May-2023': {
        'Creditor Amount': 1281500.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 123115.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 153086.00
    },
    'Jun-2023': {
        'Creditor Amount': 189500.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 50000.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 40100.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Jul-2023': {
        'Creditor Amount': 700000.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 19706.40,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Aug-2023': {
        'Creditor Amount': 100000.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 153086.00
    },
    'Sep-2023': {
        'Creditor Amount': 102500.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 103.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 50000.00,
        'Property Tax': 0.00,
        'General Insurance': 9440.00,
        'Life Insurance': 0.00
    },
    'Oct-2023': {
        'Creditor Amount': 355000.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 262910.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Nov-2023': {
        'Creditor Amount': 336161.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 24560.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 153086.00
    },
    'Dec-2023': {
        'Creditor Amount': 350000.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 184.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 0.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 172650.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Jan-2024': {
        'Creditor Amount': 37788.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 16496.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Feb-2024': {
        'Creditor Amount': 0.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 2464.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    },
    'Mar-2024': {
        'Creditor Amount': 0.00,
        'Salaries Paid': 0.00,
        'Probable EMI': 0.00,
        'Investment Details': 0.00,
        'Interest Debit': 0.00,
        'Gold Loan (Only Interest)': 0.00,
        'Rent Paid': 0.00,
        'Travelling Expense': 13553.00,
        'Donation': 0.00,
        'TDS Deducted': 0.00,
        'TDS on Forex': 0.00,
        'Total GST': 0.00,
        'Total Income Tax Paid': 0.00,
        'Property Tax': 0.00,
        'General Insurance': 0.00,
        'Life Insurance': 0.00
    }
}
        
        # Initialize the dashboard with the first month
        self.update_dashboard(self.months[0])
    
    def calculate_month_over_month(self, selected_month):
        try:
            current_index = self.months.index(selected_month)
            if current_index == 0:
                return 0
                
            current_total = sum(self.data[selected_month].values())
            previous_total = sum(self.data[self.months[current_index - 1]].values())
            
            if previous_total == 0:
                return 100
            
            return ((current_total - previous_total) / previous_total) * 100
        except Exception as e:
            print(f"Error calculating MoM change: {e}")
            return 0
    
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
    window = ImportantExpenses()
    window.show()
    sys.exit(app.exec())
