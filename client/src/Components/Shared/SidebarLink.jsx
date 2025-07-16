import React from "react";
import { NavLink } from "react-router-dom";

const SidebarLink = ({ to, icon, label }) => {
  const base =
    "flex items-center space-x-2 px-4 py-2 rounded hover:bg-blue-light hover:text-white transition";

  return (
    <NavLink
      to={to}
      className={({ isActive }) =>
        `${base} ${isActive ? "bg-blue text-white" : "text-white"}`
      }
    >
      <span>{icon}</span>
      <span>{label}</span>
    </NavLink>
  );
};

export default SidebarLink;
