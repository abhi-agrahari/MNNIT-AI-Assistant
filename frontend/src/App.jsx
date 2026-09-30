import { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import "./App.css";

const API_URL = import.meta.env.VITE_API_URL;

function App() {
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, loading]);

  const askQuestion = async () => {
    if (!question.trim() || loading) return;

    const currentQuestion = question;
    setQuestion("");
    setLoading(true);
    setError("");

    try {
      // send the question to the backend API
      const response = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: currentQuestion, college_id: "mnnit" }),
      });

      if (!response.ok) throw new Error("Failed to get response");

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          question: currentQuestion,
          answer: data.answer,
          sources: data.sources,
        },
      ]);
    } catch (err) {
      setError("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="header">
        <h1>MNNIT College RAG</h1>
        <p className="subtitle">Ask questions about MNNIT</p>
      </div>

      <div className="chat-history">
        {messages.map((message, index) => (
          <div className="conversation" key={index}>
            {/* User question section */}
            <div className="question">
              <strong>You:</strong>
              <p>{message.question}</p>
            </div>

            {/* AI answer section */}
            <div className="answer-box">
              <strong>AI</strong>
              <div className="markdown-body">
                <ReactMarkdown remarkPlugins={[remarkGfm]}>
                  {message.answer}
                </ReactMarkdown>
              </div>

              {message.sources?.length > 0 && (
                <div className="sources">
                  <h3>Sources</h3>
                  {message.sources.map((source, sourceIndex) => (
                    <div key={sourceIndex} className="source">
                      {source.document_id} - Page {source.page_number}
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      <div className="bottom-container">
        {error && <p className="error">{error}</p>}
        <div className="input-section">
          <input
            type="text"
            placeholder="Ask a question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && askQuestion()}
          />
          <button onClick={askQuestion} disabled={loading}>
            {loading ? "Asking..." : "Ask"}
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;