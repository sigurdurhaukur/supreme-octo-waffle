// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import weaviate, { WeaviateClient } from "weaviate-ts-client";

const client: WeaviateClient = weaviate.client({
  scheme: "http",
  host: "localhost:8080",
});

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest & { query: { query: string } },
  res: NextApiResponse<Data>
) {
  const query = req.query.query;
  console.log(query);
  client.graphql
    .get()
    .withClassName("News")
    .withFields("text _additional{certainty distance}")
    .withNearText({
      concepts: [query],
      certainty: 0.7,
    })
    .withLimit(2)
    .do()
    .then((result: any) => {
      console.log(result);
      for (const item of result.data.Get.News) {
        console.log(item);
      }
      res.status(200).json(result.data.Get.News);
    })
    .catch(console.error);
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
