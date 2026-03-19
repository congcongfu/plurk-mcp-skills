import pandas as pd
import sys
import os

def get_role_info():
    # Absolute path to the file as discussed
    file_path = "/Users/fucong/.openclaw/workspace/laike男性角色表.xlsx"
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        sys.exit(1)
    
    try:
        df = pd.read_excel(file_path)
        # Assuming the first column is the character name and others are details
        # Let's print the whole dataframe as string so the agent can parse it
        print(df.to_string())
    except Exception as e:
        print(f"Error reading Excel: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_role_info()
