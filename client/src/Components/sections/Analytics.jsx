// src/components/sections/Analytics.jsx
import React from "react";
import { FiActivity } from "react-icons/fi";

const Analytics = () => {
  return (
    <section className="bg-white py-20 px-6">
      <div className="max-w-6xl mx-auto text-left">
        <div className="mb-6 flex items-center space-x-2 text-gray-600 text-sm">
          <FiActivity className="text-lg" />
          <span>Always Stay Ahead</span>
        </div>
        <h2 className="text-4xl font-bold mb-4">Proactive Real-Time Monitoring</h2>
        <p className="text-gray-700 text-lg max-w-2xl mb-10">
          Gain critical insights by monitoring your business activities in real-time,
          ensuring you're always one step ahead.
        </p>
        <img
          src="/analytics.png"
          alt="Real-Time Monitoring"
          className="rounded-xl shadow-lg w-full"
        />
      </div>
    </section>
  );
};

export default Analytics;
