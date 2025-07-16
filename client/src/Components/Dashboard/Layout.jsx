import React, { useState } from "react";
import Topbar from "./Topbar";
import Sidebar from "./Sidebar";

const Layout = ({ user, children }) => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <div className={`${isSidebarOpen ? "block" : "hidden"} md:block w-64`}>
        <Sidebar role={user.role} />
      </div>

      {/* Main content */}
      <div className="flex-1 flex flex-col overflow-hidden bg-gray">
        <Topbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

        <main className="flex-1 overflow-y-auto p-4">{children}</main>
      </div>
    </div>
  );
};

export default Layout;
