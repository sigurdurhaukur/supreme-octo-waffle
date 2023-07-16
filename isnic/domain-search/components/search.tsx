"use client";

import styles from "./search.module.css";
import { useState } from "react";

export default function Search() {
  const [searchResult, setSearchResult] = useState([]);

  async function handlechange(word: string) {
    console.log(word);

    try {
      const response = await fetch("/api/search", {
        method: "POST",
        body: JSON.stringify({ data: word }),
      });
      const result = await response.json();
      console.log(result);

      if (result.status === 500) return setSearchResult([]);

      if (result.status === 200) return setSearchResult(result.data);
    } catch (error) {
      console.error("Error fetching API:", error);
    }
  }

  return (
    <>
      <div className={styles.searchWrapper}>
        <input
          type="text"
          className={styles.searchBar}
          placeholder="search domain"
          onChange={(e) => handlechange(e.target.value)}
        />
      </div>
      <div className={styles.searchResult}>
        {searchResult &&
          searchResult.map((item, index: number) => (
            <p key={index}>
              {item[0]}.is {item[1]}
            </p>
          ))}
      </div>
    </>
  );
}
