import React, { useEffect, useState } from "react";
import "./Grid.css";
import { FiSearch } from "react-icons/fi";
import { FiX } from "react-icons/fi";
import { FaMicrophone } from 'react-icons/fa';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

const ProductGrid = () => {
  const [search, setSearch] = useState("");
  const [fullStringSearch, setFullStringSearch] = useState("");
  const [correctText, setCorrectText] = useState("");
  const [searchHistory, setSearchHistory] = useState([]);
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

  const fetchSpeechRecognitionProducts = (transcript, page = 1) => {

    return fetch("http://127.0.0.1:8000/semantic-search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        query: transcript,
        top_k: 20,
        page: page,
        items_per_page: 10,
      }),
    })

      .then((res) => res.json())
      .then((data) => {
        setFilteredProducts(data.results || data);
        setUseFiltered(true);
      })
      .catch((err) => console.error("Error in filtering flow:", err));
  };

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

        return fetch("http://127.0.0.1:8000/gpt2-suggestions", {
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

  const SpeechRecognizer = () => {
    const [transcript, setTranscript] = useState("");
    const [listening, setListening] = useState(false);

    const startListening = () => {
      const SpeechRecognition =
        window.SpeechRecognition || window.webkitSpeechRecognition;

      if (!SpeechRecognition) {
        alert("Your browser does not support Speech Recognition");
        return;
      }
      const recognition = new SpeechRecognition();
      recognition.lang = "en-US";
      recognition.interimResults = false;
      recognition.maxAlternatives = 1;

      recognition.onresult = (event) => {
        const speechResult = event.results[0][0].transcript;
        setTranscript(speechResult);
        console.log("Recognized:", speechResult);
      };

      recognition.onerror = (event) => {
        console.error("Speech recognition error", event.error);
      };

      recognition.onend = () => {
        setListening(false);
      };

      recognition.start();
      setListening(true);
    };

    return (
      <div>
        <button onClick={startListening} disabled={listening}>
          {listening ? "Listening..." : "Start Listening"}
        </button>
        <p>Transcript: {transcript}</p>
        {transcript && <button onClick={(e) => { setSearch(transcript); fetchSpeechRecognitionProducts(transcript, 1); setCorrectText(""); }} >Filter data</button>}
      </div>
    );
  }

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
        <h5>The place where you can find dozens of the best quality products. </h5>
      </div>

      <div style={{ padding: "20px", textAlign: "center" }}>
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
          <button onClick={() => { setSearch(""); setCorrectText(""); setFullStringSearch(""); setSearchHistory([]); setSuggestions([]); setUseFiltered(false); }} className="clear-button">
            <FiX />
          </button>
        )}

        {/* <button className="btn-microphone" onClick={() =>
          SpeechRecognizer()
        }>  <FaMicrophone size={24} /></button> */}

      </div>
      {/* 
      <SpeechRecognizer /> */}

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
            src="src/assets/sale.png"
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

export default ProductGrid;
