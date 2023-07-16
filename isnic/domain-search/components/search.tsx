"use client";

import styles from "./search.module.css";
import { useState } from "react";

function SearchResults({ searchResult }) {
  return (
    <>
      {searchResult &&
        searchResult.map(({ word, similarity }, index: number) => (
          <p key={index}>
            <span className={styles.domain}>{word}.is</span>
            <span className={styles.distance}>
              {(similarity * 100).toString().substring(0, 4)}%
            </span>
          </p>
        ))}
    </>
  );
}

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
        <h2>Search Results:</h2>
        <SearchResults searchResult={searchResult} />
      </div>
    </>
  );
}
