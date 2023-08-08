export default function Card({ title, certainty, summary }) {
  return (
    <div className="card">
      <h3 className="card__h3">{title}</h3>
      {certainty && <p>skyldleiki: {certainty}</p>}
      {summary && <p>{summary.slice(0, 300)}...</p>}
    </div>
  );
}
