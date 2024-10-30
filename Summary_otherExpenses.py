from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
from PyQt6.QtGui import QFont
import json
from datetime import datetime

class OtherExpenses(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Income Distribution Dashboard")
        self.setGeometry(100, 100, 1200, 900)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # Create horizontal layout for the top section
        top_layout = QHBoxLayout()
        
        # Create month selector with modern styling
        self.month_selector = QComboBox()
        self.months = ['Apr-2023', 'May-2023', 'Jun-2023', 'Jul-2023', 'Aug-2023', 
                      'Sep-2023', 'Oct-2023', 'Nov-2023', 'Dec-2023', 'Jan-2024', 
                      'Feb-2024', 'Mar-2024']
        self.month_selector.addItems(self.months)
        self.month_selector.currentTextChanged.connect(self.update_dashboard)
        
        # Style the combo box
        self.month_selector.setFixedWidth(150)  # Set fixed width
        self.month_selector.setFont(QFont("Segoe UI", 10))  # Set font
        self.month_selector.setStyleSheet("""
            QComboBox {
                padding: 6px 12px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
                min-height: 30px;
            }
            
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #666;
                margin-right: 8px;
            }
            
            QComboBox:hover {
                border-color: #999;
            }
            
            QComboBox:focus {
                border-color: #0066cc;
                outline: none;
            }
            
            QComboBox::drop-down:hover {
                background-color: #f0f0f0;
            }
        """)
        
        # Add stretch to push combo box to the right
        top_layout.addStretch()
        top_layout.addWidget(self.month_selector)
        
        # Add layouts to main layout
        main_layout.addLayout(top_layout)
        
        # Create the web view
        self.web = QWebEngineView()
        main_layout.addWidget(self.web)
        # Prepare the data structure
        self.data = {
    'Apr-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 6.72,
        'Other Expenses': 0.00,
        'Utility Bills': 588.82,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 31024.78,
        'POS Txns - Dr': 283.00,
        'UPI-Dr': 13197.00,
        'Loan Given': 500000.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 216242.00,
        'Total Debit': 761342.32
    },
    'May-2023': {
        'Credit Card Payment': 30114.00,
        'Forex Charges': 0.00,
        'Bank Charges': 21.39,
        'Other Expenses': 0.00,
        'Utility Bills': 4245.64,
        'Subscription / Entertainment': 2000.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 10000.00,
        'POS Txns - Dr': 0.00,
        'UPI-Dr': 59843.40,
        'Loan Given': 46000.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 40933.00,
        'Total Debit': 193157.43
    },
    'Jun-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 45.42,
        'Other Expenses': 0.00,
        'Utility Bills': 588.82,
        'Subscription / Entertainment': 5605.72,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 10000.00,
        'POS Txns - Dr': 4533.00,
        'UPI-Dr': 11094.00,
        'Loan Given': 0.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 48030.32,
        'Total Debit': 79897.28
    },
    'Jul-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 41.76,
        'Other Expenses': 0.00,
        'Utility Bills': 1829.44,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 3211.00,
        'UPI-Dr': 12493.00,
        'Loan Given': 0.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 191094.00,
        'Total Debit': 208669.20
    },
    'Aug-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 80.82,
        'Other Expenses': 0.00,
        'Utility Bills': 1395.79,
        'Subscription / Entertainment': 1458.64,
        'Food Expenses': 330.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 490.00,
        'UPI-Dr': 25180.00,
        'Loan Given': 1010000.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 111523.90,
        'Total Debit': 1150459.15
    },
    'Sep-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 47.20,
        'Other Expenses': 0.00,
        'Utility Bills': 3119.72,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 299.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 3935.00,
        'UPI-Dr': 28361.46,
        'Loan Given': 0.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 110489.00,
        'Total Debit': 146251.38
    },
    'Oct-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 17.70,
        'Other Expenses': 0.00,
        'Utility Bills': 0.00,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 2834.00,
        'UPI-Dr': 19967.00,
        'Loan Given': 0.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 122961.00,
        'Total Debit': 145779.70
    },
    'Nov-2023': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 23.60,
        'Other Expenses': 0.00,
        'Utility Bills': 0.00,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 10915.00,
        'UPI-Dr': 31815.14,
        'Loan Given': 71834.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 33886.00,
        'Total Debit': 148473.74
    },
    'Dec-2023': {
        'Credit Card Payment': 10995.00,
        'Forex Charges': 0.00,
        'Bank Charges': 27.72,
        'Other Expenses': 0.00,
        'Utility Bills': 0.00,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 642.00,
        'Withdrawal': 10000.00,
        'POS Txns - Dr': 0.00,
        'UPI-Dr': 67035.11,
        'Loan Given': 71834.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 56505.00,
        'Total Debit': 217038.83
    },
    'Jan-2024': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 47.78,
        'Other Expenses': 0.00,
        'Utility Bills': 1428.98,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 481.01,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 0.00,
        'UPI-Dr': 87393.30,
        'Loan Given': 71834.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 397717.00,
        'Total Debit': 558902.07
    },
    'Feb-2024': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 39.80,
        'Other Expenses': 0.00,
        'Utility Bills': 1350.10,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 2834.00,
        'UPI-Dr': 40000.00,
        'Loan Given': 71834.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 186486.00,
        'Total Debit': 302543.90
    },
    'Mar-2024': {
        'Credit Card Payment': 0.00,
        'Forex Charges': 0.00,
        'Bank Charges': 16.10,
        'Other Expenses': 0.00,
        'Utility Bills': 3156.96,
        'Subscription / Entertainment': 0.00,
        'Food Expenses': 0.00,
        'Online Shopping': 0.00,
        'Withdrawal': 0.00,
        'POS Txns - Dr': 0.00,
        'UPI-Dr': 40000.00,
        'Loan Given': 0.00,
        'Cheque Paid': 0.00,
        'Departmental Store': 0.00,
        'Payment to Self': 0.00,
        'Suspense - Dr': 32089.00,
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
                                    '#10B981', '#3B82F6', '#F59E0B', '#EC4899', '#8B5CF6', '#6366F1',
                                    '#EF4444', '#F97316', '#22C55E', '#0EA5E9', '#A855F7', '#D946EF',
                                    '#14B8A6', '#F43F5E', '#EAB308', '#34D399', '#60A5FA', '#A3E635',
                                    '#D97706', '#9333EA', '#F87171', '#4ADE80', '#FACC15', '#7C3AED'
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
    window = OtherExpenses()
    window.show()
    sys.exit(app.exec())