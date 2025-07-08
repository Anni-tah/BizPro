import React from "react";

const features = [
  {
    title: "Suppliers Management",
    description:
      "Easily manage all your suppliers with contact details, order history, and purchase tracking in one place.",
    icon: "🚚",
    bg: "bg-white",
  },
  {
    title: "Customers Management",
    description:
      "Track your customers, their orders, preferences, and feedback, all in one organized view.",
    icon: "👥",
    bg: "bg-blue-100",
  },
  {
    title: "Financial Tracking",
    description:
      "Keep track of your income, expenses, and profit in a centralized dashboard.",
    icon: "💰",
    bg: "bg-white",
  },
  {
    title: "Inventory Management",
    description:
      "Know your stock levels in real-time, avoid shortages, and reorder supplies effortlessly.",
    icon: "📦",
    bg: "bg-blue-100",
  },
];

const FeaturesOverview = () => {
  return (
    <section className="py-16 px-4 bg-white">
      <div className="max-w-6xl mx-auto">
        <div className="mb-3 flex items-center text-sm text-gray-500 gap-2">
          <span>⚡</span>
          <span>Instant Updates</span>
        </div>

        <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
          Transform Your Business with BizPro’s Powerful Suite of Tools
        </h2>
        <p className="text-gray-600 max-w-2xl mb-12">
          BizPro is your command center for business success. Our integrated platform brings everything
          you need — from inventory and suppliers to customer engagement and financial management —
          into one intuitive system, tailored for efficiency and growth.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {features.map((feature, index) => (
            <div
              key={index}
              className={`rounded-xl p-6 border shadow-sm ${feature.bg}`}
            >
              <div className="text-4xl mb-3">{feature.icon}</div>
              <h3 className="text-xl font-semibold text-gray-800 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600 text-sm mb-4">{feature.description}</p>
              <a href="#" className="text-blue-600 text-sm font-medium hover:underline">
                → Go to Dashboard
              </a>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default FeaturesOverview;
