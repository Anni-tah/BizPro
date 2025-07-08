// src/components/sections/Hero.jsx
import React from "react";

const Hero = () => (
  <section className="relative bg-white min-h-screen pt-[10vh] px-4 flex flex-col items-center text-center">
    <h1 className="text-4xl md:text-6xl font-bold leading-tight">
      Streamline Your Business
      <span className="block text-3xl md:text-5xl text-blue-700 mt-2">
        Operations with BizPro
      </span>
    </h1>
    <p className="mt-4 text-gray-700 max-w-xl">
      Monitor, analyse, and optimize every aspect of your operations.
      Manage suppliers, customers, sales, and finances with ease.
    </p>
    <a
      href="/signup"
      className="mt-6 bg-blue-700 text-white px-6 py-3 rounded-lg
                 hover:bg-blue-800 transition-colors duration-300
                 focus:outline-none focus:ring-2 focus:ring-blue-500
                 focus:ring-opacity-50"
    >
      Get Started
    </a>

    {/* Bottom decorations */}
    <img src="/hero4.png" className="absolute bottom-0 left-0 hidden sm:block h-[33vh]" alt="" />
    <img src="/hero2.png" className="absolute bottom-0 left-1/4 hidden sm:block h-[33vh]" alt="" />
    <img src="/hero2.png" className="absolute bottom-0 right-1/4 h-[33vh]" alt="" />
    <img src="/hero3.png" className="absolute bottom-0 right-0 hidden sm:block h-[33vh]" alt="" />
  </section>
);

export default Hero;
