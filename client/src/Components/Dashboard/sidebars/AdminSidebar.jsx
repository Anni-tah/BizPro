import React, { useState } from "react";
import { Link } from "react-router-dom";

const AdminSidebar = () => {
  const [openUsers, setOpenUsers] = useState(true);
  const [openSuppliers, setOpenSuppliers] = useState(true);
  const [openProducts, setOpenProducts] = useState(true);
  const [openSales, setOpenSales] = useState(true);
  const [openCustomers, setOpenCustomers] = useState(false);
  const [openInventory, setOpenInventory] = useState(false);
  const [openPayments, setOpenPayments] = useState(false);

  return (
    <aside className="h-full p-4 bg-[#1f2937] text-white space-y-4 overflow-y-auto">
      <h1 className="text-2xl font-bold mb-6">BizPro Admin</h1>

      <div className="space-y-2 text-sm">

        {/* Users */}
        <div>
          <button
            onClick={() => setOpenUsers(!openUsers)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>👥 Users</span>
            <span>{openUsers ? "▾" : "▸"}</span>
          </button>
          {openUsers && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/add-user" className="block hover:text-white">Add User</Link>
              <Link to="/dashboard/admin/user-list" className="block hover:text-white">User List</Link>
            </div>
          )}
        </div>

        {/* Suppliers */}
        <div>
          <button
            onClick={() => setOpenSuppliers(!openSuppliers)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>📦 Suppliers</span>
            <span>{openSuppliers ? "▾" : "▸"}</span>
          </button>
          {openSuppliers && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/suppliers" className="block hover:text-white">Supplier List</Link>
              <Link to="/dashboard/admin/supplier-orders" className="block hover:text-white">Supplier Orders</Link>
              <Link to="/dashboard/admin/supplier-order-items" className="block hover:text-white">Supplier Order Items</Link>
            </div>
          )}
        </div>

        {/* Products */}
        <div>
          <button
            onClick={() => setOpenProducts(!openProducts)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>📋 Products</span>
            <span>{openProducts ? "▾" : "▸"}</span>
          </button>
          {openProducts && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/products" className="block hover:text-white">Product List</Link>
            </div>
          )}
        </div>

        {/* Sales */}
        <div>
          <button
            onClick={() => setOpenSales(!openSales)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>💵 Sales</span>
            <span>{openSales ? "▾" : "▸"}</span>
          </button>
          {openSales && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/sales" className="block hover:text-white">Sales List</Link>
              <Link to="/dashboard/admin/sale-items" className="block hover:text-white">Sale Items</Link>
            </div>
          )}
        </div>

        {/* Customers */}
        <div>
          <button
            onClick={() => setOpenCustomers(!openCustomers)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>👨‍👩‍👧 Customers</span>
            <span>{openCustomers ? "▾" : "▸"}</span>
          </button>
          {openCustomers && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/customer-orders" className="block hover:text-white">Customer Orders</Link>
              <Link to="/dashboard/admin/customer-deliveries" className="block hover:text-white">Customer Deliveries</Link>
            </div>
          )}
        </div>

        {/* Inventory */}
        <div>
          <button
            onClick={() => setOpenInventory(!openInventory)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>📦 Inventory</span>
            <span>{openInventory ? "▾" : "▸"}</span>
          </button>
          {openInventory && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/inventory" className="block hover:text-white">Inventory List</Link>
            </div>
          )}
        </div>

        {/* Payments */}
        <div>
          <button
            onClick={() => setOpenPayments(!openPayments)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>💳 Payments</span>
            <span>{openPayments ? "▾" : "▸"}</span>
          </button>
          {openPayments && (
            <div className="pl-4 text-gray-300 space-y-1 mt-1">
              <Link to="/dashboard/admin/payments" className="block hover:text-white">Payment Records</Link>
            </div>
          )}
        </div>

      </div>
    </aside>
  );
};

export default AdminSidebar;
