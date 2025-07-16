import React, { useEffect, useState } from "react";
import ChartCard from "../../../Components/Shared/ChartCard";

const AdminHomeDashboard = () => {
  const [summary, setSummary] = useState({
    users: 0,
    suppliers: 0,
    products: 0,
    sales: 0,
    orders: 0,
  });

  const [chartData, setChartData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  
  const fetchAdminSummary = async () => {
    try {
      const token = localStorage.getItem("access_token"); 
      console.log("🔐 Token being sent:", token);
      const response = await fetch("http://localhost:5000/admin/summary", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.message || "Failed to fetch summary");
      }

      const data = await response.json();

      // Set summary and chart data with correct field names
      const newSummary = {
        users: data.total_users,
        suppliers: data.total_suppliers,
        products: data.total_products,
        sales: data.total_sales,
        orders: data.total_orders || 0, // Fallback for optional field
      };

      setSummary(newSummary);

      setChartData([
        { name: "Users", value: newSummary.users },
        { name: "Suppliers", value: newSummary.suppliers },
        { name: "Products", value: newSummary.products },
        { name: "Sales", value: newSummary.sales },
        { name: "Orders", value: newSummary.orders },
      ]);
    } catch (error) {
      console.error("Error fetching admin summary:", error.message);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAdminSummary();
  }, []);

  if (loading) return <p className="text-center text-gray-500">Loading...</p>;
  if (error) return <p className="text-center text-red-500">{error}</p>;

  return (
    <div className="p-6 text-gray-800 w-full">
      <h2 className="text-2xl font-semibold mb-6">Admin Dashboard</h2>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <DashboardCard title="Users" count={summary.users} color="bg-blue-600" />
        <DashboardCard title="Suppliers" count={summary.suppliers} color="bg-purple-600" />
        <DashboardCard title="Products" count={summary.products} color="bg-green-600" />
        <DashboardCard title="Sales" count={summary.sales} color="bg-yellow-500" />
        <DashboardCard title="Customer Orders" count={summary.orders} color="bg-pink-600" />
      </div>

      {/* Chart */}
      <div className="mt-8">
        <ChartCard title="System Activity Overview" data={chartData} />
      </div>
    </div>
  );
};

const DashboardCard = ({ title, count, color }) => (
  <div className={`rounded-lg shadow p-4 text-white ${color}`}>
    <h3 className="text-lg font-semibold">{title}</h3>
    <p className="text-3xl mt-2">{count}</p>
  </div>
);

export default AdminHomeDashboard;
