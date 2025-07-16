import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import DashboardCard from "../../Components/Shared/DashboardCard";

const SupplierMainDashboard = () => {
  const user = JSON.parse(localStorage.getItem("user"));
  const [orderCount, setOrderCount] = useState(0);
  const [paymentTotal, setPaymentTotal] = useState(0);
  const [deliveryCount, setDeliveryCount] = useState(0);

  useEffect(() => {
    if (!user) return;

    // Supplier Orders
    fetch("http://localhost:5000/supplier_orders")
      .then(res => res.json())
      .then(data => {
        const supplierOrders = data.filter(o => o.supplier_id === user.id);
        setOrderCount(supplierOrders.length);
      });

    // Payments
    fetch("http://localhost:5000/payments")
      .then(res => res.json())
      .then(data => {
        const supplierPayments = data.filter(p => p.supplier_id === user.id);
        const total = supplierPayments.reduce((sum, p) => sum + parseFloat(p.amount), 0);
        setPaymentTotal(total.toFixed(2));
      });

    // Deliveries
    fetch("http://localhost:5000/customer_deliveries")
      .then(res => res.json())
      .then(data => {
        const myDeliveries = data.filter(d => d.supplier_id === user.id);
        setDeliveryCount(myDeliveries.length);
      });
  }, [user]);

  return (
    <div className="space-y-10 px-2 sm:px-4">
      
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <DashboardCard title="Orders" value={orderCount} icon="📦" />
        <DashboardCard title="Deliveries" value={deliveryCount} icon="🚚" />
        <DashboardCard title="Payments" value={`KSh ${paymentTotal}`} icon="💰" />
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
        <Link to="/supplier/orders" className="bg-blue text-white px-4 py-3 rounded shadow text-center hover:bg-blue-light">
          📋 View Orders
        </Link>
        <Link to="/supplier/payments" className="bg-blue text-white px-4 py-3 rounded shadow text-center hover:bg-blue-light">
          💳 View Payments
        </Link>
        <Link to="/supplier/profile" className="bg-blue text-white px-4 py-3 rounded shadow text-center hover:bg-blue-light">
          🙍 My Profile
        </Link>
      </div>
    </div>
  );
};

export default SupplierMainDashboard;
