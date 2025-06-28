import React from "react";

function Hero() {
  return (
    <div className="flex flex-col items-center text-center min-h-screen pt-[10vh] p-4">
      <h1 className="text-4xl md:text-6xl font-bold">
        Streamline Your Business
        <span className="block text-3xl md:text-5xl text-blue-700">Operation with BizPro</span>
      </h1>
      <p className="mt-2">Monitor, analyse and optimize every aspect of your operations</p>
      <p className="mb-4">To manage suppliers, customers, sales and finances with ease</p>
      <button className="bg-blue-700 text-white px-4 py-2 rounded hover:bg-red-400">
        Get started Now
      </button>
      {/* images at the bottom */}
      <img src="/hero4.png" className="absolute bottom-0 left-0 hidden sm:block h-[33vh] w-auto"/>
      <img src="/hero2.png" className="absolute bottom-0 left-1/4 hidden sm:block h-[33vh] w-auto"/>
      <img src="/hero2.png" className="absolute bottom-0 right-1/4 h-[33vh] w-auto" alt="Decoration 3" />
      <img src="/hero3.png" className="absolute bottom-0 right-0 hidden sm:block h-[33vh] w-auto"/>
    </div>
  );
}

export default Hero;
