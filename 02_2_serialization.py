"""Napisz funkcję, która zamieni format CSV na JSON. Np.:

Dane w CSV:

csv_data = "album, year, US_peak_chart_post
The White Stripes, 1999, -
De Stijl, 2000, -
White Blood Cells, 2001, 61
Elephant, 2003, 6
Get Behind Me Satan, 2005, 3
Icky Thump, 2007, 2
Under Great White Northern Lights, 2010, 11
Live in Mississippi, 2011, -
Live at the Gold Dollar, 2012, -
Nine Miles from the White City, 2013, -"

Wynikowe dane w JSON:

[
  {
    "album": "The White Stripes",
    "year": 1999,
    "US_peak_chart_post": "-"
  },
  {
    "album": "De Stijl",
    "year": 2000,
    "US_peak_chart_post": "-"
  },
  {
    "album": "White Blood Cells",
    "year": 2001,
    "US_peak_chart_post": 61
  },
  {
    "album": "Elephant",
    "year": 2003,
    "US_peak_chart_post": 6
  },
  {
    "album": "Get Behind Me Satan",
    "year": 2005,
    "US_peak_chart_post": 3
  },
  {
    "album": "Icky Thump",
    "year": 2007,
    "US_peak_chart_post": 2
  },
  {
    "album": "Under Great White Northern Lights",
    "year": 2010,
    "US_peak_chart_post": 11
  },
  {
    "album": "Live in Mississippi",
    "year": 2011,
    "US_peak_chart_post": "-"
  },
  {
    "album": "Live at the Gold Dollar",
    "year": 2012,
    "US_peak_chart_post": "-"
  },
  {
    "album": "Nine Miles from the White City",
    "year": 2013,
    "US_peak_chart_post": "-"
  }
]
Zauważ, że dane wynikowe są sformatowane tak, że pierwsza linijka CSV to nazwy pól. Zauważ, że wynikowy JSON liczby ma
zapisane we właściwym typie."""
# import json
from json import dumps, dump


def convert_to_json(csv):
    data_per_line = csv.split('\n')
    fields = data_per_line[0].split(',')
    data = data_per_line[1:]

    result_json = []

    def _ensure_proper_type(value: str):
        return int(value) if value.isdigit() else value

    for row in data:
        sub_result = {}
        cells = row.split(',')
        for cell, field in zip(cells, fields):
            sub_result[field.strip()] = _ensure_proper_type(cell.strip())
        result_json.append(sub_result)

    return dumps(result_json, indent=4)


if __name__ == '__main__':
    with open('data.csv', 'r') as f:
        csv_data = ''
        for line in f:
            csv_data += line
    with open('data.json', 'w') as out_file:
        json_data = convert_to_json(csv_data)
        dump(json_data, out_file, indent=2)
        print(json_data)
