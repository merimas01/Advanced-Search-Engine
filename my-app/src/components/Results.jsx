import React, { useState, useEffect } from 'react';
import { Link, useParams } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import "./Style.css";

function SearchResults() {
    const { search } = useParams();
    const [filteredProducts, setFilteredProducts] = useState([]);
    const totalPages = 2; //top_k/items_per_page
    const [currentPage, setCurrentPage] = useState(1);
    const [correctText, setCorrectText] = useState("");
    const navigate = useNavigate();

    let correctedText = "";

    const fetchFilteredProducts = (e, page = 1) => {
       // console.log("search", search);
        let cleaned = e.trimEnd();
       // console.log("cleaned", cleaned);


        if (search.trim() == "") {
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
              //  console.log("correctedText", correctedText);
                setCorrectText(data.corrected_text);
            //    console.log("correct text", correctText);

                return fetch("http://127.0.0.1:8000/semantic-search", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        query: data.corrected_text,
                        top_k: 20,
                        page: page,
                        items_per_page: 12,
                    }),
                });
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                setFilteredProducts(data.results || data);

            })
            .catch((err) => console.error("Error in filtering flow:", err));
    };

    const handlePageChange = (e, page, totalPages) => {
        if (page < 1 || page > totalPages) return;
        setCurrentPage(page);
        fetchFilteredProducts(e, page);
    };


    useEffect(() => {
        if(search!=null || search!="")
        fetchFilteredProducts(search, 1); // initial load
    }, []);



    return <>
     <h1 className="titleResults text-4xl font-bold text-gray-800 tracking-tight leading-snug mb-4">
      {search}
    </h1>
        
        <div className='goBack'>
            <button onClick={() => { navigate("/"); }} className='btn-homepage'>⬅️ Go back to the home page</button>
        </div>


        <div className="grid-container">
            {filteredProducts.map((product) => (
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
                        {product.ProductLabel.LabelName == "Promo" && (
                            <h4 className="productLabel" id="promo">
                                {product.ProductLabel.LabelName}
                            </h4>
                        )}
                    </div>

                    <div className="productImage">
                        {product.ProductImage.ImageBase64 == null ? (
                            <img
                                src="src/assets/no-image.svg"
                                alt={product.ProductName}
                                className="product-image"
                            />
                        ) : (
                            <img
                                src={product.ProductImage.ImageBase64} //`data:image/jpeg;base64${product.ProductImage.ImageBase64}`
                                alt={product.ProductName}
                                className="product-image"
                            />
                        )}
                    </div>

                    <div className="productName">
                        <h3 className="product-name">{product.ProductName}</h3>
                    </div>
                    <p className="productCaption">{product.ProductCaption}</p>
                    <p className='productColor' style={{ background: product.ProductColor.ColorName, color: product.ProductColor.ColorName }}>.</p>

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


        <div className="pagination">
            <button
                onClick={(e) => handlePageChange(search, currentPage - 1, totalPages)}
                disabled={currentPage === 1}
                className="pagination-btn"
            >
                &#8592;
            </button>

            <span className="page-number">{currentPage}</span>

            <button
                onClick={(e) => handlePageChange(search, currentPage + 1, totalPages)}
                disabled={currentPage === totalPages}
                className="pagination-btn"
            >
                &#8594;
            </button>
        </div>

    </>;
}

export default SearchResults;