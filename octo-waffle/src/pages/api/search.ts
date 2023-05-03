// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
import type { NextApiRequest, NextApiResponse } from "next";
import weaviate, { WeaviateClient } from "weaviate-ts-client";
// const w2v = require("word2vec");
import path from "path";

const filePath = path.join(process.cwd(), "word2vec.kv");

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  //   w2v.loadModel(filePath, (error: any, model: any) => {
  //     if (error) {
  //       console.error(error);
  //       return res.status(500).json({ name: "Failed to load model" });
  //     }
  //     console.log(model);
  //     let wordVecs = model.getVectors(["Hamlet", "daughter"]);
  res.status(200).json({ name: "mamma thin" });
  //   });
}

// const client: WeaviateClient = weaviate.client({
//   scheme: "http",
//   host: "localhost:8080",
// });

// client.schema
//   .getter()
//   .do()
//   .then((res: any) => {
//     console.log(res);
//   })
//   .catch((err: Error) => {
//     console.error(err);
//   });

// client.graphql
//     .get()
//     .withNearVector({
//         "vector": custom_embedding,
//          "certainty": 0.7
//     })
//     .withLimit(2)
//     .do()
