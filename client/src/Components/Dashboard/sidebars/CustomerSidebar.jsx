import React from "react";
import SidebarLink from "../../Shared/SidebarLink";

const CustomerSidebar = () => {
  return (
    <div className="h-screen bg-[#1f2937] text-white p-4 text-sm space-y-2">
      <h2 className="font-bold text-lg mb-6">🛒 Customer Panel</h2>
      <SidebarLink to="/dashboard" icon="🏠" label="Dashboard" />
      <SidebarLink to="/customer/products" icon="🛍" label="View Products" />
      <SidebarLink to="/customer/order" icon="✍️" label="Make Order" />
      <SidebarLink to="/customer/payments" icon="💳" label="Payments" />
      <SidebarLink to="/customer/profile" icon="🙍" label="My Details" />
    </div>
  );
};

export default CustomerSidebar;
