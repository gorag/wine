import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import click
import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_year_declination(year):
    ends_with_five_to_twenty = year % 100 in range(5, 20) and 'лет'
    ends_with_one = 1 == year % 10 and 'год'
    ends_with_two_to_four = year % 10 in (2, 3, 4) and 'года'
    others = 'лет'

    return ends_with_five_to_twenty or\
        ends_with_one or\
        ends_with_two_to_four or\
        others


@click.command()
@click.option('--file', required=True,
              type=click.Path(exists=True),
              default='wine.xlsx',
              help='Path to xlsx data file')
@click.option('--sheet', required=True,
              default='Лист1',
              help='Excel file sheet')

def main(file, sheet):
    foundation_year = 1920
    sort_column = 'Категория'

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    company_years = datetime.date.today().year - foundation_year

    wines = pandas.read_excel(
        file,
        sheet_name=sheet,
        na_values='nan',
        keep_default_na=False).to_dict(orient='records')

    wine_categories = collections.defaultdict(list)

    for wine in wines:
        wine_categories[wine[sort_column]].append(wine)

    wine_categories = collections.OrderedDict(sorted(wine_categories.items()))

    rendered_page = template.render(
        company_years=company_years,
        years_declension=get_year_declination(company_years),
        wine_categories=wine_categories,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
