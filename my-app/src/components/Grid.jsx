import React, { useEffect, useState } from "react";
import "./Grid.css";
import { FiSearch } from "react-icons/fi";
import { FiX } from "react-icons/fi";
import { FaMicrophone } from 'react-icons/fa';

const ProductGrid = () => {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [useFiltered, setUseFiltered] = useState(false);
  const [search, setSearch] = useState("");
  const [fullStringSearch, setFullStringSearch] = useState("");
  const [correctText, setCorrectText] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const [searchHistory, setSearchHistory] = useState([]);
  const totalPages = 2; //top_k/items_per_page
  const user_id = 12;

  const getSearchHistory = () => {
    let string = search ? search : "";
    fetch("http://127.0.0.1:8000/searchHistory/" + user_id + "?searchString=" + string)
      .then((res) => res.json())
      .then((data) => {
        setSearchHistory(data);
        console.log("search history", data);
      })
      .catch((err) => console.error("Error fetching products:", err));
  };


  const handleSearchHistoryChange = (e) => {
    const newValue = e.target.value;
    setSearch(newValue);

    console.log("new search value:", newValue);

    if (newValue != "") {
      getSearchHistory();
    }
    else {
      setSearchHistory([]);
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
          // Optionally update local state
          setSearchHistory((prev) =>
            prev.filter((item) => item.SearchHistoryID !== id)
          );
        } else {
          console.error("Failed to delete item");
        }
      })
      .catch((err) => console.error("Error deleting search item:", err));

  };

  const fetchProducts = () => {
    fetch("http://127.0.0.1:8000/products")
      .then((res) => res.json())
      .then((data) => {
        setProducts(data);
        setUseFiltered(false);
      })
      .catch((err) => console.error("Error fetching products:", err));
  };

  let correctedText = "";

  const fetchFilteredProducts = (page = 1) => {
    fetch("http://127.0.0.1:8000/correct-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        text: search,
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        correctedText = data.corrected_text;
        console.log("correctedText", correctedText);
        setCorrectText(data.corrected_text);

        return fetch("http://127.0.0.1:8000/semantic-search", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            query: data.corrected_text,
            top_k: 20,
            page: page,
            items_per_page: 10,
          }),
        });
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

    console.log("new search value:", newValue);

    // Trigger autocomplete only when user finishes a word
    if (newValue.endsWith(" ")) {
      fetchAutocompleteSuggestions(newValue.trim());
    }
    else {
      setSuggestions([]);
    }

  };

  const fetchAutocompleteSuggestions = (inputText) => {
    fetch("http://127.0.0.1:8000/suggest-next-words", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ context: [inputText] }),
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data.suggestions);
        setSuggestions(data.suggestions || []);
      })
      .catch((err) => console.error("Autocomplete fetch error:", err));
  };


  const [isMicrohoneClicked, setMicrophoneClicked] = useState(false);
  const speechRecognition = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/speech-to-text");
      if (!response.ok) {
        throw new Error("Failed to get speech-to-text result");
      }
      const data = await response.json();
      console.log("Recognized text:", data);
      // Optionally update your input field or state with it
      setSearch(data);
      setMicrophoneClicked(true);
    } catch (error) {
      console.error("Error calling speech-to-text API:", error);
    }
  };


  useEffect(() => {
    fetchProducts(); // initial load
  }, []);


  const displayedProducts = useFiltered ? filteredProducts : products;


  const handlePageChange = (page, totalPages) => {
    if (page < 1 || page > totalPages) return;
    setCurrentPage(page);
    fetchFilteredProducts(page);
  };

  return (
    <>
      <div className="title">
        <h1>Everything in one place!</h1>
      </div>

      <div style={{ padding: "20px", textAlign: "center" }}>
        <input
          className="search-container"
          type="text"
          placeholder="Search products..."
          value={search}
          onChange={(e) => { handleSearchChange(e); handleSearchHistoryChange(e); }} //setSearch(e.target.value);
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              search == "" ? fetchProducts() : fetchFilteredProducts(); setCurrentPage(1); setFullStringSearch(search);
              insertSearchHistory();
            }
          }}
        />
        {search && (
          <button onClick={() => { setSearch(""); setCorrectText(""); setFullStringSearch(""); setSearchHistory([]) }} className="clear-button">
            <FiX />
          </button>
        )}
        <button className="btn-microphone" onClick={() =>
          speechRecognition()
        }>  <FaMicrophone size={24} /></button>
        {/* <button type="button" className="searchButton" onClick={() => { search == "" ? fetchProducts() : fetchFilteredProducts(); setCurrentPage(1); setFullStringSearch(search); }} >
          <FiSearch className="search-icon" />
        </button> */}
      </div>

      {isMicrohoneClicked && <div><p>say something...</p></div>}

      {correctText && correctText.trim() !== "" && correctText !== fullStringSearch && fullStringSearch !== "" && <div className="didYouMean"><h6>Did you mean: </h6> <h4 className="correctText">{correctText}</h4></div>}


      {searchHistory.length > 0 && (
        <div className="searchHistory-wrapper">
          <ul className="searchHistory-list">
            {searchHistory.map((obj, index) => (
              <li key={index} onClick={() => setSearch(obj.SearchInput)}>
                {obj.SearchInput}
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
          <ul className="autocomplete-list">
            {suggestions.map((word, index) => (
              <li key={index} onClick={() => setSearch(search + word + " ")}>
                {word}
              </li>
            ))}

          </ul>

        </div>
      )}



      <div className="grid-container">
        {displayedProducts.map((product) => (
          <div key={product.ProductID} className="product-card">
            <div>
              {product.ProductLabel.LabelName == "Sale" && (
                <h4 className="productLabel" id="sale">
                  {product.ProductLabel.LabelName}
                </h4>
              )}
              {product.ProductLabel.LabelName == "New" && (
                <h4 className="productLabel" id="new">
                  {product.ProductLabel.LabelName}
                </h4>
              )}
            </div>

            <div className="productImage">
              {product.ProductImage.ImageBase64 === "" ? (
                <img
                  src="src/assets/react.svg"
                  alt={product.ProductName}
                  className="product-image"
                />
              ) : (
                <img
                  src={product.ProductImage.ImageBase64}
                  alt={product.ProductName}
                  className="product-image"
                />
              )}
            </div>

            <div className="productName">
              <h3 className="product-name">{product.ProductName}</h3>
            </div>
            <p className="productCaption">{product.ProductCaption}</p>

            {product.ProductLabel.LabelName == "Sale" && (
              <h5>
                <s className="crossedPrice">${product.ProductPrice}</s>
              </h5>
            )}
            {product.ProductLabel.LabelName == "Sale" && <br></br>}
            {product.ProductLabel.LabelName == "Sale" ? (
              <h5 className="productPrice" id="newPrice">
                ${product.NewPrice}
              </h5>
            ) : (
              <h5 className="productPrice">${product.ProductPrice}</h5>
            )}
          </div>
        ))}
      </div>

      {useFiltered &&
        <div className="pagination">
          <button
            onClick={() => handlePageChange(currentPage - 1, totalPages)}
            disabled={currentPage === 1}
            className="pagination-btn"
          >
            &#8592;
          </button>

          <span className="page-number">{currentPage}</span>

          <button
            onClick={() => handlePageChange(currentPage + 1, totalPages)}
            disabled={currentPage === totalPages}
            className="pagination-btn"
          >
            &#8594;
          </button>
        </div>
      }
    </>

  );
};

export default ProductGrid;
