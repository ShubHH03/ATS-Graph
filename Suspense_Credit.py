import plotly.express as px
import pandas as pd

# Example data
data = {
    "Value Date": ["12-04-2023", "25-04-2023", "25-04-2023", "27-04-2023", "20-05-2023", "14-07-2023", "07-08-2023", 
                   "11-08-2023", "19-08-2023", "18-11-2023", "21-11-2023", "15-12-2023", "15-12-2023", "18-12-2023", 
                   "17-01-2024", "13-03-2024", "14-03-2024", "14-03-2024", "18-03-2024", "25-03-2024"],
    "Description": ["clg/chandrakantlaxman", "clg/pradeepssharma", "clg/naishadhjdalal", "clg/antketdeelip", "clg/rgsynthetics",
                    "clg/mohiniikapoor", "acxfrfromgl05051to05066", "clg/rgsynthetics", "clg/babunidoni", "clg/neerajmishra",
                    "clg/pranitaparagraut", "clg/savitameshr", "clg/vijayvitthalrao", "trfrfrom:sunilmarutishelke", 
                    "clg/vijaykarkhile", "clg/shivdastrbak", "clg/jitendrabubhai", "clg/apexakumarinatvarlal", 
                    "clg/kbgeneral", "clg/madhusudan"],
    "Credit": [25000, 325000, 55000, 50000, 410000, 200000, 5192.90, 180000, 500000, 450000, 95000, 100000, 50000, 25000, 
               225000, 300000, 100000, 100000, 20000, 250000]
}

df = pd.DataFrame(data)

# Create a bar chart with color gradients
fig = px.bar(df, x='Description', y='Credit', color='Credit',
             color_continuous_scale='Viridis', title='Credit Transactions')

# Update layout for better readability
fig.update_layout(xaxis_title="Description", yaxis_title="Credit Amount (₹)", 
                  xaxis_tickangle=45, template="plotly_white")

# Show the figure
fig.show()
