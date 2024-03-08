import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import NotFound from "./pages/NotFound";
import SignInSide from "./pages/LoginPage";
import Deneme from "./pages/Deneme";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ProtectedRoute><Deneme /></ProtectedRoute>} />
        <Route path="/deneme" element={<ProtectedRoute><Deneme /></ProtectedRoute>} />
        <Route path="/login" element={<SignInSide />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}

const ProtectedRoute = ({ children }) => {
  if (localStorage.getItem("user")) {
    return children;
  } else {
    return <Navigate to="/login" replace />;
  }
};

export default App;
