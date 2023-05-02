// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import weaviate, { WeaviateClient } from "weaviate-ts-client";

const client: WeaviateClient = weaviate.client({
  scheme: "http",
  host: "localhost:8080",
});

client.schema
  .getter()
  .do()
  .then((res: any) => {
    console.log(res);
  })
  .catch((err: Error) => {
    console.error(err);
  });

type Data = {
  name: string;
};

// client.graphql
//     .get()
//     .withNearVector({
//         "vector": custom_embedding,
//          "certainty": 0.7
//     })
//     .withLimit(2)
//     .do()

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  res.status(200).json({ name: "John Doe" });
}
