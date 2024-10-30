import sys
import json
import tempfile
import plotly.graph_objs as go
from PyQt6.QtCore import QDateTime, Qt, QUrl
from PyQt6.QtGui import QPainter
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QScrollArea)
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt6.QtWebEngineWidgets import QWebEngineView

from transactions import BankTransactionDashboard
from Creditors import TransactionChart
from EOD_balance import EODBalanceChart
from Debtors import DebtorsChart
from Cash_withdrawal import StackedBarChart
from Cash_Deposit import CashDeposit
from Payment_Voucher import PaymentDashboard

class CombinedFinancialView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combined Visualization Overview")
        self.setGeometry(100, 100, 1200, 800)
        
        # Create scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.setCentralWidget(scroll_area)
        
        # Main widget and layout
        main_widget = QWidget()
        scroll_area.setWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        title_bank_txn = QLabel("Bank Transaction Analysis")
        title_bank_txn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_bank_txn.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title_bank_txn)
        bank_txn_dashboard = BankTransactionDashboard()
        bank_txn_dashboard.setFixedHeight(700)
        layout.addWidget(bank_txn_dashboard)


        title_eod = QLabel("EOD Balance Visualization")
        title_eod.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_eod.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title_eod)
        eod_view = EODBalanceChart()
        eod_view.setFixedHeight(700)
        layout.addWidget(eod_view)

        
        title1 = QLabel("Transaction History (Creditors)")
        title1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title1.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title1)
        txn_history_chart = TransactionChart()
        txn_history_chart.setFixedHeight(700)
        layout.addWidget(txn_history_chart)
        

        title2 = QLabel("Financial Transactions (Debtors)")
        title2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title2.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title2)
        fin_txn_chart = DebtorsChart()
        fin_txn_chart.setFixedHeight(700)
        layout.addWidget(fin_txn_chart)

        
        title3 = QLabel("Cash Withdrawal Analysis")
        title3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title3.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title3)
        cash_withdrawal = StackedBarChart()
        cash_withdrawal.setFixedHeight(700)
        layout.addWidget(cash_withdrawal)

        title4 = QLabel("Cash Deposit Analysis")
        title4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title4.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title4)
        cash_deposit = CashDeposit()
        cash_deposit.setFixedHeight(700)
        layout.addWidget(cash_deposit)
    
        

        title6 = QLabel("Payment Voucher Analysis")
        title6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title6.setStyleSheet("QLabel { font-size: 16pt; font-weight: bold; margin: 10px; }")
        layout.addWidget(title6)
        payment_voucher = PaymentDashboard()
        payment_voucher.setFixedHeight(700)
        layout.addWidget(payment_voucher)

        
        # Add spacing between charts
        layout.setSpacing(40)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CombinedFinancialView()
    window.show()
    sys.exit(app.exec())
