import { useState } from "react";
import FileUploader from "../components/FileUploader";
import CodeBlock from "../components/CodeBlock";
import MetricsPanel from "../components/MetricsPanel";

export default function Analyzer() {
  const [result, setResult] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Legacy Code Modernization Engine</h1>

      <FileUploader setResult={setResult} />

      {result && (
        <>
          <MetricsPanel summary={result.summary} />

          <CodeBlock
            title="Original Code"
            code={result.sections.original_code}
          />

          <CodeBlock
            title="Optimized Context"
            code={result.sections.optimized_context}
          />

          <CodeBlock
            title="AI Output"
            code={result.sections.generated_output}
          />
        </>
      )}
    </div>
  );
}