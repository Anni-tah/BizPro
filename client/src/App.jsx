// src/App.jsx
import React from "react";
import Navbar from "./Components/navbar/Navbar";
import AppRoutes from "./routes/AppRoutes";

const App = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow pt-[80px] px-4">
        <AppRoutes />
      </main>
    </div>
  );
};

export default App;
