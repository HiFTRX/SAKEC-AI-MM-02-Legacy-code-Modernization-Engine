export default function CodeBlock({ title, code }) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <h3>{title}</h3>
      <pre
        style={{
          background: "#0d1117",
          color: "#00ff9c",
          padding: "15px",
          borderRadius: "8px",
          overflowX: "auto",
        }}
      >
        <code>{code}</code>
      </pre>
    </div>
  );
}