import React, { useEffect, useState, useRef } from "react";
import "./Style.css";
import { FiX } from "react-icons/fi";
import { FaMicrophone } from 'react-icons/fa';
import { useNavigate } from "react-router-dom";

const ProductSearch = () => {
  const [search, setSearch] = useState("");
  const [fullStringSearch, setFullStringSearch] = useState("");
  const [correctText, setCorrectText] = useState("");
  const [searchHistory, setSearchHistory] = useState([]);
  const [voiceTranscription, setVoiceTranscription] = useState("");
  const [categories, setCategories] = useState([]);
  const user_id = 12;
  const navigate = useNavigate();

  const getSearchHistory = () => {
    let string = search ? search : "";
    fetch("http://127.0.0.1:8000/searchHistory/" + user_id + "?searchString=" + string)
      .then((res) => res.json())
      .then((data) => {
        setSearchHistory(data || []);
        console.log("search history", data);
      })
      .catch((err) => console.error("Error fetching search history:", err));
  };


  const handleSearchHistoryChange = (e) => {
    const newValue = e.target.value;
    setSearch(newValue);

    console.log("new search value:", newValue);

    if (newValue != "") {
      getSearchHistory();
    }
    else if (newValue == "" || newValue.endsWith(" ")) {
      setSearchHistory([]);
      console.log("search history list:", searchHistory);
    }

  };

  const insertSearchHistory = () => {
    fetch("http://127.0.0.1:8000/searchHistory", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ SearchInput: search, UserID: user_id }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
      })
      .catch((err) => console.error("SearchHistory post error:", err));
  }


  const handleDeleteSearchItem = (id) => {
    fetch(`http://127.0.0.1:8000/searchHistory/${id}`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.ok) {
          setSearchHistory((prev) =>
            prev.filter((item) => item.SearchHistoryID !== id)
          );
        } else {
          console.error("Failed to delete item");
        }
      })
      .catch((err) => console.error("Error deleting search item:", err));

  };

  let correctedText = "";

  const spellCorrection = (e) => {

    fetch("http://127.0.0.1:8000/correct-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: e,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        correctedText = data.corrected_text;
        console.log("correctedText", correctedText);
        setCorrectText(data.corrected_text);
        console.log("correct text", correctText);
        navigate(`/results/${correctedText}`);
      }
      )
      .catch((err) => console.error("Error in filtering flow:", err));
  }

  const [suggestions, setSuggestions] = useState([]);

  const handleSearchChange = (e) => {
    const newValue = e.target.value;
    setSearch(newValue);

    console.log("new search value:", newValue.length);
    console.log("search", search.length);

    // Trigger autocomplete only when user finishes a word
    if (newValue.endsWith(" ") && newValue.trim() !== "") {
      fetchAutocompleteSuggestions(newValue.trim());
    }
    else {
      setSuggestions([]);
    }
  };

  const fetchAutocompleteSuggestions = (inputText) => {
    let cleaned = inputText.trim();
    console.log("input text", inputText.length);
    setFullStringSearch(cleaned);

    if (inputText.trim() == "") {
      setCorrectText("");
    }

    fetch("http://127.0.0.1:8000/correct-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: cleaned,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        correctedText = data.corrected_text;
        console.log("correctedText", correctedText);
        setCorrectText(data.corrected_text);
        console.log("correct text", correctText);

        return fetch("http://127.0.0.1:8000/gpt4-suggestions", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            prompt: data.corrected_text,
            top_k: 5,

          }),
        });
      })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        console.log(data.suggestions);
        setSuggestions(data.suggestions || []);
      })
      .catch((err) => console.error("Error in filtering flow:", err));
  };


