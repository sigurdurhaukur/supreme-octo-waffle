import Link from "next/link";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <h2>Search with the Power of AI Technology</h2>
        <h1>The Explosive Way to Find Anything Online</h1>
        <Link className={styles.cta} href="/products">
          start building for free
        </Link>
      </header>
      <section className={styles.section}>
        <h1>Why leaders are choosing Kaboom...</h1>
      </section>
    </main>
  );
}
