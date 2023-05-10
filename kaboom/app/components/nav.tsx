import Link from "next/link";
import "./nav.css";

export default function Nav() {
  return (
    <nav>
      <div className="logo">
        <Link href="/">Kaboom</Link>
      </div>
      <div className="nav__links">
        <Link className="nav__a" href="/solutions">
          Solutions
        </Link>
        <Link className="nav__a" href="/products">
          Products
        </Link>
        <Link className="nav__a" href="/about">
          About Kaboom
        </Link>
      </div>
    </nav>
  );
}
