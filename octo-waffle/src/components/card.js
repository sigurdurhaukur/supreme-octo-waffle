export default function Card({ title, certainty }) {
  return (
    <div className="card">
      <h3 className="card__h3">{title}</h3>
      <p>{certainty}</p>
    </div>
  );
}
