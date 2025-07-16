import React, { useState } from "react";
import { Link } from "react-router-dom";

const SupplierSidebar = () => {
  const [openProfile, setOpenProfile] = useState(true);
  const [openFinances, setOpenFinances] = useState(true);
  const [openReports, setOpenReports] = useState(false);

  return (
    <aside className="h-full p-4 bg-[#1f2937] text-white space-y-4">
      <h1 className="text-2xl font-bold mb-6">BizPro</h1>

      <div className="space-y-2 text-sm">
        <div className="font-semibold mb-1 text-gray-400">SUPPLIER</div>

        {/* Supplier Profile */}
        <div>
          <button
            onClick={() => setOpenProfile(!openProfile)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>📄 Supplier Profile</span>
            <span>{openProfile ? "▾" : "▸"}</span>
          </button>
          {openProfile && (
            <div className="pl-4 text-sm text-gray-300 space-y-1 mt-1">
              <Link to="/supplier/add" className="hover:text-white block">Add Supplier</Link>
              <Link to="/supplier/list" className="hover:text-white block">Supplier List</Link>
            </div>
          )}
        </div>

        {/* Supplier Finances */}
        <div>
          <button
            onClick={() => setOpenFinances(!openFinances)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>💰 Supplier Finances</span>
            <span>{openFinances ? "▾" : "▸"}</span>
          </button>
          {openFinances && (
            <div className="pl-4 text-sm text-gray-300 space-y-1 mt-1">
              <Link to="/supplier/postings" className="hover:text-white block">Supplier Postings</Link>
              <Link to="/supplier/invoice-booking" className="hover:text-white block">Invoice Booking</Link>
              <Link to="/supplier/payment-form" className="hover:text-white block">Payment Form</Link>
              <Link to="/supplier/statement" className="hover:text-white block">Supplier Statement</Link>
            </div>
          )}
        </div>

        {/* Reports */}
        <div>
          <button
            onClick={() => setOpenReports(!openReports)}
            className="flex justify-between w-full text-left px-2 py-1 hover:bg-gray-700 rounded"
          >
            <span>📊 Reports</span>
            <span>{openReports ? "▾" : "▸"}</span>
          </button>
          {openReports && (
            <div className="pl-4 text-sm text-gray-300 space-y-1 mt-1">
              <Link to="/supplier/reports" className="hover:text-white block">View Reports</Link>
            </div>
          )}
        </div>
      </div>
    </aside>
  );
};

export default SupplierSidebar;
