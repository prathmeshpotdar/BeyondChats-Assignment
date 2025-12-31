import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/articles')
      .then(response => {
        if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
        return response.json();
      })
      .then(data => {
        console.log("Raw API Data:", data); // Check your browser console to see what came back!

        // ROBUST DATA PARSING (The Fix)
        let safeArticles = [];

        // Case 1: It's already an array
        if (Array.isArray(data)) {
          safeArticles = data;
        } 
        // Case 2: It's a Laravel Paginator (data is inside .data)
        else if (data.data && Array.isArray(data.data)) {
          safeArticles = data.data;
        }
        // Case 3: It's an Object with keys (e.g. { "1": {...}, "2": {...} })
        else if (typeof data === 'object' && data !== null) {
          safeArticles = Object.values(data);
        }

        setArticles(safeArticles);
        setLoading(false);
      })
      .catch(err => {
        console.error("Fetch failed:", err);
        setError(err.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="container">
      <header className="header">
        <h1>BeyondChats Article Upgrader</h1>
      </header>

      {loading && <p className="status">Loading articles...</p>}
      
      {error && (
        <div className="error-box">
          <p><strong>Error:</strong> {error}</p>
          <p>Please check if your Laravel backend is running on port 8000.</p>
        </div>
      )}

      {!loading && !error && articles.length === 0 && (
        <p className="status">No articles found in database.</p>
      )}

      <div className="grid">
        {articles.map(article => (
          <div key={article.id || Math.random()} className="card">
            <h2>{article.title}</h2>
            <div className="comparison">
              <div className="column original">
                <h3>Original</h3>
                <div className="content-box">
                  {article.original_content ? article.original_content.substring(0, 500) + "..." : "No content"}
                </div>
              </div>
              <div className="column updated">
                <h3>AI Enhanced</h3>
                {article.updated_content ? (
                  <>
                    <div className="content-box">{article.updated_content}</div>
                    <div className="refs">
                      <strong>Sources: </strong>
                      {/* Safely handle references if they are a string or array */}
                      {(typeof article.references === 'string' 
                          ? JSON.parse(article.references || '[]') 
                          : (article.references || [])
                      ).map((ref, i) => (
                        <a key={i} href={ref} target="_blank" rel="noreferrer">[{i+1}] </a>
                      ))}
                    </div>
                  </>
                ) : (
                  <p className="pending">Pending AI processing...</p>
                )}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;