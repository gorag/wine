from http.server import HTTPServer, SimpleHTTPRequestHandler
import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas
from pprint import pprint
import collections


start_date = datetime.date(1920, 1, 1)
file_name = 'wine3.xlsx'
sheet_name = 'Лист1'
sort_column = 'Категория'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')

delta = datetime.date.today().year - start_date.year

wines = pandas.read_excel(
    file_name,
    sheet_name=sheet_name,
    na_values='nan',
    keep_default_na=False).to_dict(orient='records')

wine_categories = collections.defaultdict(list)

for wine in wines:
    wine_categories[wine[sort_column]].append(wine)

wine_categories = collections.OrderedDict(sorted(wine_categories.items()))


def years_declension(age_to): return (
    (age_to % 100 in range(5, 20)) and 'лет' or
    (1 in (age_to, (diglast := age_to % 10))) and 'год' or
    ({age_to, diglast} & {2, 3, 4}) and 'года' or 'лет')


rendered_page = template.render(
    delta_years=delta,
    years_declension=years_declension(delta),
    wine_categories=wine_categories,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
