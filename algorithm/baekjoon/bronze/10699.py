from datetime import datetime

def solve():
    today = datetime.now()

    formatted_date = today.strftime("%Y-%m-%d")

    print(formatted_date)

if __name__ == "__main__":
    solve()