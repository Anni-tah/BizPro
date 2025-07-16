import React from "react";
import AdminSidebar from "./sidebars/AdminSidebar";
import CustomerSidebar from "./sidebars/CustomerSidebar";
import ShopkeeperSidebar from "./sidebars/ShopkeeperSidebar";
import SupplierSidebar from "./sidebars/SupplierSidebar";

const Sidebar = ({ role }) => {
  switch (role) {
    case "admin":
      return <AdminSidebar />;
    case "customer":
      return <CustomerSidebar />;
    case "shopkeeper":
      return <ShopkeeperSidebar />;
    case "supplier":
      return <SupplierSidebar />;
    default:
      return (
        <div className="p-4">
          <p className="text-red-500">No sidebar for role: {role}</p>
        </div>
      );
  }
};

export default Sidebar;
