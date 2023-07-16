import { NextResponse, NextRequest } from "next/server";

export async function POST(req: NextRequest, res: NextResponse) {
  let { data: searchQuery } = await req.json();

  //   remove .is from search query
  searchQuery = searchQuery.replace(".is", "");

  console.log(searchQuery);

  if (!searchQuery || searchQuery == "")
    return NextResponse.json({ data: [], status: 500 });

  try {
    const response = await fetch(`http://localhost:8000/search/${searchQuery}`);
    const result = await response.json();
    return NextResponse.json({ data: result, status: 200 });
  } catch (error) {
    console.error("Error fetching API:", error);
    return NextResponse.json({ data: [], status: 500 });
  }
}
