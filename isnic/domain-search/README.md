# ISNIC Domain Search

This is a simple domain search tool for the [ISNIC](https://www.isnic.is/en/) domain registry.

it uses word2vec to suggest similar domains based on the input query.


## to run front end

```bash
npm run dev
```

## to run the backend

```bash
uvicorn main:app --reload
```

Then go to [http://localhost:3000](http://localhost:3000).
