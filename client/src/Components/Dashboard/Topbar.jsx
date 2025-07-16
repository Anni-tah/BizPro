import React from "react";

const Topbar = ({ toggleSidebar }) => {
  return (
    <header className="flex items-center justify-between px-4 py-2 bg-white border-b shadow-sm">
      {/* Toggle sidebar (shown on small screens) */}
      <button
        onClick={toggleSidebar}
        className="md:hidden text-gray-700 focus:outline-none text-xl"
      >
        ☰
      </button>

      <input
        type="text"
        placeholder="Search"
        className="hidden sm:block w-full max-w-sm px-4 py-2 border rounded-md text-sm"
      />

      <div className="flex items-center space-x-4">
        <span className="text-red-500">🔔</span>
        <img
          src="https://i.pravatar.cc/32"
          alt="Avatar"
          className="w-8 h-8 rounded-full object-cover"
        />
      </div>
    </header>
  );
};

export default Topbar;
