import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import DashboardCard from "../../../Components/Shared/DashboardCard";
import InfoBadge from "../../../Components/Shared/InfoBadge";
import ChartCard from "../../../Components/Shared/ChartCard";

const CustomerMainDashboard = () => {
  const user = JSON.parse(localStorage.getItem("user"));
  const [orderCount, setOrderCount] = useState(0);
  const [paymentTotal, setPaymentTotal] = useState(0);
  const [deliveryCount, setDeliveryCount] = useState(0);
  const [invoiceCount, setInvoiceCount] = useState(0);
  const [recentOrders, setRecentOrders] = useState([]);

  useEffect(() => {
    if (!user) return;

    // Fetch Orders
    fetch("http://localhost:5000/customer_orders")
      .then((res) => res.json())
      .then((orders) => {
        const filtered = orders.filter((o) => o.user_id === user.id);
        setOrderCount(filtered.length);
        setRecentOrders(filtered.slice(0, 5));
      });

    // Fetch Payments
    fetch("http://localhost:5000/payments")
      .then((res) => res.json())
      .then((payments) => {
        const myPayments = payments.filter((p) => p.user_id === user.id);
        const total = myPayments.reduce((sum, p) => sum + parseFloat(p.amount), 0);
        setPaymentTotal(total.toFixed(2));
      });

    // Fetch Deliveries
    fetch("http://localhost:5000/customer_deliveries")
      .then((res) => res.json())
      .then((deliveries) => {
        const myDeliveries = deliveries.filter((d) => d.user_id === user.id);
        setDeliveryCount(myDeliveries.length);
      });

    // Dummy Invoice Count
    setInvoiceCount(3);
  }, [user]);

  return (
    <div className="space-y-10 px-2 sm:px-4">
      {/* Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <DashboardCard title="My Orders" value={orderCount} icon="📦" />
        <DashboardCard title="Payments" value={`KSh ${paymentTotal}`} icon="💳" />
        <DashboardCard title="Deliveries" value={deliveryCount} icon="🚚" />
        <DashboardCard title="Invoices" value={invoiceCount} icon="🧾" />
      </div>

      {/* Action Links */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        <Link to="/customer/products" className="bg-blue text-white px-4 py-3 rounded shadow text-center font-medium hover:bg-blue-light">
          🛍 View Products
        </Link>
        <Link to="/customer/order" className="bg-blue text-white px-4 py-3 rounded shadow text-center font-medium hover:bg-blue-light">
          ✍ Make Order
        </Link>
        <Link to="/customer/payments" className="bg-blue text-white px-4 py-3 rounded shadow text-center font-medium hover:bg-blue-light">
          💳 Make Payment
        </Link>
        <Link to="/customer/profile" className="bg-blue text-white px-4 py-3 rounded shadow text-center font-medium hover:bg-blue-light">
          🙍 My Details
        </Link>
      </div>

      {/* Recent Orders */}
      <div className="mt-6">
        {recentOrders.length === 0 ? (
          <p className="text-gray-600">You haven't placed any orders yet.</p>
        ) : (
          <div className="overflow-x-auto rounded shadow bg-white">
            <table className="min-w-full text-sm">
              <thead className="bg-gray text-left text-gray-700">
                <tr>
                  <th className="p-3">Order ID</th>
                  <th className="p-3">Status</th>
                  <th className="p-3">Items</th>
                  <th className="p-3">Total</th>
                </tr>
              </thead>
              <tbody>
                {recentOrders.map((order) => (
                  <tr key={order.id} className="border-b hover:bg-gray-100">
                    <td className="p-3">{order.id}</td>
                    <td className="p-3">
                      <InfoBadge status={order.status || "Pending"} />
                    </td>
                    <td className="p-3">{order.items?.length || 1}</td>
                    <td className="p-3">KSh {order.total || "0.00"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </div>
  );
};

export default CustomerMainDashboard;
