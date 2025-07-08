import React from "react";
import Hero from "../../Components/sections/Hero";
import Cta from "../../Components/sections/Cta";
import FeaturesOverview from "../../Components/sections/FeaturesOverview";
import Analytics from "../../Components/sections/Analytics";
import Footer from "../../Components/common/Footer";  

function Home() {
  return (
    <div className="bg-white text-gray-800">
      <Hero />
      <FeaturesOverview />
      <Analytics />
      <Cta />
      <Footer />
    </div>
  );
}

export default Home;
