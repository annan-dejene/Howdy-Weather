import pandas as pd


file_name = "country_codes.csv"

def load_country(country_name):
  df = pd.read_csv(file_name)
  codes = [code.strip().replace('"', '') for code in df['Alpha-2 code']]
           
  countries = list(df['Country'])

  country_dict = dict(zip(codes, countries))

  return country_dict[country_name]


