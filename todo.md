# todo

[] data collection
[] data pipeline
[] add, update, remove a specific column to the csv
[] calculate average vector embedding
[] search
[] display

- build a csv containing the data
  - headers: `average vector embedding` and `sentence`
- read contents of the csv
  - put it into a `Database` object
- search for the closest `average vector embedding` to the query
  - use `Database` object
  - use `average vector embedding` as the key
  - use `sentence` as the value
- display the `sentence` as the results
