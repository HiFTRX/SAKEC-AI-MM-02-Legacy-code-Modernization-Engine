import { useState } from "react";
import { analyzeFile } from "../services/api";

export default function FileUploader({ setResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Upload a file");

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const res = await analyzeFile(formData);
      setResult(res.data);
    } catch (err) {
      alert("Error analyzing file");
    }
    setLoading(false);
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}