const AudioSearch = () => {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const controllerRef = useRef(null); // to store AbortController

  const handleSearch = async () => {
    setLoading(true);
    setResult(null);
    
    const controller = new AbortController();
    controllerRef.current = controller;

    try {
      const response = await fetch('http://127.0.0.1:8000/audio/search', {
        method: 'POST',
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();
      setResult(data);
      console.log(data);
    } catch (error) {
      if (error.name === 'AbortError') {
        console.log("Fetch aborted.");
      } else {
        console.error("Error calling audio search:", error);
      }
    } finally {
      setLoading(false);
    }
  };

  const cancelSearch = () => {
    if (controllerRef.current) {
      controllerRef.current.abort(); // cancels the fetch
    }
    setLoading(false);
    setResult(null);
  };

  return (
    <div className="audioSearch">
      <button
        style={{ color: loading ? 'black' : 'grey' }}
        className="btn-microphone"
        onClick={handleSearch}
        disabled={loading}
      >
        <FaMicrophone size={24} />
      </button>

      <div className="audioSearch-loading">
        {loading && <h6>Recording and transcribing...</h6>}
        {loading && (
          <button
            style={{
              color: 'red',
              background: 'none',
              border: 'none',
              fontSize: '18px',
            }}
            onClick={cancelSearch}
          >
            <FiX />
          </button>
        )}
      </div>

      {!loading && result !== null && result.transcription !== ". ." ? (
        spellCorrection(result.transcription)
      ) : (
        <p></p>
      )}
    </div>
  );
};


  useEffect(() => {
    // initial load
    // getCategories();
  }, []);


  // const getCategories = () => {
  //   fetch('http://127.0.0.1:8000/categories')
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setCategories(data || []);
  //       console.log("categories", data);
  //     })
  //     .catch((err) => console.error("Error fetching categories:", err));
  // };


  return (
    <>

      <div className="title">
        <h1>Welcome to the eShop! 🏬</h1>
        <h5>The place where you can find dozens of the high quality products. </h5>
      </div>

      <div style={{ padding: "20px", textAlign: "center" }} className="searchEngine-div">
        <input
          className="search-container"
          type="text"
          placeholder="🔍 Search products..."
          value={search}
          onChange={(e) => { handleSearchChange(e); handleSearchHistoryChange(e); }}
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              insertSearchHistory(); setSearchHistory([]); setSuggestions([]);
              if (search.trim() !== "") {
                spellCorrection(search);
              }
            }
          }}
        />
        {search && (
          <button onClick={() => { setSearch(""); setCorrectText(""); setFullStringSearch(""); 
          setSearchHistory([]); setSuggestions([]); }} className="clear-button">
            <FiX />
          </button>
        )}
        <AudioSearch />
      </div>

      {correctText && correctText.trim() !== "" && correctText !== fullStringSearch && fullStringSearch !== "" && <div className="didYouMean"><h6>Did you mean: </h6> <h4 className="correctText" onClick={() => {
        setSearch(correctText);
        console.log("search", search);
        setFullStringSearch(correctText);
      }}>{correctText}</h4></div>}

      <div className="history-and-autocomplete">

        {searchHistory.length > 0 && (
          <div className="searchHistory-wrapper">
            <h6>Your search history:</h6>
            <ul className="searchHistory-list">
              {searchHistory.map((obj, index) => (
                <li key={index} onClick={() => {
                  setSearch(obj.SearchInput); setFullStringSearch(obj.SearchInput);
                  spellCorrection(obj.SearchInput);
                }}>
                  🕒 {obj.SearchInput}
                  <button
                    onClick={() => handleDeleteSearchItem(obj.SearchHistoryID)}
                    className="delete-btn"
                  >
                    &#x2715;
                  </button>
                </li>
              ))}
            </ul>

          </div>
        )}

        {suggestions.length > 0 && (
          <div className="autocomplete-wrapper">
            <h6>Search suggestions:</h6>
            <ul className="autocomplete-list">
              {suggestions.map(({ suggestion }, index) => (
                <li
                  key={index}
                  onClick={() => {
                    const newSearch = correctText + " " + suggestion + " ";
                    setSearch(newSearch);
                    setFullStringSearch(newSearch);
                    setCorrectText(newSearch);
                    setSuggestions([]);
                    spellCorrection(newSearch);
                  }}
                > 🔎
                  {correctText !== fullStringSearch ? (
                    <>
                      <b>{correctText} {suggestion}</b> </>
                  ) : (
                    <>
                      {fullStringSearch} <b>{suggestion}</b>
                    </>
                  )}

                </li>
              ))}
            </ul>

          </div>
        )}
      </div>


      <div className="image-text">
        <div className="title-image">
          <h4 style={{ textTransform: "uppercase" }}>A big sale!</h4>
          <h6>Find the desirable products at the lowest prices!</h6>
          <button className="btn-searchNew" onClick={() => { navigate(`/results/sale`); }}>Search now 🡺 </button>
        </div>

        <div className="image-container">
          <img
            src="src/assets/sale2.jpg"
            alt="name"
            className="big-image"
          />
        </div>

      </div>

      {/* <div className="categories">
        {categories.length > 0 && (
          <div className="categories-wrapper">
            <h6>Categories:</h6>
            <ul className="category-list">
              {categories.map(({ CategoryName }, index) => (
                <li
                  key={index}
                >
                  <>
                    <b>{CategoryName}</b> </>
                </li>
              ))}
            </ul>

          </div>
        )}
      </div> */}

    </>

  );
};

export default ProductSearch;
