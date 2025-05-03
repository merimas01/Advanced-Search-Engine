import React, { useEffect, useState } from "react";
import "./Grid.css";
import { FiSearch } from "react-icons/fi";

const ProductGrid = () => {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");
  const [currentPage, setCurrentPage] = useState(1);
  const totalPages = 10;

  useEffect(() => {
    fetch("http://127.0.0.1:8000/products")
      .then((res) => res.json())
      .then((data) => setProducts(data))
      .catch((err) => console.error("Error fetching products:", err));
  }, []);

  // Filter products by name or caption
  const filteredProducts = products.filter(
    (product) =>
      product.ProductName.toLowerCase().includes(search.toLowerCase()) ||
      product.ProductCaption.toLowerCase().includes(search.toLowerCase())
  );

  const handlePageChange = (page, totalPages) => {
    if (page < 1 || page > totalPages) return; // Prevent going out of bounds
    setCurrentPage(page);
    onPageChange(page); // Call parent callback to handle the page change
  };

  return (
    <>
      <div class="title">
        <h1>Everything in one place!</h1>
      </div>
      <div style={{ padding: "20px", textAlign: "center" }}>
        <input
          className="search-container"
          type="text"
          placeholder="Search products..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        {search && <button>x</button>}
        <button type="button" className="searchButton">
          <FiSearch className="search-icon" />
        </button>
      </div>

      <div className="grid-container">
        {products.map((product) => (
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
                  src="/public/no-image.svg"
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
    </>
  );
};

export default ProductGrid;
