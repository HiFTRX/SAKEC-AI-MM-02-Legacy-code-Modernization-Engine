export default function MetricsPanel({ summary }) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <h3>📊 Metrics</h3>
      <p>Input Size: {summary.total_input_size}</p>
      <p>Optimized Size: {summary.optimized_size}</p>
      <p>Reduction: {summary.reduction_percent}%</p>
    </div>
  );
}