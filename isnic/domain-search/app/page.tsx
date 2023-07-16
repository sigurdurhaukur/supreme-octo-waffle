import styles from "./page.module.css";
import Search from "../components/search";

export default function Home() {
  return (
    <main className={styles.main}>
      <h1 className={styles.title}>ISNIC Semantic Domain Search (Prototype)</h1>

      <Search />
    </main>
  );
}
