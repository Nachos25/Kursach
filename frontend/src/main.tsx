import React from "react";
import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import "./index.css";
import App from "./App";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import CatalogPage from "./pages/CatalogPage";
import ProductPage from "./pages/ProductPage";
import OrdersPage from "./pages/OrdersPage";
import ProfilePage from "./pages/ProfilePage";

const root = createRoot(document.getElementById("root")!);

root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        {/* Головний сайт з лейаутом */}
        <Route path="/" element={<App />}>
          <Route index element={<CatalogPage />} />
          <Route path="product/:slug" element={<ProductPage />} />
          <Route path="orders" element={<OrdersPage />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Route>

        {/* Окремі сторінки аутентифікації (без бокового меню/героя) */}
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/profile" element={<ProfilePage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);




