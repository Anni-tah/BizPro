import React from "react";
import {Routes, Route} from "react-router-dom"
import Navbar from "./Navbar";
import Home from "../Home/Home";
import Features from "../Features";
import Contact from "../Contact";
import Pricing from "../Pricing";

function Router() {
  return (
    <div className="min-h-screen flex flex-col">
      <Navbar />
      <main className="flex-grow p-4">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/features" element={<Features />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/pricing" element={<Pricing />} />
        </Routes>
      </main>
    </div>
  );
}

export default Router;