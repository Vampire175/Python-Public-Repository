import yfinance as yf
print('Welcome to Sales Seeker\nNotice-Shows sales of companies that are listed in NSE India')
a=input('Enter Company Name- ')
company = yf.Ticker(f"{a}.NS")  # NSE-listed company (use '.NS' suffix for NSE)

# Get income statement (includes revenue)
financials = company.financials
print(financials.loc['Total Revenue'])
print('Thanks for using made by Vampire in India with ❤️')
input('Press Enter key to exit')