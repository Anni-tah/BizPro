import React from "react";
import { NavLink } from "react-router-dom";
import SidebarLink from "../Shared/SidebarLink"; // Reusable styled link component

const CustomerSidebar = () => {
  return (
    <div className="h-full p-4 text-sm space-y-2">
      <h2 className="text-white font-bold text-lg mb-6">🛒 Customer Panel</h2>

      <SidebarLink to="/dashboard/customer" icon="🏠" label="Dashboard" />
      <SidebarLink to="/customer/products" icon="🛍️" label="View Products" />
      <SidebarLink to="/customer/order" icon="✍️" label="Make Order" />
      <SidebarLink to="/customer/payments" icon="💳" label="Payments" />
      <SidebarLink to="/customer/profile" icon="🙍" label="My Details" />
    </div>
  );
};

export default CustomerSidebar;
