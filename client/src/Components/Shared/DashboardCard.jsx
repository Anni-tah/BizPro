import React from "react";

const DashboardCard = ({ title, value, icon }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow flex items-center space-x-4">
      <div className="text-3xl text-blue">{icon}</div>
      <div>
        <h4 className="text-sm text-gray-500">{title}</h4>
        <p className="text-xl font-bold text-blue">{value}</p>
      </div>
    </div>
  );
};

export default DashboardCard;
