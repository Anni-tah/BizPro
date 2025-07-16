import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const ChartCard = ({ data, title }) => {
  return (
    <div className="bg-white rounded shadow p-4">
      <h3 className="text-blue text-lg font-bold mb-2">{title}</h3>
      <ResponsiveContainer width="100%" height={200}>
        <BarChart data={data}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" fill="#1D4ED8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default ChartCard;
