import React from 'react';
import { Routes, Route } from 'react-router-dom';
import ProductGrid from '../components/Grid';
import Results from '../components/Results';

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<ProductGrid />} />
      <Route path="/results/:search" element={<Results />} />
    </Routes>
  );
}

export default AppRoutes;
