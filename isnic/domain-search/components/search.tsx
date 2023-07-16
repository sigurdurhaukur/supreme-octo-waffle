"use client";

import styles from "./search.module.css";

export default function Search() {
  function handlechange(value: string) {
    console.log(value);
  }

  return (
    <div className={styles.searchWrapper}>
      <input
        type="text"
        className={styles.searchBar}
        placeholder="search domain"
        onChange={(e) => handlechange(e.target.value)}
      />
    </div>
  );
}
