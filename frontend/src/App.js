import React, { useState } from "react";
import axios from "axios";

function App() {
  const [inputText, setInputText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!inputText.trim()) {
      alert("Please enter some text to summarize.");
      return;
    }

    setLoading(true);
    try {
      const response = await axios.post("/api/summarize/", {
        text: inputText,
      });
      setSummary(response.data.summary);
    } catch (error) {
      console.error(error);
      alert("An error occurred while summarizing the text.");
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setInputText("");
    setSummary("");
  };

  const handleCopy = () => {
    navigator.clipboard.writeText(summary);
  };

  const handleSave = () => {
    const blob = new Blob([summary], { type: "text/plain" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "summary.txt";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <div style={styles.app}>
      <h1 style={styles.title}>Text Summarizer</h1>
      <textarea
        style={styles.textarea}
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Paste or type your text here..."
      />
      <div style={styles.buttonGroup}>
        <button style={styles.primaryButton} onClick={handleSubmit} disabled={loading}>
          {loading ? "Summarizing..." : "Summarize"}
        </button>
        <button style={styles.secondaryButton} onClick={handleReset} disabled={loading}>
          Reset
        </button>
      </div>
      {summary && (
        <div style={styles.summary}>
          <div style={styles.summaryHeader}>
            <h2 style={styles.summaryTitle}>Summary</h2>
            <div>
              <button style={styles.primaryButton} onClick={handleCopy}>📋 Copy</button>
              <button style={styles.secondaryButton} onClick={handleSave}>💾 Save</button>
            </div>
          </div>
          <p style={styles.summaryText}>{summary}</p>
        </div>
      )}
    </div>
  );
}

const styles = {
  app: {
    fontFamily: "Arial, sans-serif",
    maxWidth: "600px",
    margin: "40px auto",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0px 4px 10px rgba(0, 0, 0, 0.1)",
    textAlign: "center",
  },
  title: {
    color: "#333",
  },
  textarea: {
    width: "100%",
    height: "150px",
    padding: "10px",
    borderRadius: "5px",
    border: "1px solid #ccc",
    fontSize: "16px",
    resize: "none",
    marginBottom: "15px",
  },
  buttonGroup: {
    display: "flex",
    justifyContent: "center",
    gap: "10px",
  },
  primaryButton: {
    backgroundColor: "#007BFF",
    color: "white",
    border: "none",
    padding: "10px 15px",
    borderRadius: "5px",
    cursor: "pointer",
  },
  secondaryButton: {
    backgroundColor: "#6c757d",
    color: "white",
    border: "none",
    padding: "10px 15px",
    borderRadius: "5px",
    cursor: "pointer",
  },
  summary: {
    marginTop: "20px",
    padding: "15px",
    borderRadius: "5px",
    backgroundColor: "#f8f9fa",
    textAlign: "left",
  },
  summaryHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
  },
  summaryTitle: {
    margin: "0",
  },
  summaryText: {
    marginTop: "10px",
    fontSize: "16px",
  },
};

export default App;
