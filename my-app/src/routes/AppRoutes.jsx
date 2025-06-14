import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ProductSearch from '../components/Search';
import SearchResults from '../components/Results';

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<ProductSearch />} />
      <Route path="/results/:search" element={<SearchResults />} />
    </Routes>
  );
}

export default AppRoutes;
