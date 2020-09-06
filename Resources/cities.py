import pandas as pd

file = "Resources/cities.csv"
cities_df = pd.read_csv(file)
cities_html = cities_df.to_html()
html_file = open('templates/data.html', 'w')
html_file = html_file.write(cities_html)