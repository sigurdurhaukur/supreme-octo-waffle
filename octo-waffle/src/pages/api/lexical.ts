// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import weaviate, { WeaviateClient } from "weaviate-ts-client";

const client: WeaviateClient = weaviate.client({
  scheme: "http",
  host: "localhost:8080",
});

type Data = {
  title: string;
  _additional: { certainty: number };
  summary: string;
};

export default function handler(
  req: NextApiRequest & { query: { query: string } },
  res: NextApiResponse<Data>
) {
  const query = req.query.query;
  client.graphql
    .get()
    .withClassName("Articles")
    .withFields("text url summary _additional{certainty}")
    .withWhere({
      path: ["summary"],
      operator: "Equal",
      valueText: query,
    })
    .withLimit(10)
    .do()
    .then((result: any) => {
      console.log(result);
      for (const item of result.data.Get.Articles) {
        console.log(item);
      }
      res.status(200).json(result.data.Get.Articles);
    })
    .catch((err) => {
      console.log(err);
      res.status(200).json([]);
    });
}

// client.schema
//   .getter()
//   .do()
//   .then((res: any) => {
//     console.log(res);
//   })
//   .catch((err: Error) => {
//     console.error(err);
//   });
