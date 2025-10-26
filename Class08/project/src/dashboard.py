import sys, os
from data.data_loader import DataLoader
from ui.layout import DashboardLayout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main():
    df = DataLoader.read_data()
    dashboard = DashboardLayout(df=df)
    dashboard.render()

if __name__ == '__main__':
    main()