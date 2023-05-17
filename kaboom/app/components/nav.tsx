"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import styles from "./nav.module.css";

export default function Nav() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  function handleHamburgerClick() {
    if (!isMenuOpen) {
      setIsMenuOpen(true);
      document.body.style.overflow = "hidden";
    } else {
      setIsMenuOpen(false);
      document.body.style.overflow = "auto";
    }
  }

  function closeMenu() {
    if (!isMenuOpen) return;

    setIsMenuOpen(false);
    document.body.style.overflow = "auto";
  }

  return (
    <nav className={isMenuOpen ? styles.nav__active : styles.nav}>
      <div className={styles.logo} onClick={closeMenu}>
        <Link href="/">kaboom</Link>
        <span className={styles.logo__span}>An AI search engine</span>
      </div>
      <div className={styles.nav__links}>
        <Link className={styles.nav__a} href="/solutions" onClick={closeMenu}>
          Solutions
        </Link>
        <Link className={styles.nav__a} href="/products" onClick={closeMenu}>
          Products
        </Link>
        <Link className={styles.nav__a} href="/about" onClick={closeMenu}>
          About Kaboom
        </Link>
      </div>
      <div
        className={styles.hamburger__wrapper}
        onClick={() => handleHamburgerClick()}
      >
        <div className={styles.hamburger}></div>
      </div>
    </nav>
  );
}
